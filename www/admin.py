from django.contrib import admin
from www.models import Company, Printer

# Register your models here.

class PrinterAdmin(admin.ModelAdmin):
    list_display = ('company', 'label', 'area', 'referer', 'model')
    fieldsets = [
        ('', { 'fields': ['label', 'area', 'model', 'company', 'floor', 'referer', 'image'] }),
        ('Prima visita', { 'fields': ['first_visit', 'first_visit_black', 'first_visit_color'] }),
        ('Seconda visita', { 'fields': ['second_visit', 'second_visit_black', 'second_visit_color'] }),
    ]

admin.site.register(Company)
admin.site.register(Printer, PrinterAdmin)
