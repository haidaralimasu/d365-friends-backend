from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from blog.models import BlogPost
from blog.serializers import BlogPostSerializer


class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by("-created_at")
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permission_classes = (permissions.AllowAny,)


class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by("-created_at")
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permission_classes = (permissions.AllowAny,)


class BlogPostFeaturedView(ListAPIView):
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = "slug"
    permission_classes = (permissions.AllowAny,)
