from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwner


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed(request):
    following_users = request.user.following.all()

    posts = Post.objects.filter(
        author__in=following_users
    ).order_by('-created_at')

    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)