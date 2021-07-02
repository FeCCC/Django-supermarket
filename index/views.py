from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'title': '超市进销存管理系统'}
    return render(request, 'index.html', context)
