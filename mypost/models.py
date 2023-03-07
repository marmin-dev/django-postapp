from django.db import models
from datetime import datetime

class User(models.Model):
    user_name = models.CharField(max_length=20,null=False)
    create_date = models.DateTimeField('date created')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100,null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    content = models.TextField(null=False)
    pub_date = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return self.title
