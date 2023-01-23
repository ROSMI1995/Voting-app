from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . forms import RegisterUserForm, RegisterChangeForm




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



def SignupView(request):
	if request.method == "POST":
		form = RegisterChangeForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			
			user =authenticate(request,username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successfull"))
			return redirect('home')
			#def form_valid(self,  form):
				#form.instance.user = self.request.user
				#return super().form_valid(form)

	else:
		form = RegisterChangeForm()



	return render(request, 'register/signup.html', {'form':form})

