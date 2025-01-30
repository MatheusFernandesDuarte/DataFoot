from src.repositories.db import db

class Card(db.Model):
    __tablename__="cards"
    __bind_key__="cards"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    game_id = db.Column(db.Integer, db.ForeignKey("games.id"), nullable=False)
    game = db.relationship("Game", back_populates="cards")

    player_id = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    player = db.relationship("Player", back_populates="cards")

    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    team = db.relationship("Team", back_populates="cards")

    minute = db.Column(db.Integer, nullable=False)
    card_type = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"<Card(game_id={self.game_id}, player_id={self.player_id}, team_id={self.team_id}, type={self.card_type}, minute={self.minute})>"
