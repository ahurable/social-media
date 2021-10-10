from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import success, error
from .forms import UserLoginForm, UserCreateForm
# Create your views here.

class LoginView(View):
    def get(self, request):
        login_form = UserLoginForm()
        return render(request, 'users/login.html', {'form':login_form})
    def post(self, request):
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                success(request, message="شما با موفقیت وارد سایت شدید", extra_tags='success')
                return redirect('home_url')
            else:
                error(request, message="کاربری با مشخصات وارد شده یافت نشد", extra_tags='danger')
                return redirect(to='login_url')


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home_url')


class RegisterView(View):
    def get(self, request):
        register_form = UserCreateForm()
        return render(request, 'users/create_user.html', {'form':register_form})
    def post(self, request):
        register_form = UserCreateForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            success(request,  'ثبت نام شما با موفقیت انجام شد', extra_tags='success')
            return redirect('home_url')
        else:
            error(request, 'در ثبت نام شما مشکلی در سمت سرور رخ داد', extra_tags='danger')
            return redirect('register_url')