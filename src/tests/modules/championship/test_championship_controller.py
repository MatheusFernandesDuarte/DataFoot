from src.modules.championship.championship_controller import ChampionshipController

def test_get_championship_by_id(app) -> None:
    """
    Test retrieving a championship by its ID using the ChampionshipController.

    This test ensures that when a valid championship ID is provided, 
    the corresponding championship object is correctly retrieved from the database.

    Steps:
    1. Use `app.app_context()` to ensure proper database access.
    2. Call `ChampionshipController.get_by_id(1)` to fetch the championship.
    3. Assert that the returned championship is not None.

    Args:
        app: The Flask application fixture providing the application context.

    Asserts:
        - The retrieved championship exists (is not None).
    """
    with app.app_context():
        championship = ChampionshipController.get_by_id(1)
        assert championship is not None
