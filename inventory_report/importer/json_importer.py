from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(file_json: str):
        if file_json.endswith(".json"):
            with open(file_json) as file:
                my_list_in_json = json.load(file)
            return my_list_in_json
        else:
            raise ValueError('Arquivo inválido')
