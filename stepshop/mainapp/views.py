from django.shortcuts import render

links_menu = [
    {'link': 'index', 'name': 'Home'},
    {'link': 'products:index', 'name': 'Products'},
    {'link': 'about', 'name': 'About Us'},
    {'link': 'contacts', 'name': 'Contacts'},
]


def render_page(request, title, template_name):
    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, template_name, context)


def index(request):
    return render_page(request, 'Главная', 'index.html')


def about(request):
    return render_page(request, 'О нас', 'about.html')


def contacts(request):
    return render_page(request, 'Контакты', 'contacts.html')


def products(request):
    return render_page(request, 'Продукты', 'products.html')


def product(request):
    return render_page(request, 'Продукт', 'product.html')

