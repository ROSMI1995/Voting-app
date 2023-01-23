from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Profile(AbstractUser):
	#user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=256)
	#email = models.EmailField()
	phone = models.CharField(max_length=12,unique=True)
