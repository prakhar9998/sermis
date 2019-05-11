from django.db import models
from django.contrib.auth.models import User

class Forum(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    about = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=100)
    forum = models.ForeignKey(
        Forum,
        on_delete=models.CASCADE,
        related_name='topics'
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='topics'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_post_at = models.DateTimeField(null=True, blank=True)
    last_post_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(null=True)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='topics'
    )
    content = models.TextField()
