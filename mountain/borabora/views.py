from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CommentForm
from .models import CommentsInBoraBora


def borabora(request):
    comments = CommentsInBoraBora.objects.filter()
    form = CommentForm(request.POST)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            com = form.save(commit=False)
            com.name = "User"
            com.photo = "mountain/borabora/static/images/user.png"
            com.save()

            return HttpResponseRedirect('/main/borabora')
    else:
        form = CommentForm()
    context = {
        "form": form,
        "comments": comments
    }
    return render(request, "index2.html", context)

