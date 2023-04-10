from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from .models import UserProfile, PulseReport


class ReportForm(forms.ModelForm):
    # Remove the 'date' field from the form's fields list
    class Meta:
        model = PulseReport
        fields = ['pulse']

    # Specify the 'date' field in the __init__ method with a disabled widget
    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        if self.instance.pk:  # check if the instance already exists in the database
            self.fields['date'].widget.attrs['disabled'] = True


class ProfileForm(forms.ModelForm):
    age = forms.IntegerField(required=True)

    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'height', 'weight']


class RegisterUserForm(UserCreationForm):
    name = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    height = forms.FloatField(required=True)
    weight = forms.FloatField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'name', 'age', 'height', 'weight']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
