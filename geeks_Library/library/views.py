from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    return HttpResponse("<4>стрница<4>")


def about_me(request):
    return HttpResponse("<4> страница про нас <4>")


def system_time(request):
    if request.method == "GET":
        now_time = datetime.now().time()
        return HttpResponse(f"текущее время: {now_time}")



