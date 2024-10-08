from django.urls import path
from blog.views import BlogPostListView, BlogPostDetailView, BlogPostFeaturedView

urlpatterns = [
    path("", BlogPostListView.as_view()),
    path("featured", BlogPostFeaturedView.as_view()),
    path("<slug>", BlogPostDetailView.as_view()),
]
