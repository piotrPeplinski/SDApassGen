from django.shortcuts import render
import random
import string


def gen_pass(length, capital_letter=False, numbers=False, special_characters=False):
    characters = string.ascii_lowercase

    if capital_letter:
        characters += string.ascii_uppercase

    if numbers:
        characters += string.digits

    if special_characters:
        characters += string.punctuation

    password = ''
    for _ in range(length):
        password += random.choice(characters)

    return password


def home(request):
    return render(request, 'home.html')


def password(request):
    length = int(request.POST.get('length'))
    big = request.POST.get('big')
    numbers = request.POST.get('numbers')
    specials = request.POST.get('specials')

    gen_password = gen_pass(length, big, numbers, specials)
    return render(request, 'password.html', {'password': gen_password})
    
