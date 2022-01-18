from django.test import Client


class TestPosts:
    def test_post_search_view(self):
        client = Client()

        response = client.get("/search_title/<str:post>/")
        assert response.status_code == 200

        response = client.get("/search_title/<str:post>/?title")
        assert response.status_code == 200

        response = client.post("/search_title/<str:post>/", data={"title": ""})
        assert response.status_code == 200
