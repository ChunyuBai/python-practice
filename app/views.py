from django.shortcuts import render
from django.views.generic import View
# Create your views here.
# def index(request,name,age) :
#   name = request.GET.get('name','')
#   age = request.GET.get('age',18)
#   print (name,age)
#   return HttpResponse('hello django')

class Message(View) :
  def get(self, request, name) :
    return render(request,'index.html',{'name':name})