from django.urls import path
from .views import BlogCreateView, BlogListView

urlpatterns = [
    path("", BlogCreateView.as_view(), name="blog-create"),
    path("all/", BlogListView.as_view(), name="blog-list"),
]