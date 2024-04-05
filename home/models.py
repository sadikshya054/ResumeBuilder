from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    linkedin = models.URLField(max_length=200)
    summary = models.TextField()
    skills = models.TextField()
    awards = models.TextField()
    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
