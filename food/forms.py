from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post

    **Fields:**

    `body`: Text area where logged in users can write their comments
    """

    class Meta:
        model = Comment
        fields = ('body',)