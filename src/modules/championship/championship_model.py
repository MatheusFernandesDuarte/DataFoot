from typing import Any

#from src.modules.models.associations import championship_team_association
from src.repositories.db import db

class Championship(db.Model):
    """
    Represents a championship entity in the database.

    This model stores information about different championships, 
    including their name, season, and whether they are finished.

    Attributes:
        id (int): The unique identifier for the championship.
        name (str): The name of the championship.
        season (str): The season associated with the championship.
        finished (bool): A flag indicating whether the championship has ended.
    
    Relationships (Commented Out for Now):
        - `teams`: Many-to-Many relationship with `Team`.
        - `ranking`: One-to-Many relationship with `Ranking`.
        - `games`: One-to-Many relationship with `Game`.
    
    These relationships are currently **commented out** because the related models 
    have not been created yet. Uncomment them once the models exist to avoid errors.
    """
    
    __tablename__="championships"
    __bind_key__='championships'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    season = db.Column(db.String(20), nullable=False)
    finished = db.Column(db.Boolean, default=False)

    ''' 
    # Relationships (Commented Out Until Models Are Created)
    teams = db.relationship("Team", secondary=championship_team_association, back_populates="championships")
    ranking = db.relationship("Ranking", back_populates="championship")
    games = db.relationship("Game", back_populates="championship")
    '''

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the Championship object into a dictionary.

        Returns:
            dict[str, Any]: A dictionary representation of the championship object.
        """
        return {
            "id": self.id,
            "name": self.name,
            "season": self.season,
            "finished": self.finished,
            #"teams": self.teams,
            #"ranking": self.ranking,
            #"games": self.games,
        }

    def __repr__(self) -> str:
        """
        Return a string representation of the Championship object.

        Returns:
            str: A formatted string representing the championship.
        """
        return f"<Championship(name={self.name}, season={self.season}, finished={self.finished})>"