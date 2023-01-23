from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from django.contrib.auth.models import User
from django import forms
from .models import Profile



class RegisterUserForm(UserCreationForm):

	class Meta(UserCreationForm):
		model = Profile
		fields = ('username','name','phone')

class RegisterChangeForm(UserChangeForm):

	class Meta(UserChangeForm):
		model=Profile
		fields = ('username','name','phone')

	


		