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


def test_status_code_list_all(base_url):
    endpoint = f"{base_url}/api/breeds/list/all"
    resp = requests.get(endpoint)
    assert resp.status_code == 200
    assert isinstance(resp.json(), dict)
    assert "message" in resp.json(), "Key 'message' is missing"
    assert "status" in resp.json(), "Key 'status' is missing"
    assert type(resp.json()["message"]) is dict
    assert resp.json()["status"] == "success"


def test_status_code_image_random(base_url):
    endpoint = f"{base_url}/api/breeds/image/random"
    resp = requests.get(endpoint)
    assert resp.status_code == 200
    assert isinstance(resp.json(), dict)
    assert "message" in resp.json(), "Key 'message' is missing"
    assert "status" in resp.json(), "Key 'status' is missing"
    assert type(resp.json()["message"]) is str
    assert resp.json()["status"] == "success"

@pytest.mark.parametrize("breed_name", ["beagle", "corgi", "husky"])
def test_resp_keys_image_random_breed(base_url, breed_name):
    endpoint = f"{base_url}/api/breed/{breed_name}/images/random"
    resp = requests.get(endpoint)
    assert resp.status_code == 200


@pytest.mark.parametrize("breed_name", ["fjgifkd", 3456, None])
def test_resp_keys_image_random_breed(base_url, breed_name):
    endpoint = f"{base_url}/api/breed/{breed_name}/images/random"
    resp = requests.get(endpoint)
    assert resp.status_code == 404


def test_resp_hound_images(base_url):
    endpoint = f"{base_url}/api/breed/hound/images"
    resp = requests.get(endpoint)
    assert resp.status_code == 200
    assert isinstance(resp.json(), dict)
    assert "message" in resp.json(), "Key 'message' is missing"
    assert "status" in resp.json(), "Key 'status' is missing"
    assert type(resp.json()["message"]) is list
    assert len(resp.json()["message"]) != 0
    assert resp.json()["status"] == "success"
