from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from users.models import MyUser
from django import forms




class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=200,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Full Name',
                                                               'class': 'form-control',
                                                               }))
    
    phone = forms.CharField(max_length=12,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Phone Number',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = MyUser
        fields = ['name', 'phone', 'email', 'password1', 'password2']

    

class UserLoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput,)

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            "name":"email"})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            "name":"password"})


    def clean(self, *args, **keyargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            user = authenticate(email = email, password = password)
            if not user:
                raise forms.ValidationError("This user does not exists")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("User is no longer active")

        return super(UserLoginForm, self).clean(*args, **keyargs)
 