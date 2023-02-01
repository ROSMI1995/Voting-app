from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import MyUser


class MyUserAdmin(BaseUserAdmin):
	list_display = ('email','name','phone','date_joined','last_login','is_admin','is_active')
	search_fields =  ('email','name')
	readonly_fields = ('date_joined','last_login')

	filter_horizontal =()
	list_filter=('last_login',)

	fieldsets = ()

	add_fieldsets=(
		(None,{
			'classes':('wide'),
			'fields':('email','name','phone','password1','password2'),
			}),)

	ordering =('email',)

admin.site.register(MyUser,MyUserAdmin)


