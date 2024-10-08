from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from blog.models import BlogPost


class BlogPostAdmin(SummernoteModelAdmin):
    exclude = ("slug",)
    list_display = ("id", "title", "created_at")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_per_page = 25
    summernote_fields = ("content",)


admin.site.register(BlogPost, BlogPostAdmin)
