from __future__ import annotations

import random
from collections import defaultdict
from datetime import date, timedelta

from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload

from app.models import GoalEvent, Match, Team


TEAMS = [
    {
        "name": "Northbridge City",
        "short_name": "NBC",
        "city": "Northbridge",
        "strength": 85,
        "stadium": "Harbor Arena",
        "scorers": ["Ruben Moya", "Leo Duarte", "Pablo Serra", "Nico Prado"],
    },
    {
        "name": "Kingsport Athletic",
        "short_name": "KSA",
        "city": "Kingsport",
        "strength": 81,
        "stadium": "King's Ground",
        "scorers": ["Iker Solis", "Martin Vale", "Jorge Cano", "Elias Mendez"],
    },
    {
        "name": "Redhaven FC",
        "short_name": "RHF",
        "city": "Redhaven",
        "strength": 79,
        "stadium": "Forge Park",
        "scorers": ["Dani Paredes", "Samu Costa", "Mateo Linares", "Lucas Ferrer"],
    },
    {
        "name": "Bluecastle United",
        "short_name": "BCU",
        "city": "Bluecastle",
        "strength": 77,
        "stadium": "Castle View",
        "scorers": ["Adrian Vega", "Teo Marin", "Ivan Claret", "Mario Sanz"],
    },
    {
        "name": "Riverside Rovers",
        "short_name": "RSR",
        "city": "Riverside",
        "strength": 74,
        "stadium": "Riverside Park",
        "scorers": ["Gabi Pena", "Hugo Nieto", "Aitor Gil", "Rafa Otero"],
    },
    {
        "name": "Stonefield Town",
        "short_name": "SFT",
        "city": "Stonefield",
        "strength": 72,
        "stadium": "Granite Lane",
        "scorers": ["Raul Mena", "Alex Vives", "Bruno Sala", "Jose Roman"],
    },
    {
        "name": "Lakeside Albion",
        "short_name": "LSA",
        "city": "Lakeside",
        "strength": 70,
        "stadium": "Lakefront Stadium",
        "scorers": ["Unai Soto", "Pol Rubio", "David Miro", "Mikel Roca"],
    },
    {
        "name": "Ironvale CF",
        "short_name": "IVC",
        "city": "Ironvale",
        "strength": 68,
        "stadium": "Steelworks Field",
        "scorers": ["Nestor Rey", "Julen Pastor", "Sergio Cruz", "Jaime Vidal"],
    },
]

LEAGUE_INFO = {
    "name": "Data Engineering Premier League",
    "country": "Simulated Nation",
    "season": "2026",
}


def ensure_league_seeded(db: Session) -> None:
    if db.scalar(select(Team.id).limit(1)) is None:
        reset_league(db)


def reset_league(db: Session, seed: int | None = None) -> dict:
    rng = random.Random(seed if seed is not None else random.randrange(1, 1_000_000))

    db.query(GoalEvent).delete()
    db.query(Match).delete()
    db.query(Team).delete()
    db.commit()

    teams = []
    for team_data in TEAMS:
        team = Team(
            name=team_data["name"],
            short_name=team_data["short_name"],
            city=team_data["city"],
            strength=team_data["strength"],
            stadium=team_data["stadium"],
        )
        db.add(team)
        teams.append(team)

    db.commit()
    for team in teams:
        db.refresh(team)

    team_lookup = {team.id: team for team in teams}
    scorers_lookup = {team["short_name"]: team["scorers"] for team in TEAMS}

    fixtures = _build_round_robin(teams)
    season_start = date(2026, 8, 14)
    played_matchdays = len(fixtures) // 2 + 1

    for matchday, games in enumerate(fixtures, start=1):
        kickoff_date = season_start + timedelta(days=(matchday - 1) * 7)
        status = "finished" if matchday <= played_matchdays else "scheduled"

        for home_team, away_team in games:
            home_score = 0
            away_score = 0

            if status == "finished":
                home_score = _generate_goals(rng, home_team.strength + 5, away_team.strength)
                away_score = _generate_goals(rng, away_team.strength, home_team.strength + 3)

            match = Match(
                matchday=matchday,
                kickoff_date=kickoff_date,
                status=status,
                home_team_id=home_team.id,
                away_team_id=away_team.id,
                home_score=home_score,
                away_score=away_score,
            )
            db.add(match)
            db.flush()

            if status == "finished":
                _create_goal_events(db, rng, match, team_lookup, scorers_lookup)

    db.commit()

    return {
        "league": LEAGUE_INFO,
        "seeded": True,
        "teams": len(teams),
        "matchdays": len(fixtures),
        "played_matchdays": played_matchdays,
    }


def get_dashboard_data(db: Session) -> dict:
    standings = get_standings(db)
    scorers = get_top_scorers(db)
    recent_results = get_recent_results(db)
    upcoming_fixtures = get_upcoming_fixtures(db)
    return {
        "league": LEAGUE_INFO,
        "standings": standings,
        "top_scorers": scorers,
        "recent_results": recent_results,
        "upcoming_fixtures": upcoming_fixtures,
        "leader": standings[0] if standings else None,
    }


def get_standings(db: Session) -> list[dict]:
    teams = db.scalars(select(Team).order_by(Team.name)).all()
    finished_matches = db.scalars(
        select(Match)
        .options(joinedload(Match.home_team), joinedload(Match.away_team))
        .where(Match.status == "finished")
        .order_by(Match.matchday, Match.id)
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

    for match in finished_matches:
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
    for team_stats in table.values():
        team_stats["goal_difference"] = team_stats["goals_for"] - team_stats["goals_against"]
        team_stats["form"] = team_stats["form"][-5:]
        standings.append(team_stats)

    standings.sort(
        key=lambda item: (
            item["points"],
            item["goal_difference"],
            item["goals_for"],
            item["team"],
        ),
        reverse=True,
    )

    for index, item in enumerate(standings, start=1):
        item["position"] = index

    return standings


def get_top_scorers(db: Session, limit: int = 10) -> list[dict]:
    goals = db.scalars(
        select(GoalEvent)
        .options(joinedload(GoalEvent.team))
        .order_by(GoalEvent.minute)
    ).all()

    scorers: dict[tuple[str, str], dict] = {}
    for goal in goals:
        key = (goal.scorer_name, goal.team.short_name)
        if key not in scorers:
            scorers[key] = {
                "player": goal.scorer_name,
                "team": goal.team.short_name,
                "goals": 0,
            }
        scorers[key]["goals"] += 1

    leaderboard = sorted(
        scorers.values(),
        key=lambda item: (item["goals"], item["player"]),
        reverse=True,
    )
    return leaderboard[:limit]


def get_recent_results(db: Session, limit: int = 8) -> list[dict]:
    matches = db.scalars(
        select(Match)
        .options(joinedload(Match.home_team), joinedload(Match.away_team))
        .where(Match.status == "finished")
        .order_by(Match.kickoff_date.desc(), Match.id.desc())
        .limit(limit)
    ).all()
    return [_serialize_match(match) for match in matches]


def get_upcoming_fixtures(db: Session, limit: int = 8) -> list[dict]:
    matches = db.scalars(
        select(Match)
        .options(joinedload(Match.home_team), joinedload(Match.away_team))
        .where(Match.status == "scheduled")
        .order_by(Match.kickoff_date.asc(), Match.id.asc())
        .limit(limit)
    ).all()
    return [_serialize_match(match) for match in matches]


def get_matchday_groups(db: Session) -> list[dict]:
    matches = db.scalars(
        select(Match)
        .options(joinedload(Match.home_team), joinedload(Match.away_team))
        .order_by(Match.matchday.asc(), Match.id.asc())
    ).all()

    groups: dict[int, list[dict]] = defaultdict(list)
    for match in matches:
        groups[match.matchday].append(_serialize_match(match))

    return [
        {"matchday": matchday, "matches": grouped_matches}
        for matchday, grouped_matches in groups.items()
    ]


def _serialize_match(match: Match) -> dict:
    return {
        "id": match.id,
        "matchday": match.matchday,
        "kickoff_date": match.kickoff_date.isoformat(),
        "status": match.status,
        "home_team": match.home_team.name,
        "home_short_name": match.home_team.short_name,
        "away_team": match.away_team.name,
        "away_short_name": match.away_team.short_name,
        "home_score": match.home_score,
        "away_score": match.away_score,
    }


def _build_round_robin(teams: list[Team]) -> list[list[tuple[Team, Team]]]:
    pool = teams[:]
    if len(pool) % 2 != 0:
        raise ValueError("Round robin requires an even number of teams.")

    rounds = []
    total_rounds = len(pool) - 1
    half = len(pool) // 2

    for _ in range(total_rounds):
        pairings = []
        for idx in range(half):
            home = pool[idx]
            away = pool[-idx - 1]
            if idx == 0 and len(rounds) % 2 == 1:
                home, away = away, home
            pairings.append((home, away))
        rounds.append(pairings)
        pool = [pool[0], pool[-1], *pool[1:-1]]

    second_leg = [[(away, home) for home, away in matchday] for matchday in rounds]
    return rounds + second_leg


def _generate_goals(rng: random.Random, attack_strength: int, defense_strength: int) -> int:
    chance = max(0.5, min(3.2, 1.2 + ((attack_strength - defense_strength) / 28)))
    roll = rng.random()
    if roll < 0.18 * (3.0 / chance):
        return 0
    if roll < 0.45:
        return 1
    if roll < 0.72:
        return 2
    if roll < 0.9:
        return 3
    return 4 if rng.random() < 0.8 else 5


def _create_goal_events(
    db: Session,
    rng: random.Random,
    match: Match,
    team_lookup: dict[int, Team],
    scorers_lookup: dict[str, list[str]],
) -> None:
    remaining_home_goals = match.home_score
    remaining_away_goals = match.away_score
    total_goals = remaining_home_goals + remaining_away_goals

    for minute in sorted(rng.sample(range(4, 91), total_goals)):
        if remaining_home_goals > 0 and (
            remaining_away_goals == 0
            or rng.random() < remaining_home_goals / (remaining_home_goals + remaining_away_goals)
        ):
            scoring_team = team_lookup[match.home_team_id]
            remaining_home_goals -= 1
        else:
            scoring_team = team_lookup[match.away_team_id]
            remaining_away_goals -= 1

        scorer = rng.choice(scorers_lookup[scoring_team.short_name])
        db.add(
            GoalEvent(
                match_id=match.id,
                team_id=scoring_team.id,
                scorer_name=scorer,
                minute=minute,
            )
        )
