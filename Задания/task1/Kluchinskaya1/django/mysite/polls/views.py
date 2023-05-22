from django.http import HttpResponse
from django.shortcuts import render
import psycopg2
def execute_request(request):
    connection = psycopg2.connect(host='localhost', dbname='dbdata',
                              user='postgres', password='Q1w2e3r4')
    cursor = connection.cursor()
    cursor.execute(request)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def index(request):

    context = {
            "data": execute_request("select name, link from parsing")[:10]
    }
    for i in range(len(context["data"])):
        context["data"][i] = list(context["data"][i])
        context["data"][i][1] = f"polls/img/{i}.jpg"

    return HttpResponse(render(request, "polls/index.html", context))
