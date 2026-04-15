from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('signup/', views.signup_view, name='signup_page'),
    path('login/', views.signin, name='login_page'), # <--- აი ეს სჭირდება signup_view-ს
    path('admin-panel/', views.upload_movie, name='upload_movie_page'), # <--- აი ეს სჭირდება signin-ს
]