from django.contrib import admin 
from .models import Invoice, Vendor, Customer, Category, Product


# admin.site.register(Invoice)
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['customer', 'vendor', 'product', 'issue_date', 'due_date', 'total_amount', 'status', 'installment_payment']
    list_filter = ['customer', 'vendor', 'product', 'issue_date', 'due_date', 'total_amount', 'status', 'installment_payment']
    search_fields = ['customer', 'vendor', 'product', 'issue_date', 'due_date', 'total_amount', 'status', 'installment_payment']
    list_per_page = 10


#admin.site.register(Vendor)
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_email', 'phone_number', 'address']
    search_fields = ['name', 'contact_email', 'phone_number', 'address']
    list_per_page = 10

#admin.site.register(Customer)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_email', 'phone_number', 'address', 'preferred_payment_method']
    search_fields = ['name', 'contact_email', 'phone_number', 'address', 'preferred_payment_method']
    list_per_page = 10

#admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

#admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'image']
    list_filter = ['name', 'category', 'price', 'image']
    search_fields = ['name', 'category', 'price', 'image']
    list_per_page = 10
