from django.shortcuts import render
from .models import Forum, Topic, Post

def forum_list(request):
    forums = Forum.objects.all()
    context = {
        'forums': forums,
    }
    return render(request, 'forum/list.html', context=context)
