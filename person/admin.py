from django.contrib import admin

# Register your models here.
from .models import Customer, Order, Product, Tag

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Tag)
