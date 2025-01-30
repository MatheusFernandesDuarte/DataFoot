from src.modules.models.associations import championship_team_association, player_team_season_association
from src.repositories.db import db

class Team(db.Model):
    __tablename__="teams"
    __bind_key__="teams"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    abbreviation = db.Column(db.String(10), nullable=True)

    championships = db.relationship("Championship", secondary=championship_team_association, back_populates="teams")
    players = db.relationship("Player", secondary=player_team_season_association, back_populates="teams")
    cards = db.relationship("Card", back_populates="team")
    ranking = db.relationship("Ranking", back_populates="team")
    home_games = db.relationship("Game", foreign_keys="[Game.home_team_id]", back_populates="home_team")
    away_games = db.relationship("Game", foreign_keys="[Game.away_team_id]", back_populates="away_team")

    def __repr__(self):
        return f"<Team(name='{self.name}', championships={len(self.championships or [])}, players={len(self.players or [])})>"
