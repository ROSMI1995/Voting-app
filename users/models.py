from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyUserManager(BaseUserManager):
	use_in_migrations = True

	def create_user(self, email,phone,name, password=None):
		if not email:
			raise ValueError("email is required")

		if not phone:
			raise ValueError("Phone Number is required")

		if not name:
			raise ValueError("Name is required")

		user = self.model(
			email = self.normalize_email(email),
			name = name,
			phone = phone
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email,name,phone,password=None):
		user = self.create_user(
			email = email,
			name = name,
			phone = phone,
			password = password
			)
		user.is_admin =True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user



class MyUser(AbstractBaseUser):
	email = models.EmailField(verbose_name="email address", max_length=100,unique=True)
	name = models.CharField(verbose_name="name",max_length=250)
	phone = models.CharField(verbose_name="phone",max_length=12)
	date_joined = models.DateTimeField(verbose_name='date joined',auto_now=True)
	last_login = models.DateTimeField(verbose_name='lat login',auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD ='email'
	REQUIRED_FIELDS = ['name','phone']

	objects=MyUserManager()

	def __str__(self):
		return self.name

# this methods are require to login super user from admin panel
	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True
