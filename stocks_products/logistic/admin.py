from django.contrib import admin
from django.forms import BaseInlineFormSet

from .models import Stock, Product, StockProduct
# Register your models here.


class ScopeInline(admin.TabularInline):
    model = StockProduct
    extra = 0


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address']
    inlines = [ScopeInline, ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']

    