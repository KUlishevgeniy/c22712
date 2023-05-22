from django.http import HttpResponse
from django.shortcuts import render
from db_get_data import exec_query

def index(request):
    context = {
        "data": exec_query("select name, file, description, price from images")
    }

    for i in range(len(context["data"])):
        context["data"][i] = list(context["data"][i])
        context["data"][i][1] = "polls/images/" + context["data"][i][1].split("/")[-1]
        context["data"][i][-1] = context["data"][i][-1].split(":")[-1]

    return HttpResponse(render(request, "polls/index.html", context))

