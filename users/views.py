from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages




def LoginView(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user =authenticate(request,username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')

		else:
			messages.success(request, ("Invalid Login Credentials!!!"))
			return redirect('login')

	else:
		return render(request, 'register/login.html', {})

# Create your views here.
