from django.contrib import admin
from .models import Blog, Contacts, User, FooterContent, FaIcon, FooterLink

admin.site.site_header = 'Herald BlogApp'
admin.site.site_title = "Herald BlogApp"
admin.site.index_title = 'Admin'

class BlogAdmin(admin.ModelAdmin):
    list_display = ("__str__", "author", "title", "subheading", "description")
    fields = ("title",)
    list_editable = "title", "subheading",
    search_fields = "title",

# Register your models here.


admin.site.register(Blog, BlogAdmin)
admin.site.register(Contacts)
admin.site.register(User)
admin.site.register(FooterContent)
admin.site.register(FaIcon)
admin.site.register(FooterLink)