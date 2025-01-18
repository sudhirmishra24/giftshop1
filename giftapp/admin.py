from django.contrib import admin
from .models  import customer,Product,Cart
# Register your models here.
class customerAdmin(admin.ModelAdmin):
    list_display=['cname','cadd','phone','email','username','password','images']
admin.site.register(customer,customerAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','image']
admin.site.register(Product)

class CartAdmin(admin.ModelAdmin):
    list_display=['product','quantity']
admin.site.register(Cart)
