from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=20,null=False)
    content = models.TextField(null=False)
    pub_date = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return self.title
