from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Restaurant(models.Model):
    text = models.TextField(max_length=249)
    photo = models.ImageField(upload_to='photos/',blank=True,null=True)
    

    
class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=249)

    def __str__(self) -> str:
        return f'{self.user.username} - {self.text[:10]}'



