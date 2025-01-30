from src.repositories.db import db

class Goal(db.Model):
    __tablename__="goals"
    __bind_key__="goals"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    game_id = db.Column(db.Integer, db.ForeignKey("games.id"), nullable=False)
    game = db.relationship("Game", back_populates="goals")

    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    player = db.relationship("Player", back_populates="goals")

    minute = db.Column(db.Integer, nullable=False)
    goal_type = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Goal(game_id={self.game_id}, player_id={self.player_id}, minute={self.minute}, goal_type='{self.goal_type}')>"
