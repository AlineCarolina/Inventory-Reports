from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    @staticmethod
    def counter_companies(list):
        companies = Counter(
            [product["nome_da_empresa"] for product in list]
        )
        return companies

    @staticmethod
    def report(list):
        companies = CompleteReport.counter_companies(list)

        result = ""
        for empresa, quantidade in companies.items():
            result += f"- {empresa}: {quantidade}\n"

        return result

    @classmethod
    def generate(cls, list):
        simple = SimpleReport.generate(list)
        complet = CompleteReport.report(list)

        return (
            f"{simple}\n"
            "Produtos estocados por empresa:\n"
            f"{complet}"
        )
