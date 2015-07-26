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

    # writer.writerow(['Etichetta', 'Area', 'Marca', 'Modello', 'Azienda', 'Piano', 'Referente', 'Immagine', 'Data prima visita', 'Contatore nero (prima visita)', 'Contatore colore (prima visita)', 'Data seconda visita', 'Contatore nero (seconda visita)', 'Contatore colore (seconda visita)'])
    writer.writerow(['Etichetta', 'AZIENDA', 'AREA', 'PIANO', 'UFFICIO', 'UTENTI e NOTE', 'MARCA', 'MODELLO', 'DATA PRIMO RIL', 'COPIE BN', 'COPIE COLOR', 'DATA SECONDO RIL', 'COPIE BN', 'COPIE COLOR', 'IMMAGINE'])

    for p in printers:
        print p.label
        writer.writerow([p.label, p.company.name, p.area, p.floor, p.office.encode('utf-8'), p.referer.encode('utf-8'), p.brand.name, p.model.encode('utf-8'), p.first_visit, p.first_visit_black, p.first_visit_color, p.second_visit, p.second_visit_black, p.second_visit_color, p.image])

    return response