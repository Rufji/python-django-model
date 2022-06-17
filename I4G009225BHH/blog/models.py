from typing import Text
from django.db import models
from django.contrib.auth import get_user_model
user=get_user_model()
# Create your models here.
class post(models.Model):
    Title = models.CharField(max_length = 200)
    Text = models.TextField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()
    Author = models.ForeignKey(user, on_delete=models.CASCADE)
