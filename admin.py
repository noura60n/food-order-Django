from django.contrib import admin

# Register your models here.

from food.models import Food, Cust, Admin, Cart, Order
admin.site.register(Food)
admin.site.register(Cust)
admin.site.register(Admin)
admin.site.register(Cart)
admin.site.register(Order)
