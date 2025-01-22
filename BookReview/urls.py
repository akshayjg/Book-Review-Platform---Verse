from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, BookListView, BookDetailView, register, about, add_book, profile, notifications, redirect_to_login, login_view
from . import views

urlpatterns = [
    path('', redirect_to_login, name='redirect-to-login'),
    path('home/', home, name='home'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('register/', register, name='register'),  
    path('login/', login_view, name='login'),
    path('about/', about, name='about'),
    path('add-book/', add_book, name='add_book'),
    path('profile/', profile, name='profile'),
    path('notifications/', notifications, name='notifications'),  
    path('more/', views.more, name='more'),  
    path('recommendations/', views.recommendations, name='recommendations'),
    path('new-releases/', views.new_releases, name='new-releases'),
    path('explore/', views.explore, name='explore'),
    path('awards/', views.awards, name='awards'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),]
