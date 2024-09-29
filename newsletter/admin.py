from django.contrib import admin
from newsletter.models import Newsletter


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
    )
    list_display_links = (
        "id",
        "email",
    )
    search_fields = (
        "id",
        "email",
    )
    list_per_page = 25


admin.site.register(Newsletter, NewsletterAdmin)
