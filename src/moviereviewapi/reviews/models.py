####### this file is created by users 

from django.db import models
from django.contrib.auth.models import User

######### table name Movie

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    poster_url = models.URLField()

    def __str__(self):
        return self.title
    

######### table name Review

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s review of {self.movie.title}"
