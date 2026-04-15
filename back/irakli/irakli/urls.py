from django.contrib import admin
from django.urls import path
# აქ ჩამოწერე ის სახელები, რაც რეალურად გიწერია views.py-ში
from owner.views import signin, upload_movie, home, signup_view 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', signin, name='login_page'), # აქ ეწერა login_view და შევცვალე signin-ით
    path('owner/upload/', upload_movie, name='upload_movie_page'),
    path('signup/', signup_view, name='signup_page'), # ესეც დავამატოთ ბარემ
    path('', home, name='home_page'),
]