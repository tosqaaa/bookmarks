from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from .forms import LoginForm
from .views import home, dashboard, register, edit

appname = 'account'
urlpatterns = [
    path('', home, name='home'),

    path('login/', auth_views.LoginView.as_view(form_class=LoginForm),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),

    # смена пароля
    path('password-change/',
         auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')),
         name='password_change'),
    path('password-change/done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # сброс пароля
    path('password-reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy("account:password_reset_done")),
         name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('account:password_reset_complete')),
         name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # регистрация
    path('register/', register, name='register'),

    # редактирования профиля
    path('edit/', edit, name='edit'),
]
