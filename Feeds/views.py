# Create your views here.
from django.shortcuts import render


def hello(request):
    context = {}
    context['param_display'] = "it's me"
    return render(request, 'hello.html', context)
