from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('upload/', views.upload_file, name='upload_file'),
]
