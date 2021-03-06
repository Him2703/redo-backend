from django.contrib import admin
from account.models import Account, VendorAccount, BloggerAccount
# from django.contrib.auth.admin import UserAdmin
from shop.models import Order

# Register your models here.
class OrderInline(admin.TabularInline):
    model = Order
    extra = 3



class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'contact_number', 'last_login')
    search_fields = ('email', 'contact_number', 'name', 'id')
    readonly_fields = ()
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()
    inlines = [OrderInline, ]

class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'gst',)
    search_fields = ('gst', 'shop_name')
    readonly_fields = ()
    ordering = ()
    filter_horizontal = ()
    list_filter = ()



admin.site.register(Account, AccountAdmin)
admin.site.register(VendorAccount, VendorAdmin)
admin.site.register(BloggerAccount)

# admin.site.register(Account)
# admin.site.register(VendorAccount)
