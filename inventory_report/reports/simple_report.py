from datetime import date
import statistics


class SimpleReport:
    @staticmethod
    def generate(list_of_report):
        current_year = str(date.today())
        for report in list_of_report:
            old_year = min(report.get("data_de_fabricacao"), current_year)
            res = max(current_year, report.get("data_de_validade"))
            name = [name["nome_da_empresa"] for name in list_of_report]
            return_name = statistics.mode(name)
        result = (
            f"Data de fabricação mais antiga: {old_year}\n"
            f"Data de validade mais próxima: {res}\n"
            f"Empresa com mais produtos: {return_name}"
        )
        return result
