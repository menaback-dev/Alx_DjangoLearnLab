from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django import forms
from .models import Comment
from .models import Tag




class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Comma-separated tags")

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
    


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

def save(self, commit=True, author=None):
    post = super().save(commit=False)

    if author:
        post.author = author

    if commit:
        post.save()

    tag_names = self.cleaned_data.get("tags", "")
    tag_list = [t.strip().lower() for t in tag_names.split(",") if t.strip()]

    tags = []
    for name in tag_list:
        tag, _ = Tag.objects.get_or_create(name=name)
        tags.append(tag)

    post.tags.set(tags)

    return post
