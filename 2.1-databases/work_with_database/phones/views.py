from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', 'name')
    template = 'catalog.html'
    if sort == 'max_price':
        phones_obj = Phone.objects.all().order_by('-price')
    else:
        phones_obj = Phone.objects.all().order_by(f'{sort}')
    context = {"phones": phones_obj}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
