from django.shortcuts import render
from django.http import HttpResponse
from .models import Printer
import csv

# Create your views here.

def export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="stampanti.csv"'

    writer = csv.writer(response)
    printers = Printer.objects.all()

    writer.writerow(['Etichetta', 'Area', 'Modello', 'Azienda', 'Piano', 'Referente', 'Immagine', 'Data prima visita', 'Contatore nero (prima visita)', 'Contatore colore (prima visita)', 'Data seconda visita', 'Contatore nero (seconda visita)', 'Contatore colore (seconda visita)'])

    for p in printers:
        writer.writerow([p.label, p.area, p.model, p.company.name, p.floor, p.referer, p.image, p.first_visit, p.first_visit_black, p.first_visit_color, p.second_visit, p.second_visit_black, p.second_visit_color])

    return response