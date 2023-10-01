from django.shortcuts import render
from .utils import gen_pass


def home(request):
    return render(request, 'home.html')


def password(request):
    length = int(request.POST.get('length'))
    big = request.POST.get('big')
    numbers = request.POST.get('numbers')
    specials = request.POST.get('specials')

    gen_password = gen_pass(length, big, numbers, specials)
    return render(request, 'password.html', {'password': gen_password})


def about(request):
    return render(request, 'about.html')
