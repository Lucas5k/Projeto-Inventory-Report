from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(files: str):
        if files.endswith(".csv"):
            with open(files, encoding="utf-8") as file:
                my_list_in_csv = []
                listOfDict = csv.DictReader(
                    file, delimiter=",", quotechar='"'
                )
                for my_file in listOfDict:
                    my_list_in_csv.append(my_file)
                return my_list_in_csv
        else:
            raise ValueError('Arquivo inválido')
