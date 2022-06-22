import csv
import os
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(cls, path, types):
        # https://www.geeksforgeeks.org/python-os-path-splitext-method/
        format_path = os.path.splitext(path)[1]
        file = Inventory.get_file_type(format_path)(path)
        if types == 'simples':
            return SimpleReport.generate(file)
        else:
            return CompleteReport.generate(file)

    @classmethod
    def get_file_type(cls, format_path):
        if format_path == '.csv':
            return Inventory.csv_reader

    @classmethod
    def csv_reader(cls, path):
        with open(path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            csvList = []
            for file in reader:
                csvList.append(file)
            return csvList
