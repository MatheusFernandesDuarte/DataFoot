from src.repositories.db import db

class GameStats(db.Model):
    __tablename__="game_stats"
    __bind_key__="game_stats"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    # 1-1 Game
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"), nullable=False, unique=True)
    game = db.relationship("Game", back_populates="stats")

    home_goals = db.Column(db.Integer, nullable=False, default=0)
    away_goals = db.Column(db.Integer, nullable=False, default=0)

    home_possession = db.Column(db.Float, nullable=False)
    away_possession = db.Column(db.Float, nullable=False)
    home_shots = db.Column(db.Integer, nullable=False)
    away_shots = db.Column(db.Integer, nullable=False)
    home_shots_on_target = db.Column(db.Integer, nullable=False)
    away_shots_on_target = db.Column(db.Integer, nullable=False)
    home_passes = db.Column(db.Integer, nullable=False)
    away_passes = db.Column(db.Integer, nullable=False)    
    home_corners = db.Column(db.Integer, nullable=False)
    away_corners = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return (f"<GameStats(game_id={self.game_id}, home_possession={self.home_possession}, "
                f"away_possession={self.away_possession}, home_shots={self.home_shots}, "
                f"away_shots={self.away_shots})>")