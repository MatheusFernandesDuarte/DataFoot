from src.modules.models.associations import championship_team_association
from src.repositories.db import db

class Championship(db.Model):
    __tablename__="championships"
    __bind_key__='championships'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    season = db.Column(db.String(20), nullable=False)
    finished = db.Column(db.Boolean, default=False)

    teams = db.relationship("Team", secondary=championship_team_association, back_populates="championships")
    ranking = db.relationship("Ranking", back_populates="championship")
    games = db.relationship("Game", back_populates="championship")

    def __repr__(self):
        return f"<Campeonato(nome={self.nome}, temporada={self.temporada}, finalizado={self.finalizado})>"