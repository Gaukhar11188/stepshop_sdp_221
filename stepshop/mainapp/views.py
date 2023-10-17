from django.shortcuts import render


def index(request):
    title = "главная"
    links_menu = [
        {'link': 'index', 'name': 'Главная'},
        {'link': 'about', 'name': 'О нас'},
        {'link': 'products:index', 'name': 'Продукты'},
        {'link': 'contacts', 'name': 'Контакты'},
    ]
    context = {'title': title,
               'links_menu': links_menu, }
    return render(request, 'index.html', context)


def about(request):
    title = "о нас"
    context = {'title': title}
    return render(request, 'about.html', context)


def contacts(request):
    title = "контакты"
    context = {'title': title}
    return render(request, 'contacts.html', context)


def product(request):
    title = "каталог продуктов"
    context = {'title': title}
    return render(request, 'product.html', context)


def products(request):
    title = "страница продукта"
    context = {'title': title}
    return render(request, 'products.html', context)

