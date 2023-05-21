from django.db import models
from django.contrib.auth.models import User

class Registration(models.Model):
    name=models.CharField(max_length=60)
    city=models.CharField(max_length=30)
    mobile_no=models.CharField(max_length=10)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
