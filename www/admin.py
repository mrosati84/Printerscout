from django.contrib import admin
from www.models import Company, Brand, Printer

# Register your models here.

class PrinterAdmin(admin.ModelAdmin):
    list_display = ('label', 'company', 'area', 'referer', 'brand', 'model', 'is_network_printer')
    list_filter = ['company']
    fieldsets = [
        ('', { 'fields': ['label', 'company', 'area', 'floor', 'office', 'referer', 'brand', 'model', 'image', 'ip_address'] }),
        ('Prima visita', { 'fields': ['first_visit', 'first_visit_black', 'first_visit_color'] }),
        ('Seconda visita', { 'fields': ['second_visit', 'second_visit_black', 'second_visit_color'] }),
    ]

admin.site.register(Company)
admin.site.register(Brand)
admin.site.register(Printer, PrinterAdmin)
