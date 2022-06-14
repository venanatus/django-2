from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from . import forms


def sign_up(request):
    form = forms.SignUpForm(request.POST)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('users:sign_in')
    form = forms.SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


def sign_in(request):
    form = forms.SignInForm(data=request.POST)
    if form.is_valid() and request.method == 'POST':
        user = form.get_user()
        login(request, user)
        return redirect('articles:home')
    form = forms.SignInForm()
    return render(request, 'sign_in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('users:sign_in')
