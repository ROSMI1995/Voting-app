from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from . forms import RegisterUserForm, RegisterChangeForm
from .models import Profile


# Register your models here.
class MyUserAdmin(UserAdmin):
	add_form = RegisterUserForm
	form = RegisterChangeForm
	model = Profile
	list_display = ['username','name','phone']

	fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('name','phone')}),
    ) 
	

admin.site.register(Profile, MyUserAdmin)