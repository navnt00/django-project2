from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('create/' , views.create , name='create'),
    path('edit/<int:pk>/' , views.edit , name='edit'),
    path('<slug:slug>/' , views.detail , name='detail'),
]
