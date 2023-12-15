from django.urls import path
from . import views
from .views import create
app_name = 'blog'

urlpatterns = [
    path('create/' , views.create , name='create'),
    path('blog/create/', create, name='blog_create'),
    path('edit/<int:pk>/' , views.edit , name='edit'),
    path('<slug:slug>/' , views.detail , name='detail'),
]
