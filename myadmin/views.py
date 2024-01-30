from django.shortcuts import render


def index(request):
    return render(request, 'myadmin/index.html')

def login(request):
    return render(request, 'myadmin/login.html')
