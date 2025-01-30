from django.db import models
import hashlib

# Create your models here.

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email= models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def set_password(self, raw_password):
        #hashing and saving the password
        self.password = hashlib.sha256(raw_password.encode()).hexdigest()
    
    def check_password(self, raw_password):
        return self.password == hashlib.sha256(raw_password.encode()).hexdigest()
