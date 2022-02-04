import pytest
from django.contrib.auth.models import User
from django.test import Client

from posts.models import Post


@pytest.mark.django_db
class TestPosts:
    def test_posts_view(self):
        client = Client()

        user = User.objects.create(username="test", email="test@test.com", password="testtest")
        Post.objects.create(author=user, title="Test", text="test", slug="test")

        client.force_login(user)

        response = client.get("/")
        assert response.status_code == 200

        response = client.get("/posts/all")
        assert response.status_code == 301
