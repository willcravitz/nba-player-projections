from typing import Optional
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

class Player(SQLModel, table=True):
    person_id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    player_slug: str
    birthdate: Optional[datetime]
    school: str
    country: str
    height: int
    weight: int
    jersey: int
    position: str
    roster_status: str
    team_id: int = Field(foreign_key="team.id")
    draft_year: Optional[int]
    draft_round: Optional[int]
    draft_number: Optional[int]