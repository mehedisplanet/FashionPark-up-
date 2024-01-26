from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone=models.IntegerField()
    body = models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email by {self.name}"