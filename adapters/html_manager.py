from weasyprint import HTML


class HtmlManager:
    def html_to_pdf(self, source: str, outupt_name: str) -> None:
        HTML(string=source).write_pdf(outupt_name)
