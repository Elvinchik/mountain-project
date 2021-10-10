from .models import CommentsInPhilipinnes
from django.forms import ModelForm


class CommentForm(ModelForm):
    class Meta:
        model = CommentsInPhilipinnes
        fields = ['body']