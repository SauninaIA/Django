from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    sort_dict = {
        'name': 'name',
        'min_price': '-price',
        'max_price': 'price'}
    template = 'catalog.html'
    phones = Phone.objects.all()
    if sort:
        phones = phones.order_by(sort_dict[sort])
    context = {"phones": phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
