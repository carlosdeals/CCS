from django.contrib import admin
from .models import Category, Product
#from parler.admin import TranslatableAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image', 'description', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)
