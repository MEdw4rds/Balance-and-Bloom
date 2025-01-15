from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post

    **Fields:**

    `body`: Text area where logged in users can write their comments
    """

    class Meta:
        model = Comment
        fields = ('rating', 'body',)
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)]),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'author',
            'excerpt',
            'featured_image',
            'status',
            'category',
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'featured_image': forms.ClearableFileInput(
                attrs={'class': 'form-control'}),
        }