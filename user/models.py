from django.db import models 
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    image = models.FileField( default= 'default.jpg' , upload_to='profile_pic')    

    def __str__(self):
        return f'{self.user.username} Profile'
    

