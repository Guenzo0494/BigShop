from django.contrib import admin
from django.contrib.auth.models import Group

from products.models import Category, Product, Profile

# Register your models here.

admin.site.unregister(Group)

admin.site.register(Product)
admin.site.register(Category)

admin.site.register(Profile)