from django.test import TestCase
import pytest
import requests


def test_app_is_available():
    response = requests.get("http://127.0.0.1:8000/")
    assert response.ok


def test_page_unavailable():
    response = requests.get("http://127.0.0.1:8000/")
    assert response.status_code == 404
