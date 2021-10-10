from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CommentForm
from .models import CommentsInTasmania


def tasmania(request):
    comments = CommentsInTasmania.objects.filter()
    form = CommentForm(request.POST)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            com = form.save(commit=False)
            com.name = "User"
            com.photo = "mountain/tasmania/static/images/user.png"
            com.save()

            return HttpResponseRedirect('/main/tasmania')
    else:
        form = CommentForm()
    context = {
        "form": form,
        "comments": comments
    }
    return render(request, "index5.html", context)