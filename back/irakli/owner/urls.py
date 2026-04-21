from django.contrib import admin
from django.urls import path
from owner import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home_page'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup_view, name='signup_page'),
    path('main/', views.main, name='main_page'),
    path('contact/', views.contact_view, name='contact_page'), # ← ეს დაამატე კონტაქტისთვის
    
    # ირაკლის პანელის მისამართები
    path('owner/upload/', views.upload_movie, name='upload_movie_page'),
    path('owner/delete/<int:movie_id>/', views.delete_movie, name='delete_movie'), # ← ეს წაშლისთვის
]