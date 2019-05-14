from django.db import models
from forum.models import Forum
from django.contrib.auth.models import User

class Thread(models.Model):
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