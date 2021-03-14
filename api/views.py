from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated

from posts.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class OwnResourcePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ("DELETE", "PUT", "POST", "PATCH"):
            return request.user == obj.author
        return True


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [OwnResourcePermission, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [OwnResourcePermission, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
