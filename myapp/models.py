from django.db import models

class Userdata(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    address=models.TextField()
    image=models.ImageField(upload_to="profile_image")
