from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CommentForm
from .models import CommentsInPhilipinnes


def philippines(request):
    comments = CommentsInPhilipinnes.objects.filter()
    form = CommentForm(request.POST)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            com = form.save(commit=False)
            com.name = "User"
            com.photo = "mountain/philippines/static/images/user.png"
            com.save()

            return HttpResponseRedirect('/main/philippines')
    else:
        form = CommentForm()
    context = {
        "form": form,
        "comments": comments
    }
    return render(request, "index4.html", context)