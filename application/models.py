from django.db import models
from django.contrib.auth.models import User
class CareerPath(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image=models.ImageField(upload_to='careers/')
    description = models.TextField()
    def __str__(self):
        return self.name
class Technology(models.Model):
    name = models.CharField(max_length=255, unique=True)
    career_path = models.ForeignKey(CareerPath, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    link=models.TextField()
    def __str__(self):
        return self.name

class wish(models.Model):
    career=models.ForeignKey(CareerPath,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)