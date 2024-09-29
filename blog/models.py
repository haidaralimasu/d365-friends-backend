from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()

    thumbnail = models.ImageField(upload_to="photos/")
    excerpt = models.CharField(max_length=150)
    content = models.TextField()
    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while queryset:
            slug = original_slug + "-" + str(count)
            count += 1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
