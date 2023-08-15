from django.urls import path

from .views import loginPage, logoutUser, register, resetPassword

app_name = 'users'
urlpatterns = [
    path("login/", loginPage, name="login"),
    path("register/", register, name="register"),
    path("reset-password/", resetPassword, name="reset-password"),
    path("logout/", logoutUser, name="logout"),
]