from django.contrib import admin

from .models import *

class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo')
    list_display_links = ('id','title')
    search_fields = ('title', 'content')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Cars, CarsAdmin)
admin.site.register(Categories, CategoryAdmin)