from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import User
from django.utils import timezone

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля',  widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль',  widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'bio', 'avatar', 'email', 'country', 'city', 'occupation', 'gender', 'age']

class UserPasswordChangeForm(PasswordChangeForm):
    pass

class BioForm(forms.ModelForm):
    is_online = forms.BooleanField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = ['is_online', 'username', 'bio', 'avatar', 'email', 'country', 'city', 'occupation', 'gender', 'age']

    def __init__(self, *args, **kwargs):
        super(BioForm, self).__init__(*args, **kwargs)
        self.fields['is_online'].initial = self.instance.is_online()

    def save(self, commit=True):
        user = super(BioForm, self).save(commit)
        user.update_last_login()
        return user
