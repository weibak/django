import pytest

from django.contrib.auth.models import User

from django.test import Client

from profiles.models import Profile


@pytest.mark.django_db
class TestProfilesApi:
    def test_profiles_index_view(self):
        client = Client()

        user = User.objects.create(username="test", email="test@test.com", password="test")
        Profile.objects.create(user=user, age=25, status="test")

        client.force_login(user)

        response = client.get("/api/profiles/")
        assert response.status_code == 200
        assert response.data[0]["status"] == "test"

        response = client.post("/api/profiles/", data={"age": 25, "status": "test"})
        assert response.status_code == 201
