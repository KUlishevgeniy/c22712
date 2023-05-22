from django.http import HttpResponse
from django.shortcuts import render
from db_get import djselect


def index(request):
      a = djselect()
      return render(request, 'polls/Menu.html', {'data': a})