from django import forms
from django.db import models
from .models import CustomUserModel

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'نام کاربری', 'name':'username'
    }), label='')
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        'class':'form-control', 'placeholder':'رمز عبور', 'name':'password'
    }), label='')

class UserCreateForm(forms.ModelForm):

    password = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={
        'class':'form-control', 'placeholder':'رمز عبور', 'name':'password', 'id':'password'
    }), label='')
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={
        'class':'form-control', 'placeholder':'تکرار رمز عبور', 'name':'password2', 'id':'repassword'
    }), label='')

    class Meta:
        model = CustomUserModel
        fields = ['username', 'email', 'phone_number']
        widgets = {
            'username': forms.TextInput(attrs={
                'class':'form-control', 'placeholder':'نام کاربری', 'name':'username'
            }),
            'email': forms.EmailInput(attrs={
                'class':'form-control', 'placeholder':'ایمیل', 'name':'email'
            }),
            'phone_number': forms.NumberInput(attrs={
                'class':'form-control', 'placeholder':'شماره تلفن همراه', 'name':'phoneNumber'
            }),
        }

    def clean(self):
        cd = super().clean()
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('رمز عبور با تکرار آن مغایرت دارد')
        return cd

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if phone_number:
            if len(phone_number) > 11:
                raise forms.ValidationError('شماره همراه شما بیشتر از حد مجاز است')
            elif len(phone_number) < 10:
                raise forms.ValidationError('شماره همراه شما کمتر از حد مجاز است')
        return phone_number

    def save(self, commit=True):
        cd = self.clean()
        instance = super().save(commit=False)
        instance.set_password(cd['password'])
        if commit:
            instance.save()