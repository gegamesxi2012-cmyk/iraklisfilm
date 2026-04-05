from django.urls import path
from . import views

urlpatterns = [
    path('owner-login/', views.owner_login, name='owner_login_page'),
    path('upload-movie/', views.upload_movie, name='upload_movie_page'),
    path('', views.home, name='home_page'),
    
]