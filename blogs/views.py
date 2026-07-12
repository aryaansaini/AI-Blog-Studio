from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response

from .services import generate_blog
from django.shortcuts import get_object_or_404




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

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "title",
        "content",
    ]

    ordering_fields = [
        "created_at",
        "title",
    ]

    filterset_fields = [
        "status",
        "category",
    ]



class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class GenerateBlogView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        topic = request.data.get("topic")
        category_id = request.data.get("category")
        category = None

        if category_id:
            category = get_object_or_404(Category, id=category_id)

        if not topic:
            return Response(
                {"error": "Topic is required"},
                status=400
            )

        generated_blog = generate_blog(topic)

        
        # AI response se title extract
        lines = generated_blog.splitlines()

        title = topic

        for line in lines:
            if line.strip().startswith("#"):
                title = line.replace("#", "").strip()
                break

        # Database save
        blog = Blog.objects.create(
            title=title,
            content=generated_blog,
            author=request.user,
            category=category,
            status="draft",
        )

        return Response({
            "message": "Blog generated successfully",
            "id": blog.id,
            "title": blog.title,
            "content": blog.content,
        })