from django.shortcuts import render
from second.models import Post


def list_view(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)
