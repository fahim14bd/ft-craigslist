from django.urls import path
from .views import search

app_name = 'my_app'
urlpatterns = [
  path('', search, name='search')
]