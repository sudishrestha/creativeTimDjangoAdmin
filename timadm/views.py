from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from django.template import loader  
def index(request):    
    template = loader.get_template('dashboard.html') 
    context={}
    return HttpResponse(template.render(context, request)) 
def dashboard(request):    
    template = loader.get_template('dashboard.html') 
    context={}
    return HttpResponse(template.render(context, request)) 
def tables(request):    
    template = loader.get_template('tables.html') 
    context={}
    return HttpResponse(template.render(context, request)) 
def billing(request):    
    template = loader.get_template('billing.html') 
    context={}
    return HttpResponse(template.render(context, request)) 
def virtual_reality(request):    
    template = loader.get_template('virtual-reality.html') 
    context={}
    return HttpResponse(template.render(context, request)) 
def rtl(request):    
    template = loader.get_template('rtl.html') 
    context={}
    return HttpResponse(template.render(context, request)) 
def notifications(request):    
    template = loader.get_template('notifications.html') 
    context={}
    return HttpResponse(template.render(context, request)) 
def profile(request):    
    template = loader.get_template('profile.html') 
    context={}
    return HttpResponse(template.render(context, request)) 
def sign_in(request):    
    template = loader.get_template('sign-in.html') 
    context={}
    return HttpResponse(template.render(context, request)) 
def sign_up(request):    
    template = loader.get_template('sign-up.html') 
    context={}
    return HttpResponse(template.render(context, request)) 