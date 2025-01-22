from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Bookstore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_information = models.TextField()

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    contact_information = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publish_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers/', default='https://www.flaticon.com/free-icon/open-book_2702134?term=book&page=1&position=5&origin=search&related_id=2702134')

    def __str__(self):
        return self.title



class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.book.title}'
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username

