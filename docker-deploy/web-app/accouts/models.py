from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyUser(User):
    isDriver = models.BooleanField(default=False)