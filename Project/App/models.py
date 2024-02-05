from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    
    contact_id=models.AutoField(primary_key=True)
    contact_name=models.CharField(max_length=25,null=True,blank=True)
    contact_surname=models.CharField(max_length=25,null=True,blank=True)
    contact_email=models.EmailField(max_length=55,null=True,blank=True)
    comment=models.TextField(max_length=255)
    
    def __str__(self):
        return f"{self.contact_name}"
    


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
    
class Actor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image_actor = models.ImageField(upload_to='actor_images', default='path/to/default/image.jpg')
    
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=250)
    director = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    actors = models.ManyToManyField(Actor,related_name='movies')
    description = models.TextField()
    duration = models.IntegerField()  
    country_of_origin = models.CharField(max_length=100)
    release_year = models.DateField()
    poster_image = models.ImageField(upload_to="movies/")

    def __str__(self):
        return self.title
    

    
class Cinema(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name

class Hall(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    hall_number = models.IntegerField()
    seat_capacity = models.IntegerField()
    hall_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cinema.name} - Hall {self.hall_number}"
    
class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2, default=300.00)

    def __str__(self):
        return f"{self.movie.title} - {self.date} {self.time}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    showing = models.ForeignKey(Showing, on_delete=models.CASCADE)
    number_of_tickets = models.IntegerField()
    reservation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation {self.id} for {self.showing.movie.title} - {self.number_of_tickets} tickets"