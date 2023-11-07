from django.shortcuts import render

from mainapp.models import Product


def get_data(**kwargs):
    links_menu = [
        {'link': 'index', 'name': 'Home'},
        {'link': 'products:index', 'name': 'Products'},
        {'link': 'about', 'name': 'About Us'},
        {'link': 'contacts', 'name': 'Contacts'},
    ]
    context = {
        'links_menu': links_menu,
    }

    context.update(**kwargs)
    return context


def index(request):
    title = "Главная"
    prods = Product.objects.all()
    context = get_data(title=title, prods=prods)
    return render(request, 'index.html', context)


def about(request):
    title = "Информация"
    context = get_data(title=title)
    return render(request, 'about.html', context)


def contacts(request):
    title = "Контакты"
    context = get_data(title=title)
    return render(request, 'contacts.html', context)


def products(request, pk):
    title = "Продукт"
    prod = Product.objects.get(pk=pk)
    context = get_data(title=title, prod=prod)
    return render(request, 'products.html', context)


def product(request):
    title = "Каталог продуктов"
    prods = Product.objects.all()
    context = get_data(title=title, prods=prods)
    return render(request, 'product.html', context)