from django.forms import ModelForm
from mypost.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content']

