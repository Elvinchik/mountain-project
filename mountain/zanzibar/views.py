from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CommentForm
from .models import CommentsInZanzibar


def zanzibar(request):
    comments = CommentsInZanzibar.objects.filter()
    form = CommentForm(request.POST)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            com = form.save(commit=False)
            com.name = "User"
            com.photo = "mountain/zanzibar/static/images/user.png"
            com.save()

            return HttpResponseRedirect('/main/zanzibar')
    else:
        form = CommentForm()
    context = {
        "form": form,
        "comments": comments
    }
    text = "C:/Users/Admin/mountain-project/mountain/main/templates/mountain/zanzibar/templates/index.html"
    return render(request, "C:/Users/Admin/mountain-project/mountain/main/templates/mountain/zanzibar/templates/index.html", context)