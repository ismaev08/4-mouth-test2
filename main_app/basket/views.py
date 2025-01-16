from django.shortcuts import render,redirect,get_object_or_404
from main_app.basket.models import BasketModel
from main_app.basket.forms import BasketForm



def create_basket_view(request):
    if request.method == 'POST':
        form = BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('BasketList')

    else:
        form = BasketForm()
    return render(request, 'basket/create_basket.html', context={'form': form})




def basket_list_view(request):
    if request.method == 'GET':
        basket_list = BasketModel.objects.all().order_by('-id')
        context = {'basket_list': basket_list}
        return render(request, template_name='basket/basket_list.html', context=context)



def basket_detail_view(request, id):
    if request.method == 'GET':
        basket_id = get_object_or_404(BasketModel, id=id)
        context = {'basket_id': basket_id}
        return render(request, template_name='basket/basket_detail.html', context=context)


def update_basket_view(request, id):
    basket_id = get_object_or_404(BasketModel, id=id)
    if request.method == 'POST':
        form = BasketForm(request.POST, instance=basket_id)
        if form.is_valid():
            form.save()
            return redirect('BasketList')

    else:
        form = BasketForm(instance=basket_id)
    return render(request, template_name='basket/update_basket.html',
                  context={'basket_id': basket_id, 'form': form})


def delete_basket_view(request, id):
    basket_id = get_object_or_404(BasketModel, id=id)
    basket_id.delete()
    return redirect('BasketList')

def list_of_orders_view(request):
    if request.method == 'GET':
        list_of_orders = BasketModel.objects.all().order_by('-id')
        context = {'list_of_orders': list_of_orders}
        return render(request, template_name='basket/List_of_orders.html', context=context)