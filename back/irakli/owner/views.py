from django.shortcuts import render, redirect
from django.http import HttpResponse

# 1. შესასვლელი გვერდი (ლოგინი)
def owner_login(request):
    if request.method == "POST":
        name = request.POST.get('username')
        password = request.POST.get('password')

        if name == "irakli" and password == "12345":
            # თუ დაემთხვა, გადავიყვანოთ ატვირთვის გვერდზე
            # 'upload_movie' არის URL-ის სახელი (name)
            return redirect('upload_movie_page') 
        else:
            return HttpResponse("წვდომა უარყოფილია!")
            
    return render(request, 'login.html')

# 2. ფილმის ატვირთვის გვერდი
def upload_movie(request):
    # აქ მერე დაწერ ფილმის შენახვის ლოგიკას
    return render(request, 'iraklispanel.html')

def home(request):
    return render(request, 'index.html')