from django.http import HttpResponse
from django.shortcuts import render
from db import getcont


def index(request):
      a = getcont()
      return render(request, 'polls/menu.html', {'data':a})
