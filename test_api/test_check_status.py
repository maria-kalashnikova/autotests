"""
utf-8
Создан 31.03.2022

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №4. Тесты статуса запроса

Для работы тестов необходимо на вход передать адресс сайта и ожидаемый код ответа
--url=<адрес сайта>
--status_code=<ожидаемый статус>
"""
import pytest
import requests


def test_status_resp(base_url, base_status_code):
    resp = requests.get(base_url)
    assert resp.status_code == base_status_code
