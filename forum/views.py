from django.shortcuts import render
from .models import Forum

def forum_list(request):
    forums = Forum.objects.all()
    context = {
        'forums': forums,
    }
    return render(request, 'forum/list.html', context=context)
