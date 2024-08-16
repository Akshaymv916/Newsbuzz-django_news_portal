from django.contrib import admin

from newsapp.models import Category, Customeuser, News, Subcategory

# Register your models here.
admin.site.register(Customeuser)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(News)