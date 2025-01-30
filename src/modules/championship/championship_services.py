from sqlalchemy.orm import Session
from typing import Any, List, Optional

from src.modules.championship.championship_model import Championship
from src.repositories.db import db

class ChampionshipService:
    """
    Service class for managing Championship-related database operations.
    """
    @staticmethod
    def get_all() -> List[Championship]:
        """
        Retrieves all championships from the database.

        Returns:
            List[Championship]: A list of all championship records.
        """
        return db.session.query(Championship).all()
    
    @staticmethod
    def get_by_id(id: int) -> Optional[Championship]:
        """
        Retrieves a championship by its ID.

        Args:
            championship_id (int): The ID of the championship.

        Returns:
            Optional[Championship]: The championship object if found, otherwise None.
        """
        return db.session.get(Championship, id)

    @staticmethod
    def create(data) -> Championship:
        """
        Creates a new championship record in the database.

        Args:
            data (dict): A dictionary containing championship attributes.

        Returns:
            Championship: The newly created championship object.
        """
        championship = Championship(**data)
        db.session.add(championship)
        db.session.commit()
        db.session.refresh(championship)
        return championship
    
    @staticmethod
    def update(id: int, data) -> Optional[Championship]:
        """
        Updates an existing championship record.

        Args:
            championship_id (int): The ID of the championship to update.
            data (dict): A dictionary containing the updated values.

        Returns:
            Optional[Championship]: The updated championship object if found, otherwise None.
        """
        championship = db.session.get(Championship, id)
        if not championship:
            return None
        for key, value in data.items():
            setattr(championship, key, value)
        db.session.commit()
        db.session.refresh(championship)
        return championship
    
    @staticmethod
    def delete(id: int) -> Optional[Championship]:
        """
        Deletes a championship record by its ID.

        Args:
            championship_id (int): The ID of the championship to delete.

        Returns:
            Optional[Championship]: The deleted championship object if found, otherwise None.
        """
        championship = db.session.get(Championship, id)
        if not championship:
            return None
        db.session.delete(championship)
        db.session.commit()
        return championship
