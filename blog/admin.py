from django.contrib import admin
from .models import Post,Category,Tag
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields = ('name', 'status', 'is_nav', 'owner')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status', 'owner')