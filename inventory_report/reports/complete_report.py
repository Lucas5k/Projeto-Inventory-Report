from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(list_of_report):
        simple_report = SimpleReport.generate(list_of_report)
        name = [name["nome_da_empresa"] for name in list_of_report]
        names = Counter(name)
        products = ""
        for name in names:
            products += f"- {name}: {names.get(name)}\n"

        result = (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{products}"
        )
        return result
