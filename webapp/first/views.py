import datetime
import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    now = datetime.datetime.now()
    context = {
        'current_date': now
    }
    return render(request, 'first/index.html', context)


def select(request):
    context = {}
    return render(request, 'first/select.html', context)


def result(request):
    chosen = int(request.GET['number'])

    results = []
    if 1 <= chosen <= 45:
        results.append(chosen)

    box = [i for i in range(1, 45) if i != chosen]
    random.shuffle(box)

    while len(results) < 6:
        results.append(box.pop())

    context = {
        'numbers': results
    }
    return render(request, 'first/result.html', context)
