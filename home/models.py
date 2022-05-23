from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length= 500)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)  # auto_now_add: for first time dating
    updated = models.DateTimeField(auto_now=True)      # auto_now: Each time it was saved

    def __str__(self):
        return f' {self.slug} - {self.updated}'
