from django.urls import path
from .views import BlogListCreateView

urlpatterns = [
    path("", BlogListCreateView.as_view(), name="blog-list"),
]