from .models import CommentsInMaldiv
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = CommentsInMaldiv
        fields = ['body']