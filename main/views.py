from django.shortcuts import render

def index(request):
    return render(request, 'main/base.html', {})

def tip(request):
    return render(request, 'main/tip.html', {})

def display(request):
    return render(request, 'main/display.html', {})