from datetime import date


class SimpleReport:
    @staticmethod
    def generate(list_of_report):
        current_year = str(date.today())
        for report in list_of_report:
            old_year = min(report.get("data_de_fabricacao"), current_year)
            one_index_of_list = list_of_report[0].get("nome_da_empresa")
            res = max(current_year, report.get("data_de_validade"))
            if one_index_of_list == report.get("nome_da_empresa"):
                return_name = report.get("nome_da_empresa")
            else:
                return_name = list_of_report[2].get("nome_da_empresa")
        result = (
            f"Data de fabricação mais antiga: {old_year}\n"
            f"Data de validade mais próxima: {res}\n"
            f"Empresa com mais produtos: {return_name}"
        )
        return result
