from django.urls import path
from .views import BlogCreateView, BlogListView, BlogDetailView, CategoryListCreateView, GenerateBlogView
urlpatterns = [
    path("", BlogCreateView.as_view(), name="blog-create"),
    path("all/", BlogListView.as_view(), name="blog-list"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),

   
    path("categories/", CategoryListCreateView.as_view(), name="category-list-create"),
    path("generate/", GenerateBlogView.as_view(), name="generate-blog"),
]