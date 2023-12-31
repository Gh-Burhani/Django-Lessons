from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def microsoftbing(request):
    template = loader.get_template('microsoftbing.html')
    return HttpResponse(template.render())

def chat(request):
    template = loader.get_template('chat.html')
    return HttpResponse(template.render())

def images(request):
    template = loader.get_template('images.html')
    return HttpResponse(template.render())

def videos(request):
    template = loader.get_template('videos.html')
    return HttpResponse(template.render())

def maps(request):
    template = loader.get_template('maps.html')
    return HttpResponse(template.render())

def news(request):
    template = loader.get_template('news.html')
    return HttpResponse(template.render())
