from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, template_name='index.html')


def indexForTest(request, id):
    return render(request, template_name='index.html')
