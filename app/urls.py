from django.urls import path
from .views import Message
urlpatterns = [
  #path('index',index)
  #path('index/<str:name>/<int:age>',index)
  path('message/<str:name>/<int:age>',Message.as_view())
]