from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Users(models.Model):
    id = models.CharField(max_length=100,unique=True,primary_key=True)
    email = models.EmailField(max_length=100,unique=True)
    passw = models.CharField(max_length=128)
    
    def set_password(self, raw_password):
        self.passw = make_password(raw_password)
        
    def check_password(self, raw_password):
        return check_password(raw_password, self.passw)
    
    def __str__(self):
        return self.email