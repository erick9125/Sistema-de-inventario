from django.http import HttpResponse

from apps.inventario.application.services.asignacion_service import AsignacionService
from apps.inventario.application.services.equipo_service import EquipoService
from apps.inventario.application.services.pda_service import PdaService
from apps.inventario.application.services.telefono_service import TelefonoService
from apps.inventario.infrastructure.reporting.excel_exporter import ExcelExporter


class ReporteService:
    def __init__(
        self,
        exporter: ExcelExporter | None = None,
        equipo_service: EquipoService | None = None,
        asignacion_service: AsignacionService | None = None,
        pda_service: PdaService | None = None,
        telefono_service: TelefonoService | None = None,
    ):
        self._exporter = exporter or ExcelExporter()
        self._equipo_service = equipo_service or EquipoService()
        self._asignacion_service = asignacion_service or AsignacionService()
        self._pda_service = pda_service or PdaService()
        self._telefono_service = telefono_service or TelefonoService()

    def equipos(self) -> HttpResponse:
        return self._exporter.export_from_queryset(
            title="REPORTE DE EQUIPOS",
            headers=["Marca", "Modelo", "Serie", "Rotulo", "Fecha ingreso", "Tipo", "Descripcion"],
            queryset=self._equipo_service.listar(),
            row_builder=lambda e: (
                e.marca,
                e.modelo,
                e.serie,
                e.rotulo,
                e.fecha_ing,
                e.tipo,
                e.descripcion,
            ),
            filename="ReporteEquipoExcel.xlsx",
        )

    def asignaciones(self) -> HttpResponse:
        return self._exporter.export_from_queryset(
            title="REPORTE DE ASIGNACIONES",
            headers=[
                "Usuario asignado",
                "Cargo",
                "Departamento",
                "Fecha_entrega",
                "Marca_equipo_asignado",
                "Modelo_equipo_asignado",
                "Serie_equipo_asignado",
                "Rotulo_equipo_asignado",
                "Tipo_equipo",
                "Activo",
            ],
            queryset=self._asignacion_service.listar(),
            row_builder=lambda a: (
                a.usuario_asig,
                a.cargo,
                a.departamento,
                a.fecha_entrega,
                a.marca_equipo_asig,
                a.modelo_equipo_asig,
                a.serie_equipo_asig,
                a.rotulo_equipo_asig,
                a.tipo_equipo,
                a.activo,
            ),
            filename="ReporteAsignacionExcel.xlsx",
        )

    def pdas(self) -> HttpResponse:
        return self._exporter.export_from_queryset(
            title="REPORTE DE PDA",
            headers=[
                "OT",
                "modelo_pda",
                "serie_pda",
                "fecha_ing",
                "fecha_desp",
                "serie_bateria",
                "num_inventario",
                "sucursal",
                "region",
                "estado",
                "dias_st",
                "descripcion_pda",
            ],
            queryset=self._pda_service.listar(),
            row_builder=lambda p: (
                p.ot,
                p.modelo_pda,
                p.serie_pda,
                p.fecha_ing,
                p.fecha_desp,
                p.serie_bateria,
                p.num_inventario,
                p.sucursal,
                p.region,
                p.estado,
                p.dias_st,
                p.descripcion_pda,
            ),
            filename="ReportePDAExcel.xlsx",
        )

    def telefonos(self) -> HttpResponse:
        return self._exporter.export_from_queryset(
            title="REPORTE DE TELEFONOS",
            headers=[
                "marca_tel",
                "modelo_tel",
                "serie_tel",
                "numero_tel",
                "fecha_ing_tel",
                "usuario_asig_tel",
                "departamento_usuario",
            ],
            queryset=self._telefono_service.listar(),
            row_builder=lambda t: (
                t.marca_tel,
                t.modelo_tel,
                t.serie_tel,
                t.numero_tel,
                t.fecha_ing_tel,
                t.usuario_asig_tel,
                t.departamento_usuario,
            ),
            filename="ReporteTelefonoExcel.xlsx",
        )
