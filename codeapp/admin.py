from django.contrib import admin
from .models import *
# Register your models here.

class CustomAccountAdmin(admin.ModelAdmin) :
    list_display = ['id', 'email']

class CustomContactUsAdmin(admin.ModelAdmin) :
    list_display = ['email', 'name', 'id', 'date_posted', 'responded']

class CustomNotesAdmin(admin.ModelAdmin) :
    list_display = ['title', 'id', 'user']

class CustomBookmaksAdmin(admin.ModelAdmin):
    list_display = ['bookmark','user']

admin.site.register(Account, CustomAccountAdmin)
admin.site.register(ContactUsModel, CustomContactUsAdmin)
admin.site.register(Cards)
admin.site.register(CardsSolutions)
admin.site.register(Notes, CustomNotesAdmin)
admin.site.register(Bookmarks, CustomBookmaksAdmin)
