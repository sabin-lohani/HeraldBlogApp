from django.urls import path

from .views import index, about, contacts, partData, edit, delete, createBlog

app_name = 'crud'
urlpatterns = [
    path("",index, name="home"),
    path("about/", about, name="about"),
    path("<int:id>/", partData, name="part-data"),
    path("create-blog/", createBlog, name="create-blog"),
    path('update/<int:id>/', edit, name="update-blog"),
    path('delete/<int:id>/', delete, name="delete-blog"),
    path("contacts/", contacts, name="contact"),
]