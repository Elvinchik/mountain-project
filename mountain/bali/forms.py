from .models import CommentsInBali
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = CommentsInBali
        fields = ['body']