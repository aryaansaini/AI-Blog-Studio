from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Blog
from .serializers import BlogSerializer
from .permissions import IsAuthorOrReadOnly

# Create Blog
class BlogCreateView(generics.CreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# List All Blogs
class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all().order_by("-created_at")
    serializer_class = BlogSerializer



class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]