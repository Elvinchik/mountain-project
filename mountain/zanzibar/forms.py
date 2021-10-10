from .models import CommentsInZanzibar
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = CommentsInZanzibar
        fields = ['body']