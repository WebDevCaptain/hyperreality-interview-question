def test_create_passenger_res_status(test_client):
    res = test_client.post(
        "/api/passengers",
        json={
            "checked": True,
            "name": "Atishi",
            "type": "AC",
            "age": 42,
            "description": "Regular from DEL to PNJ",
            "aadhar_no": "1234567891011171",
        },
    )
    assert res.status_code == 201


def test_create_passenger_res_status(test_client):
    p = {
        "checked": True,
        "name": "Atishi",
        "type": "AC",
        "age": 42,
        "description": "Regular from DEL to PNJ",
        "aadhar_no": "1234567891011171",
    }

    res = test_client.post(
        "/api/passengers",
        json=p,
    )

    assert res.json["aadhar_no"] == p["aadhar_no"]
