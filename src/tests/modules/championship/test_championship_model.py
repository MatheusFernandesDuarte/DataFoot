from src.modules.championship.championship_model import Championship

def test_create_championship() -> None:
    """
    Test the creation of a Championship object.

    This test ensures that a Championship instance can be created with the expected
    attributes and that they are correctly assigned.

    Steps:
    1. Instantiate a Championship object with test data.
    2. Assert that the object’s attributes match the expected values.

    Asserts:
        - The championship's name is correctly assigned.
        - The season is correctly assigned.
        - The finished status is correctly assigned as False.
    """
    championship = Championship(name="Brasileirão", season="2024", finished=False)
    assert championship.name == "Brasileirão"
    assert championship.season == "2024"
    assert championship.finished is False
