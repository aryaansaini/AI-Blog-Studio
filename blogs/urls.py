from django.urls import path
from .views import BlogCreateView, BlogListView, BlogDetailView

urlpatterns = [
    path("", BlogCreateView.as_view(), name="blog-create"),
    path("all/", BlogListView.as_view(), name="blog-list"),
    path("<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),
]