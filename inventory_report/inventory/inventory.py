from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    def verify_is_manipulate(files: str):
        if files.endswith('.csv'):
            my_list_in_csv = []
            with open(files, encoding="utf-8") as file:
                listOfDict = csv.DictReader(file, delimiter=",", quotechar='"')
                for my_file in listOfDict:
                    my_list_in_csv.append(my_file)
                return my_list_in_csv

        if files.endswith('.json'):
            with open(files) as file:
                my_list_in_json = json.load(file)
                return my_list_in_json

        if files.endswith('.xml'):
            with open(files) as file:
                my_list_in_xml = xmltodict.parse(file.read(), encoding="utf-8")
                return my_list_in_xml['dataset']['record']

    @staticmethod
    def import_data(files, type):
        if type == "simples":
            list_of_files = Inventory.verify_is_manipulate(files)
            result = SimpleReport.generate(list_of_files)
            return result
        else:
            list_of_files = Inventory.verify_is_manipulate(files)
            result = CompleteReport.generate(list_of_files)
            return result
