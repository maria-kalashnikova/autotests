"""
utf-8
Создан 31.03.2022

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №4. Тесты сайта

Для работы тестов необходимо на вход передать адресс сайта
--url=<адрес сайта>
"""
import pytest
import requests


def test_get_messages(base_url):
    resp = requests.get(f"{base_url}/posts")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert len(resp.json()) != 0


@pytest.mark.parametrize("id", [1, 20, 33, 100])
def test_get_post_by_id_correct(base_url, id):
    resp = requests.get(f"{base_url}/posts/{id}")
    assert resp.status_code == 200
    assert isinstance(resp.json(), dict)
    assert "userId" in resp.json()
    assert "id" in resp.json()
    assert "title" in resp.json()
    assert "body" in resp.json()
    assert resp.json()["id"] == id


@pytest.mark.parametrize("id", [0, 110, -3])
def test_get_post_by_id_incorrect(base_url, id):
    resp = requests.get(f"{base_url}/posts/{id}")
    assert resp.status_code == 404
    assert isinstance(resp.json(), dict)


def test_get_users(base_url):
    resp = requests.get(f"{base_url}/users")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert len(resp.json()) != 0


@pytest.mark.parametrize("id", [1, 20, 33, 100])
def test_get_user_by_id_correct(base_url, id):
    resp = requests.get(f"{base_url}/posts/{id}")
    assert resp.status_code == 200
    assert isinstance(resp.json(), dict)
    assert "id" in resp.json()
    assert resp.json()["id"] == id


@pytest.mark.parametrize("id", [0, 15, -3])
def test_get_user_by_id_incorrect(base_url, id):
    resp = requests.get(f"{base_url}/users/{id}")
    assert resp.status_code == 404
    assert isinstance(resp.json(), dict)
