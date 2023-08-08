from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    Date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class TravelPlan(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_number = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.IntegerField()
    places = models.CharField(max_length=500)
    no_of_visitors = models.IntegerField()
    booked_before = models.BooleanField()
    find = models.CharField(max_length=50, blank=True, null=True)
    generated_itinerary = models.TextField(null=True, blank=True)  # Add this field

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
