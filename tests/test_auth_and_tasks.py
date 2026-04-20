def register_and_login(client):
    register_response = client.post(
        "/register",
        json={"email": "user@example.com", "password": "password123"},
    )
    assert register_response.status_code == 201

    login_response = client.post(
        "/login",
        json={"email": "user@example.com", "password": "password123"},
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_register_and_login(client):
    headers = register_and_login(client)
    assert headers["Authorization"].startswith("Bearer ")


def test_task_crud_flow(client):
    headers = register_and_login(client)

    create_response = client.post(
        "/tasks",
        json={"title": "Write tests", "description": "Cover main flows"},
        headers=headers,
    )
    assert create_response.status_code == 201
    task_id = create_response.json()["id"]

    list_response = client.get("/tasks", headers=headers)
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1

    update_response = client.put(
        f"/tasks/{task_id}",
        json={"completed": True},
        headers=headers,
    )
    assert update_response.status_code == 200
    assert update_response.json()["completed"] is True

    filtered_response = client.get("/tasks?completed=true", headers=headers)
    assert filtered_response.status_code == 200
    assert len(filtered_response.json()) == 1

    delete_response = client.delete(f"/tasks/{task_id}", headers=headers)
    assert delete_response.status_code == 204


def test_users_cannot_access_other_users_tasks(client):
    first_user_headers = register_and_login(client)
    task_response = client.post(
        "/tasks",
        json={"title": "Private task"},
        headers=first_user_headers,
    )
    task_id = task_response.json()["id"]

    client.post(
        "/register",
        json={"email": "other@example.com", "password": "password123"},
    )
    second_login = client.post(
        "/login",
        json={"email": "other@example.com", "password": "password123"},
    )
    second_headers = {"Authorization": f"Bearer {second_login.json()['access_token']}"}

    get_response = client.get(f"/tasks/{task_id}", headers=second_headers)
    assert get_response.status_code == 404
