from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CommentForm
from .models import CommentsInBali


def bali(request):
    comments = CommentsInBali.objects.filter()
    form = CommentForm(request.POST)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            com = form.save(commit=False)
            com.name = "User"
            com.photo = "mountain/bali/static/images/user.png"
            com.save()

            return HttpResponseRedirect('/main/bali')
    else:
        form = CommentForm()
    context = {
        "form": form,
        "comments": comments
    }
    return render(request, "index1.html", context)
