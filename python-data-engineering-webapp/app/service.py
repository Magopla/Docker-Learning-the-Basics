from __future__ import annotations

import random
from collections import defaultdict
from datetime import date, timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models import GoalEvent, Match, SeasonState, Team


TEAM_DATA = [
    ("Northbridge City", "NBC", "Northbridge", 90, "Harbor Arena", ["Ruben Moya", "Leo Duarte", "Pablo Serra", "Nico Prado"]),
    ("Kingsport Athletic", "KSA", "Kingsport", 88, "King's Ground", ["Iker Solis", "Martin Vale", "Jorge Cano", "Elias Mendez"]),
    ("Redhaven FC", "RHF", "Redhaven", 86, "Forge Park", ["Dani Paredes", "Samu Costa", "Mateo Linares", "Lucas Ferrer"]),
    ("Bluecastle United", "BCU", "Bluecastle", 84, "Castle View", ["Adrian Vega", "Teo Marin", "Ivan Claret", "Mario Sanz"]),
    ("Riverside Rovers", "RSR", "Riverside", 82, "Riverside Park", ["Gabi Pena", "Hugo Nieto", "Aitor Gil", "Rafa Otero"]),
    ("Stonefield Town", "SFT", "Stonefield", 81, "Granite Lane", ["Raul Mena", "Alex Vives", "Bruno Sala", "Jose Roman"]),
    ("Lakeside Albion", "LSA", "Lakeside", 80, "Lakefront Stadium", ["Unai Soto", "Pol Rubio", "David Miro", "Mikel Roca"]),
    ("Ironvale CF", "IVC", "Ironvale", 79, "Steelworks Field", ["Nestor Rey", "Julen Pastor", "Sergio Cruz", "Jaime Vidal"]),
    ("Eastgate FC", "EGF", "Eastgate", 78, "Gateway Park", ["Pepe Bravo", "Julio Vela", "Victor Rios", "Mario Luna"]),
    ("Westport Rangers", "WPR", "Westport", 77, "Portside Stadium", ["Toni Galan", "Mauro Nieto", "Diego Cases", "Enzo Pardo"]),
    ("Hillview Athletic", "HVA", "Hillview", 76, "Summit Field", ["Santi Mena", "Rafa Cuesta", "Alvaro Rey", "Hector Pino"]),
    ("Oakridge Town", "ORT", "Oakridge", 75, "Oakridge Park", ["Joel Marin", "Alex Luque", "Pau Roman", "Dario Costa"]),
    ("Southfield United", "SFU", "Southfield", 74, "Southfield Bowl", ["Mikel Conde", "Pol Vives", "Aitor Sanz", "Noel Flores"]),
    ("Brighton Vale", "BRV", "Brighton Vale", 73, "Vale Arena", ["Bruno Soler", "Cesar Mulet", "Adri Moya", "Ivan Rubio"]),
    ("Crownford FC", "CFC", "Crownford", 72, "Crown Stadium", ["Oscar Lara", "Javi Bello", "Luis Tello", "Pedro Hita"]),
    ("Maplebridge SC", "MSC", "Maplebridge", 71, "Maple Park", ["Eric Navas", "Gael Ortiz", "Dani Ruiz", "Ciro Abad"]),
    ("Harbor Youth", "HBY", "Harbor", 70, "Docklands Ground", ["Asier Pardo", "Yago Peña", "Roi Mena", "Coke Vera"]),
    ("Pinehurst Club", "PHC", "Pinehurst", 69, "Pinehurst Lane", ["Unai Vera", "Saul Iborra", "Nico Cobo", "Marc Tena"]),
    ("Granite Albion", "GRA", "Granite", 68, "Granite Dome", ["Julen Vera", "Tomas Miro", "Kevin Mena", "Dani Yusta"]),
    ("Rivergate 04", "RG4", "Rivergate", 67, "Rivergate 04 Park", ["Axel Pons", "Jorge Pina", "Sergi Luque", "Marc Campos"]),
]

LEAGUE_INFO = {
    "name": "Data Engineering Premier League",
    "country": "Simulated Nation",
    "season": "2026/27",
}
MAX_LEAGUE_WEEKS = 38
INITIAL_PLAYED_WEEKS = 4
CUP_WEEKS = {
    2: "Preliminary Round",
    4: "Round of 16",
    6: "Quarter-finals",
    8: "Semi-finals",
    10: "Final",
}


def ensure_league_seeded(db: Session) -> None:
    if db.scalar(select(SeasonState.id).limit(1)) is None:
        reset_league(db)


def reset_league(db: Session, seed: int | None = None) -> dict:
    chosen_seed = seed if seed is not None else random.randrange(1, 1_000_000)
    _wipe_all(db)

    teams = _seed_teams(db)
    _create_league_schedule(db, teams)
    db.add(
        SeasonState(
            id=1,
            season=LEAGUE_INFO["season"],
            current_week=0,
            random_seed=chosen_seed,
        )
    )
    db.commit()

    for _ in range(INITIAL_PLAYED_WEEKS):
        play_next_week(db)

    state = _get_state(db)
    return _season_summary(state)


def play_next_week(db: Session) -> dict:
    state = _get_state(db)
    if state.current_week >= MAX_LEAGUE_WEEKS:
        return {
            "advanced": False,
            "message": "Season is already complete.",
            **_season_summary(state),
        }

    next_week = state.current_week + 1
    _play_league_week(db, state, next_week)
    _create_and_play_cup_round_if_needed(db, state, next_week)

    state.current_week = next_week
    db.commit()

    return {
        "advanced": True,
        "week_played": next_week,
        **_season_summary(state),
    }


def get_dashboard_data(db: Session) -> dict:
    state = _get_state(db)
    standings = get_standings(db)
    return {
        "league": LEAGUE_INFO,
        "season": _season_summary(state),
        "leader": standings[0] if standings else None,
        "standings": standings,
        "top_scorers": get_top_scorers(db),
        "latest_results": get_results_by_week(db, state.current_week),
        "previous_results": get_previous_results(db, weeks=4),
        "next_week_matches": get_matches_by_week(db, state.current_week + 1),
        "cup_overview": get_cup_overview(db),
    }


def get_results_archive(db: Session) -> list[dict]:
    groups = defaultdict(list)
    matches = db.scalars(
        select(Match)
        .options(joinedload(Match.home_team), joinedload(Match.away_team))
        .where(Match.status == "finished")
        .order_by(Match.week_number.desc(), Match.competition.asc(), Match.id.asc())
    ).all()
    for match in matches:
        groups[match.week_number].append(_serialize_match(match))
    return [{"week": week, "matches": groups[week]} for week in sorted(groups.keys(), reverse=True)]


def get_calendar_view(db: Session) -> list[dict]:
    groups = defaultdict(list)
    matches = db.scalars(
        select(Match)
        .options(joinedload(Match.home_team), joinedload(Match.away_team))
        .order_by(Match.week_number.asc(), Match.competition.asc(), Match.id.asc())
    ).all()
    for match in matches:
        groups[match.week_number].append(_serialize_match(match))
    return [{"week": week, "matches": groups[week]} for week in sorted(groups.keys())]


def get_cup_overview(db: Session) -> dict:
    rounds = []
    champion = None
    for week, stage_name in CUP_WEEKS.items():
        matches = db.scalars(
            select(Match)
            .options(joinedload(Match.home_team), joinedload(Match.away_team))
            .where(Match.competition == "cup", Match.week_number == week)
            .order_by(Match.id.asc())
        ).all()
        serialized = [_serialize_match(match) for match in matches]
        rounds.append({"week": week, "stage_name": stage_name, "matches": serialized})
        if stage_name == "Final" and serialized and serialized[0]["status"] == "finished":
            champion = serialized[0]["winner"]
    return {"rounds": rounds, "champion": champion}


def get_matches_by_week(db: Session, week: int) -> list[dict]:
    if week < 1 or week > MAX_LEAGUE_WEEKS:
        return []
    matches = db.scalars(
        select(Match)
        .options(joinedload(Match.home_team), joinedload(Match.away_team))
        .where(Match.week_number == week)
        .order_by(Match.competition.asc(), Match.id.asc())
    ).all()
    return [_serialize_match(match) for match in matches]


def get_results_by_week(db: Session, week: int) -> list[dict]:
    matches = db.scalars(
        select(Match)
        .options(joinedload(Match.home_team), joinedload(Match.away_team))
        .where(Match.week_number == week, Match.status == "finished")
        .order_by(Match.competition.asc(), Match.id.asc())
    ).all()
    return [_serialize_match(match) for match in matches]


def get_previous_results(db: Session, weeks: int = 4) -> list[dict]:
    state = _get_state(db)
    start_week = max(1, state.current_week - weeks + 1)
    archive = []
    for week in range(state.current_week, start_week - 1, -1):
        matches = get_results_by_week(db, week)
        if matches:
            archive.append({"week": week, "matches": matches})
    return archive


def get_standings(db: Session) -> list[dict]:
    teams = db.scalars(select(Team).order_by(Team.name)).all()
    matches = db.scalars(
        select(Match)
        .options(joinedload(Match.home_team), joinedload(Match.away_team))
        .where(Match.competition == "league", Match.status == "finished")
        .order_by(Match.week_number.asc(), Match.id.asc())
    ).all()

    table = {
        team.id: {
            "team": team.name,
            "short_name": team.short_name,
            "played": 0,
            "wins": 0,
            "draws": 0,
            "losses": 0,
            "goals_for": 0,
            "goals_against": 0,
            "goal_difference": 0,
            "points": 0,
            "form": [],
        }
        for team in teams
    }

    for match in matches:
        home = table[match.home_team_id]
        away = table[match.away_team_id]
        home["played"] += 1
        away["played"] += 1
        home["goals_for"] += match.home_score
        home["goals_against"] += match.away_score
        away["goals_for"] += match.away_score
        away["goals_against"] += match.home_score

        if match.home_score > match.away_score:
            home["wins"] += 1
            home["points"] += 3
            away["losses"] += 1
            home["form"].append("W")
            away["form"].append("L")
        elif match.home_score < match.away_score:
            away["wins"] += 1
            away["points"] += 3
            home["losses"] += 1
            home["form"].append("L")
            away["form"].append("W")
        else:
            home["draws"] += 1
            away["draws"] += 1
            home["points"] += 1
            away["points"] += 1
            home["form"].append("D")
            away["form"].append("D")

    standings = []
    for item in table.values():
        item["goal_difference"] = item["goals_for"] - item["goals_against"]
        item["form"] = item["form"][-5:]
        standings.append(item)

    standings.sort(
        key=lambda entry: (entry["points"], entry["goal_difference"], entry["goals_for"], entry["team"]),
        reverse=True,
    )
    for index, item in enumerate(standings, start=1):
        item["position"] = index
    return standings


def get_top_scorers(db: Session, limit: int = 12) -> list[dict]:
    goals = db.scalars(
        select(GoalEvent)
        .options(joinedload(GoalEvent.team))
        .join(GoalEvent.match)
        .where(Match.competition == "league")
    ).all()
    scorers = {}
    for goal in goals:
        key = (goal.scorer_name, goal.team.short_name)
        if key not in scorers:
            scorers[key] = {"player": goal.scorer_name, "team": goal.team.short_name, "goals": 0}
        scorers[key]["goals"] += 1
    return sorted(scorers.values(), key=lambda item: (item["goals"], item["player"]), reverse=True)[:limit]


def _wipe_all(db: Session) -> None:
    db.query(GoalEvent).delete()
    db.query(Match).delete()
    db.query(SeasonState).delete()
    db.query(Team).delete()
    db.commit()


def _seed_teams(db: Session) -> list[Team]:
    teams = []
    for name, short_name, city, strength, stadium, _ in TEAM_DATA:
        team = Team(name=name, short_name=short_name, city=city, strength=strength, stadium=stadium)
        db.add(team)
        teams.append(team)
    db.commit()
    for team in teams:
        db.refresh(team)
    return teams


def _create_league_schedule(db: Session, teams: list[Team]) -> None:
    schedule = _build_round_robin(teams)
    season_start = date(2026, 8, 14)
    for week_number, games in enumerate(schedule, start=1):
        kickoff_date = season_start + timedelta(days=(week_number - 1) * 7)
        for home_team, away_team in games:
            db.add(
                Match(
                    competition="league",
                    week_number=week_number,
                    stage_name=f"Matchday {week_number}",
                    kickoff_date=kickoff_date,
                    status="scheduled",
                    home_team_id=home_team.id,
                    away_team_id=away_team.id,
                    home_score=0,
                    away_score=0,
                    notes="",
                )
            )
    db.commit()


def _build_round_robin(teams: list[Team]) -> list[list[tuple[Team, Team]]]:
    pool = teams[:]
    rounds = []
    half = len(pool) // 2
    for round_index in range(len(pool) - 1):
        pairings = []
        for idx in range(half):
            home = pool[idx]
            away = pool[-idx - 1]
            if round_index % 2 == 1:
                home, away = away, home
            pairings.append((home, away))
        rounds.append(pairings)
        pool = [pool[0], pool[-1], *pool[1:-1]]
    second_leg = [[(away, home) for home, away in matchday] for matchday in rounds]
    return rounds + second_leg


def _play_league_week(db: Session, state: SeasonState, week_number: int) -> None:
    matches = db.scalars(
        select(Match)
        .options(joinedload(Match.home_team), joinedload(Match.away_team))
        .where(Match.competition == "league", Match.week_number == week_number, Match.status == "scheduled")
        .order_by(Match.id.asc())
    ).all()
    scorers_lookup = {item[1]: item[5] for item in TEAM_DATA}
    for match in matches:
        _simulate_match(db, state.random_seed, week_number, match, scorers_lookup, knockout=False)


def _create_and_play_cup_round_if_needed(db: Session, state: SeasonState, week_number: int) -> None:
    stage_name = CUP_WEEKS.get(week_number)
    if not stage_name:
        return

    existing = db.scalars(
        select(Match)
        .where(Match.competition == "cup", Match.week_number == week_number)
        .limit(1)
    ).first()
    if existing is None:
        _create_cup_round(db, week_number, stage_name)

    matches = db.scalars(
        select(Match)
        .options(joinedload(Match.home_team), joinedload(Match.away_team))
        .where(Match.competition == "cup", Match.week_number == week_number, Match.status == "scheduled")
        .order_by(Match.id.asc())
    ).all()
    scorers_lookup = {item[1]: item[5] for item in TEAM_DATA}
    for match in matches:
        _simulate_match(db, state.random_seed + 5000, week_number, match, scorers_lookup, knockout=True)


def _create_cup_round(db: Session, week_number: int, stage_name: str) -> None:
    seeded_teams = db.scalars(select(Team).order_by(Team.strength.desc(), Team.name.asc())).all()
    participants = _cup_participants(db, stage_name, seeded_teams)
    if len(participants) < 2:
        return

    kickoff_date = date(2026, 8, 14) + timedelta(days=(week_number - 1) * 7 + 3)
    ordered = participants[:]
    pairings = []
    while len(ordered) >= 2:
        pairings.append((ordered.pop(0), ordered.pop(-1)))

    for home_team, away_team in pairings:
        db.add(
            Match(
                competition="cup",
                week_number=week_number,
                stage_name=stage_name,
                kickoff_date=kickoff_date,
                status="scheduled",
                home_team_id=home_team.id,
                away_team_id=away_team.id,
                home_score=0,
                away_score=0,
                notes="",
            )
        )
    db.commit()


def _cup_participants(db: Session, stage_name: str, seeded_teams: list[Team]) -> list[Team]:
    if stage_name == "Preliminary Round":
        return seeded_teams[12:]
    if stage_name == "Round of 16":
        top_twelve = seeded_teams[:12]
        return top_twelve + _cup_winners(db, "Preliminary Round")
    if stage_name == "Quarter-finals":
        return _cup_winners(db, "Round of 16")
    if stage_name == "Semi-finals":
        return _cup_winners(db, "Quarter-finals")
    if stage_name == "Final":
        return _cup_winners(db, "Semi-finals")
    return []


def _cup_winners(db: Session, stage_name: str) -> list[Team]:
    matches = db.scalars(
        select(Match)
        .options(joinedload(Match.home_team), joinedload(Match.away_team))
        .where(Match.competition == "cup", Match.stage_name == stage_name, Match.status == "finished")
        .order_by(Match.id.asc())
    ).all()
    winners = []
    for match in matches:
        winners.append(match.home_team if match.home_score > match.away_score else match.away_team)
    return winners


def _simulate_match(
    db: Session,
    base_seed: int,
    week_number: int,
    match: Match,
    scorers_lookup: dict[str, list[str]],
    knockout: bool,
) -> None:
    rng = random.Random(base_seed + week_number * 100 + match.id)
    home_strength = match.home_team.strength + 4
    away_strength = match.away_team.strength
    home_score = _generate_goals(rng, home_strength, away_strength)
    away_score = _generate_goals(rng, away_strength, home_strength)
    notes = ""

    if knockout and home_score == away_score:
        if rng.random() < 0.5:
            home_score += 1
            notes = "Won after penalties"
        else:
            away_score += 1
            notes = "Won after penalties"

    match.home_score = home_score
    match.away_score = away_score
    match.status = "finished"
    match.notes = notes
    db.flush()
    _create_goal_events(db, rng, match, scorers_lookup)


def _generate_goals(rng: random.Random, attack_strength: int, defense_strength: int) -> int:
    chance = max(0.6, min(3.4, 1.1 + ((attack_strength - defense_strength) / 26)))
    roll = rng.random()
    if roll < 0.14 * (3.0 / chance):
        return 0
    if roll < 0.43:
        return 1
    if roll < 0.70:
        return 2
    if roll < 0.88:
        return 3
    if roll < 0.96:
        return 4
    return 5


def _create_goal_events(db: Session, rng: random.Random, match: Match, scorers_lookup: dict[str, list[str]]) -> None:
    total_goals = match.home_score + match.away_score
    if total_goals == 0:
        return
    remaining_home_goals = match.home_score
    remaining_away_goals = match.away_score
    minutes = sorted(rng.sample(range(3, 91), total_goals))
    for minute in minutes:
        if remaining_home_goals > 0 and (
            remaining_away_goals == 0 or rng.random() < remaining_home_goals / (remaining_home_goals + remaining_away_goals)
        ):
            scoring_team = match.home_team
            remaining_home_goals -= 1
        else:
            scoring_team = match.away_team
            remaining_away_goals -= 1
        db.add(
            GoalEvent(
                match_id=match.id,
                team_id=scoring_team.id,
                scorer_name=rng.choice(scorers_lookup[scoring_team.short_name]),
                minute=minute,
            )
        )


def _serialize_match(match: Match) -> dict:
    winner = None
    if match.status == "finished" and match.home_score != match.away_score:
        winner = match.home_team.name if match.home_score > match.away_score else match.away_team.name
    return {
        "id": match.id,
        "competition": match.competition,
        "week_number": match.week_number,
        "stage_name": match.stage_name,
        "kickoff_date": match.kickoff_date.isoformat(),
        "status": match.status,
        "home_team": match.home_team.name,
        "home_short_name": match.home_team.short_name,
        "away_team": match.away_team.name,
        "away_short_name": match.away_team.short_name,
        "home_score": match.home_score,
        "away_score": match.away_score,
        "notes": match.notes,
        "winner": winner,
    }


def _get_state(db: Session) -> SeasonState:
    return db.scalar(select(SeasonState).where(SeasonState.id == 1))


def _season_summary(state: SeasonState) -> dict:
    return {
        "current_week": state.current_week,
        "max_weeks": MAX_LEAGUE_WEEKS,
        "remaining_weeks": MAX_LEAGUE_WEEKS - state.current_week,
        "season": state.season,
    }

