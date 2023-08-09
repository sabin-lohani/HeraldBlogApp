from django.urls import path

from .views import loginPage, logoutUser, register

app_name = 'users'
urlpatterns = [
    path("login/", loginPage, name="login"),
    path("register/", register, name="register"),
    path("logout/", logoutUser, name="logout"),
]