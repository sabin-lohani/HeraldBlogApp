from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import User

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    subheading=models.CharField(max_length=200, null=True)
    body=RichTextUploadingField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.title
    
class Contacts(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    phone = models.CharField(max_length = 150)
    message = models.TextField()

    def __str__(self):
        return self.name

class FooterContent(models.Model):
    copyright_year = models.PositiveIntegerField()
    site_url = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.site_url} - {self.copyright_year}'
    
class FaIcon(models.Model):
    name = models.CharField(max_length = 150)
    iconClass = models.CharField(max_length = 150)

    def __str__(self):
        return f'{self.name} - {self.iconClass}'

class FooterLink(models.Model):
    icon = models.ForeignKey(FaIcon, on_delete=models.SET_NULL, null=True)
    link = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.icon.name} - {self.link}'

