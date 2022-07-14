import os

from dataclasses import dataclass, field
from datetime import date
from tinydb import TinyDB

os.makedirs(os.path.dirname('data/tournament.json'), exist_ok=True)
tournament_database = TinyDB('data/tournament.json')


@dataclass
class Tournament:
    name: str
    place: str
    time_control: str
    description: str
    rounds_number: int = 4
    date: str = date.today().strftime("%d/%m/%Y")
    rounds: list = field(default_factory=list)
    players: list = field(default_factory=list)
    round_index: int = 0
    match_index: int = 0

    def save(tournament):
        tournament_database.insert(tournament.__dict__)
