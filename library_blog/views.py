from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def about_me(request):
    if request.method == "GET":
        return HttpResponse("привет это мой 4 месяц учебы")

def about_pets(request):
    if request.method == "GET":
        return HttpResponse("Буря мглою небо кроет, Вихри снежные крутя; То,"
                            " как зверь, она завоет, То заплачет, как дитя")

def system_time(request):
    if request.method == "GET":
        now_time = datetime.now().time()
        return HttpResponse(f"текущее время: {now_time}")


