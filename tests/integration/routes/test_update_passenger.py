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


def test_update_passenger_res_status(test_client):
    passenger = new_passenger()
    updates = {"aadhar_no": "1234567891011131", "age": 150}

    res = test_client.put(f"/api/passenger/{passenger.id}", json=updates)

    assert res.status_code == 200


def test_get_passenger_res_content(test_client):
    passenger = new_passenger()
    updates = {"aadhar_no": "1234567891011131", "age": 1900}

    res = test_client.put(f"/api/passenger/{passenger.id}", json=updates)

    assert res.json["age"] == updates["age"]
