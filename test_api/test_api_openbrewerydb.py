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


def test_get_list_breweries(base_url):
    resp = requests.get(f"{base_url}/breweries")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert len(resp.json()) != 0


@pytest.mark.parametrize("city", ["Alameda", "San Diego", "South Windsor"])
def test_sort_by_city(base_url, city):
    resp = requests.get(f"{base_url}/breweries", params={"by_city": city})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert len(resp.json()) != 0
    for item in resp.json():
        assert item["city"] == city


@pytest.mark.parametrize("name", ["Snow Belt Brew", "Cycler's Brewing", "Devout Brewing"])
def test_sort_by_name(base_url, name):
    resp = requests.get(f"{base_url}/breweries", params={"by_name": name})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert len(resp.json()) != 0
    for item in resp.json():
        assert item["name"] == name


@pytest.mark.parametrize("type", ["micro", "nano", "regional", "brewpub", "large", "planning",
                                  "bar", "contract", "closed"])
def test_sort_by_name_correct(base_url, type):
    resp = requests.get(f"{base_url}/breweries", params={"by_type": type})
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert len(resp.json()) != 0
    for item in resp.json():
        assert item["brewery_type"] == type


@pytest.mark.parametrize("type", ["some_inf", 33, "blablabla"])
def test_sort_by_name_correct(base_url, type):
    resp = requests.get(f"{base_url}/breweries", params={"by_type": type})
    assert resp.status_code == 400
    assert isinstance(resp.json(), dict)
    assert "errors" in resp.json()
