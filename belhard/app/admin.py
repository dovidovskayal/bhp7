from django.contrib import admin

# Register your models here.


from .models import Category
from .models import Product
from .models import Order


class AppAdminSite(admin.AdminSite):
    site_header = 'SITE HEADER'
    site_title = 'TITLE'
    index_title = 'INDEX TITLE'



appadmin = AppAdminSite(name='appadmin')


class ProductTabularInline(admin.TabularInline):
    model = Product



@admin.action(description='Опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Снять с публикации')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('name', 'parent', 'is_published')
    list_filter = ('is_published', 'parent')
    actions = (make_published, make_unpublished)
    # search_fields = ('parent', 'id')
    search_help_text = 'Введите имя родительской категории или id категории'
    inlines = (ProductTabularInline, )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('title', 'article', 'category', 'price', 'is_published')
    list_filter = ('is_published', 'category', 'count')
    search_fields = ('title', 'id', 'article', 'price')
    actions = (make_published, make_unpublished)
    search_help_text = 'Введите имя товара, id , артикул, цену'
    fieldsets = (
        ('Основные настройки',
         {
             'fields': ('title', 'article', 'price', 'category'),
             'description': ('описание',)
         }
         ),
        ('Дополнительные настройки',
         {'fields': ('is_published', 'descr', 'count')

          }
         )
    )
    list_editable = ('category',)
    prepopulated_fields = {'descr': ('title', 'article')}



# admin.site.register(Category, CategoryAdmin)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    empty_value_display = 'N/a'
    list_display = ('user', 'product', 'date_created', 'is_paid')
    list_filter = ('is_paid',)
    date_hierarchy = 'date_created'
    search_fields = ('is_paid', 'user', 'date_created')
    search_help_text = 'Введите имя пользователя, статус, дату создания'


appadmin.register(Category, CategoryAdmin)
appadmin.register(Product, ProductAdmin)
appadmin.register(Order, OrderAdmin)
