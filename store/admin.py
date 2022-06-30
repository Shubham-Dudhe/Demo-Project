from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer
from .models import Address
from .models import Order

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','description','image','category']

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Category,CategoryAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','phone','email','password']

admin.site.register(Customer,CustomerAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ['customer','house_no','street_name','area','town','city','state','pincode']

admin.site.register(Address,AddressAdmin)



class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','customer','address','quantity','price','mobile_number','date','status']

admin.site.register(Order,OrderAdmin)