import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # <-- ეს აუცილებელია ძებნისთვის
from .models import Message, Movie

# --- დამხმარე ფუნქცია ლინკისთვის ---
def make_embed(url):
    if not url:
        return url
    pattern = r'(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})'
    match = re.search(pattern, url)
    if match:
        return f"https://www.youtube.com/embed/{match.group(1)}"
    return url

# --- რეგისტრაცია / შესვლა ---
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            return render(request, 'register.html', {'error': 'სახელი და პაროლი აუცილებელია!'})
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'ეს სახელი დაკავებულია!'})
        User.objects.create_user(username=username, password=password)
        return redirect('signin')
    return render(request, 'register.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('upload_movie_page')
            return redirect('home_page')
        else:
            return render(request, 'login.html', {'error': 'მომხმარებელი ვერ მოიძებნა!'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home_page')

# --- ფილმების მართვა (ირაკლის პანელი) ---
@staff_member_required
def upload_movie(request):
    if request.method == "POST":
        title = request.POST.get('movie_title')
        description = request.POST.get('movie_description', '')
        raw_video_url = request.POST.get('movie_file')

        if title and raw_video_url:
            clean_url = make_embed(raw_video_url)
            Movie.objects.create(title=title, description=description, video_url=clean_url)
            return redirect('upload_movie_page')

    # აი აქ დავაბრუნეთ მესიჯები, რომ არ დაიკარგოს!
    all_movies = Movie.objects.all().order_by('-id')
    all_messages = Message.objects.all().order_by('-id') 
    
    return render(request, 'iraklispanel.html', {
        'all_movies': all_movies,
        'messages_list': all_messages # HTML-ში გამოიყენე messages_list
    })

@staff_member_required
def delete_movie(request, movie_id):
    if request.method == "POST":
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
    return redirect('upload_movie_page')

# --- გვერდები ---

def home(request):
    return render(request, 'index.html')


def main(request):
    query = request.GET.get('q') # იჭერს ძებნას ნებისმიერი გვერდიდან
    
    if query:
        movies = Movie.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).order_by('-id')
    else:
        movies = Movie.objects.all().order_by('-id')
        
    return render(request, 'main.html', {'movies': movies})

# --- კონტაქტის გვერდი ---
def contact_view(request):
    if request.method == "POST":
        # ვიღებთ მონაცემებს HTML ფორმიდან (name ატრიბუტებით)
        phone = request.POST.get('phone')
        subject = request.POST.get('subject', 'თემა არ არის')
        message_content = request.POST.get('message_text')

        if phone and message_content:
            # ვინახავთ შეტყობინებას ბაზაში
            Message.objects.create(
                phone=phone, 
                subject=subject, 
                text=message_content
            )
            # გაგზავნის შემდეგ მომხმარებელს ისევ კონტაქტის გვერდს ვუჩვენებთ
            return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')