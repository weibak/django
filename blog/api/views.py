from rest_framework import viewsets


from api.serializers import PostModelSerializer
from posts.models import Post
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed.
    """

    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostModelSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)