from datetime import date
from collections import Counter


class SimpleReport():
    def oldest_manufacture(list):
        oldest = {
            date.fromisoformat(product["data_de_fabricacao"])
            for product in list
        }
        return min(oldest).isoformat()

    def validate_closer(list):
        closer = {
                date.fromisoformat(product["data_de_validade"])
                for product in list
                if date.fromisoformat(product["data_de_validade"])
                >= date.today()
            }
        return min(closer).isoformat()

    def company_with_more_products(list):
        [(company, _)] = Counter(
            item["nome_da_empresa"] for item in list
            ).most_common(1)
        return company

    def generate(list):
        oldest = SimpleReport.oldest_manufacture(list)
        closer = SimpleReport.validate_closer(list)
        company = SimpleReport.company_with_more_products(list)

        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {closer}\n"
            f"Empresa com mais produtos: {company}"
        )
