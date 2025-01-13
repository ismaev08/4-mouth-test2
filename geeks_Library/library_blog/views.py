from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from . import models


def book_list(request):
    if request.method == "GET":
        book_list = models.Books.objects.all().order_by("-id")
        context = {'book_list': book_list}
        return render(request, template_name='book.html', context=context)



def index(request):
    return HttpResponse("<4>стрница<4>")


def about_me(request):
    return HttpResponse("<4> страница про нас <4>")


def system_time(request):
    if request.method == "GET":
        now_time = datetime.now().time()
        return HttpResponse(f"текущее время: {now_time}")




