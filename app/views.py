from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request) :
  name = request.GET.get('name','')
  age = request.GET.get('age',18)
  print (name,age)
  return HttpResponse('hello django')