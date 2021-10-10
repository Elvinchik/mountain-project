from .models import CommentsInBoraBora
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = CommentsInBoraBora
        fields = ['body']