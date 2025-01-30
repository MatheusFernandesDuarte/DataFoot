from src.repositories.db import db

class Ranking(db.Model):
    __tablename__="ranking"
    __bind_key__="ranking"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    championship_id = db.Column(db.Integer, db.ForeignKey("championships.id"), nullable=False)
    championship = db.relationship("Championship", back_populates="ranking")

    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)
    team = db.relationship("Team", back_populates="ranking")

    position = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    wins = db.Column(db.Integer, nullable=False)
    losses = db.Column(db.Integer, nullable=False)
    draws = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return (f"<Ranking(championship_id={self.championship_id}, team_id={self.team_id}, position={self.position}, "
                f"points={self.points}, wins={self.wins}, losses={self.losses}, draws={self.draws})>")
