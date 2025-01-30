from django.urls import path
from app.blog.views import BlogView

urlpatterns = [
    path("blog/", BlogView.as_view(), name='blog')
]
