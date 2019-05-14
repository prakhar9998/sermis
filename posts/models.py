from django.db import models
from django.contrib.auth.models import User
from threads.models import Thread

class Post(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(null=True)
    topic = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE,
        related_name='topics'
    )
    content = models.TextField()