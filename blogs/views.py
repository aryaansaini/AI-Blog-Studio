from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Blog
from .serializers import BlogSerializer


class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by("-created_at")
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)