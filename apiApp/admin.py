from django.contrib import admin

from .models import Product

# Register your models here.
# class ProducAdmin(admin.ModelAdmin):
#     list_display=('name','content','price','timestamp','completed')

admin.site.register(Product)