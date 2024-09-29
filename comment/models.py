from datetime import datetime
from blog.models import BlogPost
from django.db import models


class Comment(models.Model):
    user = models.CharField(max_length=50)
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.TextField()

    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.comment
