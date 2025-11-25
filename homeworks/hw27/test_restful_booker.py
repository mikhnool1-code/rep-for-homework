import requests


def test_get_token():
    base_url = "https://restful-booker.herokuapp.com"
    path_to_auth = "/auth"

    body = {"username": "admin", "password": "password123"}

    response = requests.post(base_url+path_to_auth, json=body)

    assert response.status_code == 200
    assert "token" in response.json()


def test_create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    path_to_all_bookings = "/booking"

    body = {
        "firstname": "Sally",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }

    create = requests.post(base_url+path_to_all_bookings, json=body)
    booking_id = create.json()["bookingid"]

    response = requests.get(f"{base_url}{path_to_all_bookings}/{booking_id}")
    assert response.json()["firstname"] == "Sally"


def test_get_all_bookings():
    base_url = "https://restful-booker.herokuapp.com"
    path_to_all_bookings = "/booking"

    response = requests.get(base_url+path_to_all_bookings)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert isinstance(data[0], dict)
        assert "bookingid" in data[0]


def test_full_update():
    base_url = "https://restful-booker.herokuapp.com"
    path_to_all_bookings = "/booking"

    old_body = {
        "firstname": "Sally",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }

    new_body = {
        "firstname": "Dexter",
        "lastname": "Morgan",
        "totalprice": 456,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-01"
        },
        "additionalneeds": "Plastic bags"
    }

    create = requests.post(base_url + path_to_all_bookings, json=old_body)
    booking_id = create.json()["bookingid"]

    token = requests.post(base_url + "/auth",
                          json={"username": "admin", "password": "password123"}
                          ).json()["token"]
    headers = {"Cookie": f"token={token}"}

    response = requests.put(f"{base_url}{path_to_all_bookings}/{booking_id}",
                            json=new_body, headers=headers)

    assert response.status_code == 200
    assert response.json()["firstname"] == "Dexter"


def test_partial_update():
    base_url = "https://restful-booker.herokuapp.com"
    path_to_all_bookings = "/booking"

    old_body = {
        "firstname": "Dexter",
        "lastname": "Morgan",
        "totalprice": 456,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-01"
        },
        "additionalneeds": "Plastic bags"
    }

    new_body = {
        "firstname": "Mary",
        "lastname": "Bloody"
    }
    create = requests.post(base_url + path_to_all_bookings, json=old_body)
    booking_id = create.json()["bookingid"]

    token = requests.post(base_url + "/auth",
                          json={"username": "admin", "password": "password123"}
                          ).json()["token"]
    headers = {"Cookie": f"token={token}"}

    response = requests.patch(f"{base_url}{path_to_all_bookings}/{booking_id}",
                              json=new_body,
                              headers=headers)

    assert response.status_code == 200
    assert response.json()["firstname"] == "Mary"


def test_delete_positive():
    base_url = "https://restful-booker.herokuapp.com"
    path_to_all_bookings = "/booking"

    body = {
        "firstname": "Mary",
        "lastname": "Bloody",
        "totalprice": 456,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-01"
        },
        "additionalneeds": "Plastic bags"
    }

    create = requests.post(base_url + path_to_all_bookings, json=body)
    booking_id = create.json()["bookingid"]

    token = requests.post(base_url + "/auth",
                          json={"username": "admin", "password": "password123"}
                          ).json()["token"]
    headers = {"Cookie": f"token={token}"}

    response = requests.patch(f"{base_url}{path_to_all_bookings}/{booking_id}",
                              json=body,
                              headers=headers)

    assert response.status_code == 200


def test_get_token_with_bad_credentials():
    base_url = "https://restful-booker.herokuapp.com"
    path_to_auth = "/auth"

    body = {"username": "incorrect", "password": "incorrect"}

    response = requests.post(base_url+path_to_auth, json=body)

    assert response.status_code == 200
    assert response.json().get("reason") == "Bad credentials"


def test_get_nonexisting_booking():
    base_url = "https://restful-booker.herokuapp.com"
    path_to_all_bookings = "/booking"

    response = requests.get(f"{base_url}{path_to_all_bookings}/{99999999}")
    assert response.status_code == 404


def test_delete_with_outdated_token():
    base_url = "https://restful-booker.herokuapp.com"
    path_to_all_bookings = "/booking"

    body = {
        "firstname": "Mary",
        "lastname": "Bloody",
        "totalprice": 456,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-01"
        },
        "additionalneeds": "Plastic bags"
    }

    create = requests.post(base_url + path_to_all_bookings, json=body)
    booking_id = create.json()["bookingid"]

    headers = {"Cookie": "token=outdated_data"}

    response = requests.delete(
        f"{base_url}{path_to_all_bookings}/{booking_id}",
        headers=headers
    )

    assert response.status_code == 403


def test_create_booking_without_body():
    base_url = "https://restful-booker.herokuapp.com"
    path_to_all_bookings = "/booking"

    response = requests.post(base_url + path_to_all_bookings)
    assert response.status_code == 500
