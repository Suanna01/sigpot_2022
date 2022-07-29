from django.db import models
from django.contrib.auth.models import User

# 게시판
class FreePost(models.Model):
    # title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(null=True,default='')
    time = models.TextField(null=True,default='')
    food = models.TextField(null=True,default='')
    def __str__(self):
        return self.body

class Comment(models.Model):
    comment = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(FreePost, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
