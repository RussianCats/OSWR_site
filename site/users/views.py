from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from users.forms import UserLoginForm, ProfileForm, UserRegistrationForm

def login(request):

    # логиука на вход пользователя
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                messages.success(request, f"Вы вошли в аккаунт, {username}!")

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))

                # после входа отправляем
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Вы успешно зарегистрировались, {form.username}")
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()

    context: dict[str, str] = {
        'title': 'Home - Регистрация',
        'form': form,
    }

    return render(request, 'users/registration.html', context)

@login_required
def profile(request):

    # логиука на вход пользователя
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Данные успешно изменены, {request.user.username}!")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/profile.html', context)

def users_cart(request):
    return render(request, 'users/users_cart.html')

@login_required
def logout(request):
    messages.success(request, f"Вы успешно вышли из аккаунта, {request.user.username}!")
    auth.logout(request)
    return redirect(reverse('main:index'))