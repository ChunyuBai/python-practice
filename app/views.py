from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
# def index(request,name,age) :
#   name = request.GET.get('name','')
#   age = request.GET.get('age',18)
#   print (name,age)
#   return HttpResponse('hello django')

class Message(View) :
  def get(self, request, name, age) :
    # print(dir(request))
    # name = request.GET.get('name','')
    # age = request.GET.get('age','18')
    return HttpResponse('My name is %s and I am %s old' %(name,age))