def test_get_championships(client) -> None:
    """
    Test retrieving the list of championships from the API.

    This test ensures that a GET request to the `/championship/` endpoint
    returns a successful response (HTTP 200).

    Steps:
    1. Use the test client to send a GET request to `/championship/`.
    2. Assert that the response status code is 200 (OK).

    Args:
        client: The test client fixture used to simulate HTTP requests.

    Asserts:
        - The response status code is 200, indicating a successful request.
    """
    response = client.get("/championship/")
    assert response.status_code == 200
