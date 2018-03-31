from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=191, blank=False)
    post = models.TextField()
    user = models.ForeignKey(User, name='user_id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now())

    def __str__(self):
        return self.title


class Comment(models.Model):
    message = models.TextField()
    post = models.ForeignKey(Post, name='post_id', on_delete=models.CASCADE)
    user = models.ForeignKey(User, name='user_id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now())

    def __str__(self):
        return self.message


class Like(models.Model):
    comment = models.ForeignKey(Comment, 'comment_id')
    user = models.ForeignKey(User, name='user_id', on_delete=models.CASCADE)
