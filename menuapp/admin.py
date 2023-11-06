from django.contrib import admin
from menuapp.models import Menu

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']




admin.site.register(Menu, MenuAdmin)