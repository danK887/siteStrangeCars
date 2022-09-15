from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Контакты', 'url_name': 'contact'},

]

def index(request):
    posts = Cars.objects.all()
    cats = Categories.objects.all()
    return render(request, 'cars/index.html', {'menu': menu, 'posts': posts, 'cats': cats, 'cat_selected':0,})

def show_category(request, categor_id):
    posts = Cars.objects.filter(categor_id=categor_id)
    cats = Categories.objects.all()

    if len(posts)==0:
        raise Http404()
    return render(request, 'cars/index.html', {'menu': menu, 'posts': posts, 'cats': cats, 'cat_selected': categor_id, })


def about(request):
    return render(request, 'cars/about.html', {'menu': menu})

def login(request):
    return HttpResponse("<h1>Войти</h1>")

def contact(request):
    return render(request, 'cars/contact.html', {'menu': menu})

def show_post(request, post_id):
    post = get_object_or_404(Cars, pk = post_id)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.categor_id,
    }

    return render(request, 'cars/post.html', context=context)

