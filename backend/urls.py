from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "D365 Friends"
admin.site.site_title = "D365 Friends"
admin.site.index_title = "D365 Friends"

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("summernote/", include("django_summernote.urls")),
    path("api/v1/blog/", include("blog.urls")),
    path("api/v1/contact/", include("contact.urls")),
    path("api/v1/comment/", include("contact.urls")),
    path("api/v1/admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r"^.*", TemplateView.as_view(template_name="index.html"))]
