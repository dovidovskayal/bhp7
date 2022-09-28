from django.contrib import admin

# Register your models here.


from .models import Category
from .models import Product
from .models import Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('name', 'parent', 'is_published')
    list_filter = ('is_published', 'parent')
    # search_fields = ('parent', 'id')
    search_help_text = 'Введите имя родительской категории или id категории'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('title', 'article', 'category', 'price', 'is_published')
    list_filter = ('is_published', 'category', 'count')
    search_fields = ('title', 'id', 'article', 'price')
    search_help_text = 'Введите имя товара, id , артикул, цену'

# admin.site.register(Category, CategoryAdmin)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('user', 'product', 'date_created', 'is_paid')
    list_filter = ('is_paid', 'user', 'date_created')
    search_fields = ('is_paid', 'user', 'date_created')
    search_help_text = 'Введите имя пользователя, статус, дату создания'

