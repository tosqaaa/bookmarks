from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


def home(request):
    return render(request, 'account/home.html')


@login_required
def dashboard(request):
    context = {
        'section': 'dashboard'
    }
    return render(request, 'account/dashboard.html', context=context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            messages.success(request, 'Вы успешно зарегистрировались!')
            return render(request, 'registration/register_done.html', context={'new_user': new_user})
        else:
            messages.error(request, 'Произошла ошибка регистрации')
            return redirect('account:register')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', context={'user_form': user_form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Изменения прошли успешно!')
        else:
            messages.error(request, 'Произошла ошибка редактирования!')
            return redirect('account:dashboard')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'account/edit.html', context=context)
# def user_login(request):
#     dir(request)
#     if request.method == "POST":
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     messages.success(request, 'Успешно')
#                     return redirect('/account/')
#                 else:
#                     messages.error(request, 'Аккаунт отключен')
#             else:
#                 messages.error(request, 'Неправильный логин')
#     else:
#         form = LoginForm()
#     context = {
#         'title': 'Вход',
#         'form': form
#     }
#
#     return render(request, 'user_login.html', context=context)
