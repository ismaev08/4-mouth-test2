from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
from django.views import generic



class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'library_li'
    paginate_by = 2

    def get_queryset(self):
        return models.BooksModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.BooksModel, id=id)
        context = {
            "book_id": book_id,
        }
        return render(request, template_name='book_detail.html', context=context)

def book_list_view(request):
    if request.method == "GET":
        #query запрос что мы хотим видеть на html странице
        book_list = models.BooksModel.objects.all().order_by('-id')
        context = {'book_list': book_list}
        return render(request, template_name='book.html', context=context)


def about_me(request):
    if request.method == "GET":
        return HttpResponse("Привет, я Машалло Алим и это мой проект 4-месяца")

def about_pets(request):
    if request.method == "GET":
        return HttpResponse("Кошка: черного цвета с красивыми глазами, очень игривая и постоянно голодная."
                            "Возраст: не знаю, примерно 3 месяца")

def system_time(request):
    if request.method == "GET":
        now_time = datetime.now().time()
        return HttpResponse(f"текущее время: {now_time}")

def library_details_view(request, id):
    if request.method == 'GET':
        library_id = get_object_or_404(models.BooksModel, id=id)
        context = {
            'library_id': library_id,
        }
        return render(request, template_name='book_detail.html', context=context)