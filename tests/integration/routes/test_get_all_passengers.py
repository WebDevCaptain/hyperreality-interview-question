def test_get_all_passengers_res_status(test_client):
    res = test_client.get("/api/passengers")
    assert res.status_code == 200


def test_get_all_passengers_res_length(test_client):
    res = test_client.get("/api/passengers")
    assert len(res.json) > 0
