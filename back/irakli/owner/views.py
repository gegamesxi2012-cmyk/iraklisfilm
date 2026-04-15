from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.admin.views.decorators import staff_member_required
from .models import Message, Movie

# --- რეგისტრაცია ---
def signup_view(request):
    if request.method == "POST":
        saxeli = request.POST.get('first_name')
        paroli = request.POST.get('password')
        
        if User.objects.filter(username=saxeli).exists():
            return render(request, 'register.html', {'error': 'ეს სახელი დაკავებულია!'})
        
        User.objects.create_user(username=saxeli, password=paroli)
        return redirect('login_page') # ჯობია ლოგინზე გადააგდო
    
    return render(request, 'register.html')

# --- შესვლა (Login) ---
def signin(request):
    if request.method == "POST":
        name = request.POST.get('first_name') 
        password = request.POST.get('password')
        
        user = authenticate(request, username=name, password=password)
        
        if user is not None:
            login(request, user)
            # თუ ადმინია ან ირაკლია, პანელზე გადავიდეს
            if user.is_staff or user.username == "irakli":
                return redirect('upload_movie_page')
            return redirect('home_page')
        else:
            return render(request, 'login.html', {'error': 'არასწორი სახელი ან პაროლი!'})
            
    return render(request, 'login.html')

# --- ადმინ პანელი (მესიჯები + ფილმის ატვირთვა) ---

@staff_member_required
def upload_movie(request):
    if request.method == "POST":
        # HTML-ში name="movie_title" გიწერია
        title = request.POST.get('movie_title') 
        # HTML-ში name="movie_file" გიწერია
        video_url = request.POST.get('movie_file')
        
        if title and video_url:
            Movie.objects.create(title=title, video_url=video_url)
            return redirect('upload_movie_page')

    # შეტყობინებების გამოსაჩენად (HTML-ში გიწერია messages_list)
    all_messages = Message.objects.all().order_by('-created_at')
    return render(request, 'iraklispanel.html', {'messages_list': all_messages})

# --- მთავარი გვერდი ---
def home(request):
    movies = Movie.objects.all() # ფილმებიც წამოვიღოთ, რომ გამოვაჩინოთ
    return render(request, 'index.html', {'movies': movies})