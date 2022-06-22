import csv
import os
import json
import xmltodict
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
        elif format_path == '.json':
            return Inventory.json_reader
        elif format_path == '.xml':
            return Inventory.xml_reader

    @classmethod
    def csv_reader(cls, path):
        with open(path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            csv_list = []
            for file in reader:
                csv_list.append(file)
            return csv_list

    @classmethod
    def json_reader(cls, path):
        with open(path, 'r') as json_file:
            json_list = json.load(json_file)
            return json_list

    @classmethod
    def xml_reader(cls, path):
        with open(path, 'r') as xml_file:
            xml_list = xml_file.read()
            return xmltodict.parse(xml_list)["dataset"]["record"]
