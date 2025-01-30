from src.modules.models.associations import player_game_association
from src.repositories.db import db

class Game(db.Model):
    __tablename__="games"
    __bind_key__="games"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    round = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    # 1-N championship
    championship_id = db.Column(db.Integer, db.ForeignKey("championships.id"), nullable=False)
    championship = db.relationship("Championship", back_populates="games")

    # Relationship w/ home and away team
    home_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    away_team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)

    home_team = db.relationship("Team", foreign_keys=[home_team_id], back_populates="home_games")
    away_team = db.relationship("Team", foreign_keys=[away_team_id], back_populates="away_games")

    # N-N players
    players = db.relationship("Player", secondary=player_game_association, back_populates="games")

    # 1-1 Stats
    stats = db.relationship("GameStats", uselist=False, back_populates="game")

    # 1-N Cards
    cards = db.relationship("Card", back_populates="game")

    # 1-N Goals
    goals = db.relationship("Goal", back_populates="game")

    __table_args__ = {"info": {"bind_key": "teams"}}

    def __repr__(self):
        return (f"<Game(id={self.id}, date={self.date}, championship_id={self.championship_id}, "
                f"home_team_id={self.home_team_id}, away_team_id={self.away_team_id})>")
