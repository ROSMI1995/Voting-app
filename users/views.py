from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.forms import SignUpForm, UserLoginForm
from users.models import MyUser
from django.views import View

def LoginView(request):
    context ={}
    if request.method == "POST":
        form=UserLoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user=authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            form=UserLoginForm()
            context['login_form']=form
            messages.success(request, ("Invalid Login Credentials!!!"))
    return render(request, 'register/login.html', context)

def LogOut(request):
    logout(request)
    return redirect('login')


 

class register(View):
    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = 'register/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}')

            return redirect(to='home')

        return render(request, self.template_name, {'form': form})
