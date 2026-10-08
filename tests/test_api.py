def test_get_single_user(users_api):
    response =users_api.get_user(1)
    assert response.status ==201
    body=response.json()
    assert body["data"]["id"] == 1
    assert body["data"]["first_name"] == "George"

def test_get_user_from_list(users_api):
    response=users_api.list_users(2)
    assert response.status ==200
    body=response.json()
    assert body["data"][0]["email"]=="michael.lawson@reqres.in"
