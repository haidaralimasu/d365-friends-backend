from django.urls import path
from comment.views import GetBlogCommentsView, GetBlogCommentView, CreateBlogCommentView

urlpatterns = [
    path("get-comments/<blogSlug>", GetBlogCommentsView.as_view()),
    path("get-comment/<blogSlug>", GetBlogCommentView.as_view()),
    path("create-comment/<blogSlug>", CreateBlogCommentView.as_view()),
]
