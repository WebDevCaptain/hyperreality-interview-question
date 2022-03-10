from database.models.passenger import Passenger


def new_passenger():
    p = {
        "checked": True,
        "name": "Atishi",
        "type": "AC",
        "age": 42,
        "description": "Regular from DEL to PNJ",
        "aadhar_no": "1234567891011131",
    }

    passenger = Passenger(**p)
    passenger.save_to_db()

    return passenger


def test_delete_passenger_res_status(test_client):
    passenger = new_passenger()
    res = test_client.delete(f"/api/passenger/{passenger.id}")
    assert res.status_code == 200


def test_delete_passenger_res_content(test_client):
    passenger = new_passenger()
    res = test_client.delete(f"/api/passenger/{passenger.id}")
    expected_res = f"Passenger {passenger.id} deleted"
    assert res.data == bytes(expected_res, "utf-8")
