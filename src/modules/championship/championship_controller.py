from flask import jsonify, request
from flask.wrappers import Response
from typing import Literal

from src.modules.championship.championship_services import ChampionshipService

class ChampionshipController:
    """
    Controller for handling Championship-related HTTP requests.

    Provides methods for retrieving, creating, updating, and deleting 
    championships via Flask API endpoints.
    """

    @staticmethod
    def get_all() -> tuple[Response, Literal[200]]:
        """
        Retrieve all championships.

        This method fetches all championships from the database and returns 
        them as a JSON response.

        Returns:
            tuple[Response, Literal[200]]: A JSON response containing the list of championships 
            and the HTTP status code 200.
        """
        precatorios = ChampionshipService.get_all()
        return jsonify([precatorio.to_dict() for precatorio in precatorios]), 200

    @staticmethod
    def get_by_id(id) -> tuple[Response, Literal[404]] | tuple[Response, Literal[200]]:
        """
        Retrieve a championship by its ID.

        Args:
            id (int): The ID of the championship to retrieve.

        Returns:
            tuple[Response, Literal[200]]: If the championship is found, returns a JSON response 
            containing the championship data and HTTP status code 200.
            tuple[Response, Literal[404]]: If the championship is not found, returns an error 
            message with HTTP status code 404.
        """
        precatorio = ChampionshipService.get_by_id(id)
        if not precatorio:
            return jsonify({"error": "Championship not found"}), 404
        return jsonify(precatorio.to_dict()), 200

    @staticmethod
    def create() -> tuple[Response, Literal[201]]:
        """
        Create a new championship.

        This method retrieves JSON data from the request, creates a new 
        championship in the database, and returns the newly created object.

        Returns:
            tuple[Response, Literal[201]]: A JSON response containing the created championship 
            and HTTP status code 201.
        """
        data = request.get_json()
        precatorio = ChampionshipService.create(data)
        return jsonify(precatorio.to_dict()), 201

    @staticmethod
    def update(id) -> tuple[Response, Literal[404]] | tuple[Response, Literal[200]]:
        """
        Update an existing championship.

        Args:
            id (int): The ID of the championship to update.

        Returns:
            tuple[Response, Literal[200]]: If the championship is successfully updated, 
            returns a JSON response containing the updated championship data and HTTP status code 200.
            tuple[Response, Literal[404]]: If the championship is not found, returns an error 
            message with HTTP status code 404.
        """
        data = request.get_json()
        precatorio = ChampionshipService.update(id, data)
        if not precatorio:
            return jsonify({"error": "Championship not found"}), 404
        return jsonify(precatorio.to_dict()), 200

    @staticmethod
    def delete(id) -> tuple[Response, Literal[404]] | tuple[Response, Literal[200]]:
        """
        Delete a championship by its ID.

        Args:
            id (int): The ID of the championship to delete.

        Returns:
            tuple[Response, Literal[200]]: If the championship is successfully deleted, 
            returns a confirmation message and HTTP status code 200.
            tuple[Response, Literal[404]]: If the championship is not found, returns an error 
            message with HTTP status code 404.
        """
        precatorio = ChampionshipService.delete(id)
        if not precatorio:
            return jsonify({"error": "Championship not found"}), 404
        return jsonify({"message": "Championship deleted with success"}), 200
