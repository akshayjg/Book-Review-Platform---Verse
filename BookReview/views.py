from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Book, Author, Genre
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout

def register(request):
    if request.method == 'POST':
        # Get form data from POST request
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate the data
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        
        # Optionally save additional information like name and phone in a profile model

        user.save()

        # Log the user in and redirect to home page
        login(request, user)
        messages.success(request, f'Account created successfully for {username}!')
        return redirect('home')

    return render(request, 'register.html')

def notifications(request):
    return render(request, 'notifications.html', {'messages': messages.get_messages(request)})
def notify_user(request, message, level=messages.INFO):
    messages.add_message(request, level, message)

@login_required
def home(request):
    currently_reading = ...  
    recommended_books = ... 
    return render(request, 'home.html', {
        'currently_reading': currently_reading,
        'recommended_books': recommended_books,
    })

def redirect_to_login(request):
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    
class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    
class GenreListView(ListView):
    model = Genre
    template_name = 'genre_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

def home(request):
    books = Book.objects.all()[:10]  #first 10 books 
    genres = Genre.objects.all()
    context = {
        'books': books,
        'genres': genres,
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')  
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def more(request):
    return render(request, 'more.html') 

def recommendations(request):
    context = {
        'recommendations': ['Book 1', 'Book 2', 'Book 3']  
    }
    return render(request, 'recommendations.html', context)

def new_releases(request):
    context = {
        'new_releases': ['New Book 1', 'New Book 2', 'New Book 3']  # Example data
    }
    return render(request, 'new_releases.html', context)

def explore(request):
    context = {
        'explore_items': ['Explore Item 1', 'Explore Item 2', 'Explore Item 3']  # Example data
    }
    return render(request, 'explore.html', context)

def awards(request):
    context = {
        'awards_list': ['Award 1', 'Award 2', 'Award 3']  # Example data
    }
    return render(request, 'awards.html', context)

