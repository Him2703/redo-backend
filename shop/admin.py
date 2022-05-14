from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import Product, Order,Cart,Variation,My_Wishlist


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'Weigth')
    # subcategory2__name works as subcategory2.name
    search_fields = ('id', 'name',  'subcategory2__name','subcategory2__subcategory1__name', 'price', 'product_for')
    readonly_fields = ()
    ordering = ('pub_date',)
    filter_horizontal = ()
    list_filter = ()

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','date','id')
    search_fields = ('id', 'used__name',  'date')
    readonly_fields = ()
    ordering = ('date',)
    filter_horizontal = ()
    list_filter = ()

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ('id','Weigth','delivery_charges','sales_value','gst_value','seller_commission','gst_commission','tcs','redopact_amount','seller_amount')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(My_Wishlist)
admin.site.register(Cart)
