from django.contrib import admin

from .models import Item, Category


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'category']
    list_editable = ['price', 'available']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
