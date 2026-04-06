from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    short_name: Mapped[str] = mapped_column(String(8), unique=True)
    city: Mapped[str] = mapped_column(String(100))
    strength: Mapped[int] = mapped_column(Integer)
    stadium: Mapped[str] = mapped_column(String(120))


class Match(Base):
    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(primary_key=True)
    matchday: Mapped[int] = mapped_column(Integer, index=True)
    kickoff_date: Mapped[date] = mapped_column(Date, index=True)
    status: Mapped[str] = mapped_column(String(20), index=True)
    home_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    away_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    home_score: Mapped[int] = mapped_column(Integer, default=0)
    away_score: Mapped[int] = mapped_column(Integer, default=0)

    home_team: Mapped[Team] = relationship(foreign_keys=[home_team_id])
    away_team: Mapped[Team] = relationship(foreign_keys=[away_team_id])
    goals: Mapped[list["GoalEvent"]] = relationship(
        back_populates="match",
        cascade="all, delete-orphan",
    )


class GoalEvent(Base):
    __tablename__ = "goal_events"

    id: Mapped[int] = mapped_column(primary_key=True)
    match_id: Mapped[int] = mapped_column(ForeignKey("matches.id"))
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    scorer_name: Mapped[str] = mapped_column(String(120), index=True)
    minute: Mapped[int] = mapped_column(Integer)

    match: Mapped[Match] = relationship(back_populates="goals")
    team: Mapped[Team] = relationship()

