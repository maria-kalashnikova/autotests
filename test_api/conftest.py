"""
utf-8
Создан 31.03.2022

:author: maria.kalashnikova

Обучающий курс Python QA Engineer.
Домашняя работа №4. конфиг файл для тестов API
"""
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action='store',
        default="https://ya.ru",
        help="This is requests url"
    )

    parser.addoption(
        "--status_code",
        action='store',
        default=200,
        help="This is requests url"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def base_status_code(request):
    return request.config.getoption("--status_code")
