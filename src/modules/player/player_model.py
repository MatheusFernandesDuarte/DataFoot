from src.modules.models.associations import player_game_association, player_team_season_association
from src.repositories.db import db

class Player(db.Model):
    __tablename__="players"
    __bind_key__="players"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50), nullable=True)

    teams = db.relationship("Team", secondary=player_team_season_association, back_populates="players")

    games = db.relationship("Game", secondary=player_game_association, back_populates="players")

    cards = db.relationship("Card", back_populates="player")

    goals = db.relationship("Goal", back_populates="player")

    def __repr__(self):
        return f"<Player(name='{self.name}', position='{self.position}')>"
