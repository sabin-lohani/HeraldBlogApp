from django.contrib import admin
from .models import Blog, Contacts, User, FooterContent, FaIcon, FooterLink
# Register your models here.


admin.site.register(Blog)
admin.site.register(Contacts)
admin.site.register(User)
admin.site.register(FooterContent)
admin.site.register(FaIcon)
admin.site.register(FooterLink)