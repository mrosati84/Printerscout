from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(null=True, blank=True, max_length=40, verbose_name='Azienda')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Azienza'
        verbose_name_plural = 'Aziende'

class Printer(models.Model):
    company = models.ForeignKey('Company', null=True, blank=True, verbose_name='Azienda')
    label = models.IntegerField(null=True, blank=True, verbose_name='Etichetta')
    area = models.CharField(null=True, blank=True, max_length=50, verbose_name='Area')
    floor = models.CharField(null=True, blank=True, max_length=20, verbose_name='Piano')
    model = models.CharField(null=True, blank=True, max_length=50, verbose_name='Modello')
    referer = models.CharField(null=True, blank=True, max_length=50, verbose_name='Referente')
    image = models.ImageField(null=True, blank=True, verbose_name='Immagine')

    first_visit = models.DateField(null=True, blank=True, verbose_name='Data prima visita')
    first_visit_black = models.IntegerField(null=True, blank=True, verbose_name='Contatore nero')
    first_visit_color = models.IntegerField(null=True, blank=True, verbose_name='Contatore colore')

    second_visit = models.DateField(null=True, blank=True, verbose_name='Data seconda visita')
    second_visit_black = models.IntegerField(null=True, blank=True, verbose_name='Contatore nero')
    second_visit_color = models.IntegerField(null=True, blank=True, verbose_name='Contatore colore')

    def __unicode__(self):
        return self.model

    class Meta:
        verbose_name = 'Stampante'
        verbose_name_plural = 'Stampanti'
