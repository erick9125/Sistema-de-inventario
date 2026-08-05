from datetime import date, datetime
from io import BytesIO
from typing import Callable, Iterable, Sequence

from django.http import HttpResponse
from django.utils import timezone
from openpyxl import Workbook


def _excel_safe(value: object) -> object:
    if isinstance(value, datetime):
        if timezone.is_aware(value):
            return timezone.make_naive(value, timezone.get_current_timezone())
        return value
    if isinstance(value, date):
        return value
    return value


class ExcelExporter:
    def export(
        self,
        *,
        title: str,
        headers: Sequence[str],
        rows: Iterable[Sequence[object]],
        filename: str,
    ) -> HttpResponse:
        workbook = Workbook()
        sheet = workbook.active
        sheet["B1"] = title
        sheet.merge_cells("B1:E1")

        for index, header in enumerate(headers, start=2):
            sheet.cell(row=3, column=index).value = header

        row_number = 4
        for row in rows:
            for column, value in enumerate(row, start=2):
                sheet.cell(row=row_number, column=column).value = _excel_safe(value)
            row_number += 1

        buffer = BytesIO()
        workbook.save(buffer)
        buffer.seek(0)

        response = HttpResponse(
            buffer.getvalue(),
            content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        response["Content-Disposition"] = f'attachment; filename="{filename}"'
        return response

    def export_from_queryset(
        self,
        *,
        title: str,
        headers: Sequence[str],
        queryset: Iterable[object],
        row_builder: Callable[[object], Sequence[object]],
        filename: str,
    ) -> HttpResponse:
        rows = (row_builder(item) for item in queryset)
        return self.export(title=title, headers=headers, rows=rows, filename=filename)
