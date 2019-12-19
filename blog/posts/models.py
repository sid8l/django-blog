from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_ordered_comments(self):
        return self.comment_set.order_by("-pub_date")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
