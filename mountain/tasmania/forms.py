from .models import CommentsInTasmania
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = CommentsInTasmania
        fields = ['body']