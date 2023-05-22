from django.shortcuts import render
from django.http import HttpResponse
from db import getcont2

def index(request):
    return render(request, 'polls/index.html')
# Create your views here.
def html(request):
    return HttpResponse("Привет Мир")
def newpage(request):
    df = {
        "data": getcont2()
    }

    for i in range(len(df["data"])):
        df["data"][i] = list(df["data"][i])
        df["data"][i][-1] = "img/laptops/" + df["data"][i][-1].split("/")[-1]
    return render(request, 'electronics/shop.html', df)