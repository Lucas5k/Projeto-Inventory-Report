from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(file_xml: str):
        if file_xml.endswith(".xml"):
            with open(file_xml) as file:
                my_list_in_xml = xmltodict.parse(
                    file.read(), encoding="utf-8"
                )
            return my_list_in_xml["dataset"]["record"]
        else:
            raise ValueError('Arquivo inválido')
