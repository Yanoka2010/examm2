from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group


def login_view(request):
    """Представление для входа в систему"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.get_full_name() or user.username}!')
            return redirect('products:product_list')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')

    return render(request, 'accounts/login.html')


def logout_view(request):
    """Представление для выхода из системы"""
    logout(request)
    messages.info(request, 'Вы успешно вышли из системы.')
    return redirect('accounts:login')


@login_required
def profile_view(request):
    """Представление профиля пользователя"""
    return render(request, 'accounts/profile.html')
