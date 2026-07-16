from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_student_from_activity():
    response = client.delete("/activities/Chess Club/signup?email=michael@learn2earn.com")

    assert response.status_code == 200
    assert response.json()["message"] == "Removed michael@learn2earn.com from Chess Club"

    activities_response = client.get("/activities")
    chess_club = activities_response.json()["Chess Club"]
    assert "michael@learn2earn.com" not in chess_club["participants"]
