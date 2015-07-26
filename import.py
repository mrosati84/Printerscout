#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import csv
from datetime import datetime

if __name__ == "__main__":
    env = os.environ.get('DJANGO_ENV') or local
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", '.'.join(['settings', env]))
    from www.models import Printer, Company, Brand

    with open('data.csv', 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            if row[1]:
                printer = Printer()
                company = Company.objects.filter(name__iexact=row[1])
                brand = Brand.objects.filter(name__iexact=row[6])

                if len(company) == 0:
                    company = Company()
                    company.name = row[1]
                    company.save()
                else:
                    company = company.first()

                if len(brand) == 0:
                    brand = Brand()
                    brand.name = row[6]
                    brand.save()
                else:
                    brand = brand.first()

                if row[8]:
                    first_visit_parts = row[8].split('/')
                    first_visit = datetime(day=int(first_visit_parts[0]),
                        month=int(first_visit_parts[1]),
                        year=int(first_visit_parts[2]))
                else:
                    first_visit = None

                if row[11]:
                    second_visit_parts = row[11].split('/')
                    second_visit = datetime(day=int(second_visit_parts[0]),
                        month=int(second_visit_parts[1]),
                        year=int(second_visit_parts[2]))
                else:
                    second_visit = None

                printer.label = int(row[0])
                printer.company = company
                printer.area = row[2]
                printer.floor = row[3]
                printer.office = row[4]
                printer.referer = row[5]
                printer.brand = brand
                printer.model = row[7]

                printer.first_visit = first_visit
                printer.first_visit_black = int(row[9].replace('.', '')) if row[9] else 0
                printer.first_visit_color = int(row[10].replace('.', '')) if row[10] else 0
                printer.second_visit = second_visit
                printer.second_visit_black = int(row[12].replace('.', '')) if row[12] else 0
                printer.second_visit_color = int(row[13].replace('.', '')) if row[13] else 0

                try:
                    printer.ip_address = row[14]
                except IndexError:
                    printer.ip_address = None

                print row

                printer.save()
