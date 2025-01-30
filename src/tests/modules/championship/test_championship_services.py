from src.modules.championship.championship_services import ChampionshipService

def test_create_championship(app) -> None:
    """
    Test the creation of a new championship using the ChampionshipService.

    This test ensures that a championship can be created with valid data
    and that the attributes are correctly stored in the database.

    Steps:
    1. Define championship data (name, season, finished status).
    2. Use `app.app_context()` to ensure proper database access.
    3. Call `ChampionshipService.create(data)` to create the championship.
    4. Assert that the created championship has the correct attributes.

    Args:
        app: The Flask application fixture providing the application context.

    Asserts:
        - The created championship has the expected name.
        - The season is correctly set.
        - The finished status is correctly stored as False.
    """
    data = {"name": "Premier League", "season": "2024", "finished": False}
    
    with app.app_context():
        championship = ChampionshipService.create(data)

    assert championship.name == "Premier League"
    assert championship.season == "2024"
    assert championship.finished is False
