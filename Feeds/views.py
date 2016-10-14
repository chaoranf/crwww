# Create your views here.
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'hello world123123123312'
    return render(request, 'hello.html', context)
