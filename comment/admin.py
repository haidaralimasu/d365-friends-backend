from django.contrib import admin
from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "comment",
    )
    list_display_links = (
        "id",
        "comment",
    )
    search_fields = ("comment",)
    list_per_page = 25


admin.site.register(Comment, CommentAdmin)
