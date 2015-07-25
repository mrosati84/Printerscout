from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(null=True, blank=True, max_length=140, verbose_name='Azienda')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Azienza'
        verbose_name_plural = 'Aziende'

class Brand(models.Model):
    name = models.CharField(null=True, blank=True, max_length=140, verbose_name='Marca stampante')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Marca stampante'
        verbose_name_plural = 'Marche stampanti'

class Printer(models.Model):
    company = models.ForeignKey('Company', null=True, blank=True, verbose_name='Azienda')
    label = models.IntegerField(null=True, blank=True, verbose_name='Etichetta')
    area = models.CharField(null=True, blank=True, max_length=150, verbose_name='Area')
    floor = models.CharField(null=True, blank=True, max_length=120, verbose_name='Piano')
    office = models.CharField(null=True, blank=True, max_length=120, verbose_name='Ufficio')
    brand = models.ForeignKey('Brand', null=True, blank=True, verbose_name='Marca')
    model = models.CharField(null=True, blank=True, max_length=150, verbose_name='Modello')
    referer = models.CharField(null=True, blank=True, max_length=150, verbose_name='Referente')
    ip_address = models.CharField(null=True, blank=True, max_length=16, verbose_name='Indirizzo IP')
    image = models.ImageField(null=True, blank=True, verbose_name='Immagine')

    first_visit = models.DateField(null=True, blank=True, verbose_name='Data prima visita')
    first_visit_black = models.IntegerField(null=True, blank=True, verbose_name='Contatore nero')
    first_visit_color = models.IntegerField(null=True, blank=True, verbose_name='Contatore colore')

    second_visit = models.DateField(null=True, blank=True, verbose_name='Data seconda visita')
    second_visit_black = models.IntegerField(null=True, blank=True, verbose_name='Contatore nero')
    second_visit_color = models.IntegerField(null=True, blank=True, verbose_name='Contatore colore')

    def is_network_printer(self):
        if self.ip_address:
            return True
        else:
            return False

    is_network_printer.boolean = True
    is_network_printer.short_description = 'In rete'

    def __unicode__(self):
        return self.model

    class Meta:
        verbose_name = 'Stampante'
        verbose_name_plural = 'Stampanti'
