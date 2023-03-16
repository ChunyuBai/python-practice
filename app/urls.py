from django.urls import path
from .views import Message
urlpatterns = [
  #path('index',index)
  #path('index/<str:name>/<int:age>',index)
  path('<str:name>',Message.as_view())
]