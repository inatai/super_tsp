from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse("Hello, world. You're at the tsp index.")
    return render(request, 'tsp/index.html')
