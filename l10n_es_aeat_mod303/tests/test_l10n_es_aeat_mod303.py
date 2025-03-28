# Copyright 2016-2019 Tecnativa - Pedro M. Baeza
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

import logging

from odoo import exceptions

from odoo.addons.l10n_es_aeat.tests.test_l10n_es_aeat_mod_base import (
    TestL10nEsAeatModBase,
)

_logger = logging.getLogger("aeat.303")


class TestL10nEsAeatMod303Base(TestL10nEsAeatModBase):
    # Set 'debug' attribute to True to easy debug this test
    # Do not forget to include '--log-handler aeat:DEBUG' in Odoo command line
    debug = False
    taxes_sale = {
        # tax code: (base, tax_amount)
        "S_IVA4B": (1000, 40),
        "S_IVA4B//neg": (-100, -4),
        "S_IVA4S": (1100, 44),
        "S_IVA10B": (1200, 120),
        "S_IVA10B//neg": (-120, -12),
        "S_IVA10S": (1300, 130),
        "S_IVA21B": (1400, 294),
        "S_IVA21B//neg": (-140, -29.4),
        "S_IVA21S": (1500, 315),
        "S_REQ05": (1700, 8.5),
        "S_REQ014": (1800, 25.2),
        "S_REQ52": (1900, 98.8),
        "S_IVA0_E": (2000, 0),
        "S_IVA_E": (2100, 0),
        "S_IVA_NS": (2200, 0),
        "S_IVA0_ISP": (2300, 0),
        "S_IVA0_IC": (2400, 0),
        "S_IVA0_SP_I": (2500, 0),
        "S_IVA0": (2600, 0),
    }
    taxes_purchase = {
        # tax code: (base, tax_amount)
        "P_IVA4_IC_BC": (100, 0),
        "P_IVA10_IC_BC": (200, 0),
        "P_IVA21_IC_BC": (300, 0),
        "P_IVA4_SP_IN": (400, 0),
        "P_IVA10_SP_IN": (500, 0),
        "P_IVA21_SP_IN": (600, 0),
        "P_IVA4_IC_BI": (700, 0),
        "P_IVA10_IC_BI": (800, 0),
        "P_IVA21_IC_BI": (900, 0),
        "P_IVA4_SP_EX": (110, 0),
        "P_IVA10_SP_EX": (120, 0),
        "P_IVA21_SP_EX": (130, 0),
        "P_IVA4_ISP": (140, 0),
        "P_IVA10_ISP": (150, 0),
        "P_IVA4_SC": (210, 8.4),
        "P_IVA4_SC//neg": (-21, -0.84),
        "P_IVA10_SC": (220, 22),
        "P_IVA10_SC//neg": (-22, -2.2),
        "P_IVA21_SC": (230, 48.3),
        "P_IVA21_SC//neg": (-23, -4.83),
        "P_IVA4_BC": (240, 9.6),
        "P_IVA10_BC": (250, 25),
        "P_IVA21_BC": (260, 54.6),
        "P_REQ05": (270, 1.35),
        "P_REQ014": (280, 3.92),
        "P_REQ52": (290, 15.08),
        "P_IVA4_BI": (310, 12.4),
        "P_IVA10_BI": (320, 32),
        "P_IVA21_BI": (330, 69.3),
        "P_IVA4_IBC": (340, 13.6),
        "P_IVA10_IBC": (350, 35),
        "P_IVA21_IBC": (360, 75.6),
        "P_IVA4_IBI": (370, 14.8),
        "P_IVA10_IBI": (380, 38),
        "P_IVA21_IBI": (390, 81.9),
        # 'P_IVA12_AGR': (410, 49.2),
    }
    taxes_result = {
        # Régimen General - Base imponible 4%
        "1": (3 * 1000) + (3 * 1100) - 3 * 100,  # S_IVA4B, S_IVA4S
        # Régimen General - Cuota 4%
        "3": (3 * 40) + (3 * 44) - 3 * 4,  # S_IVA4B, S_IVA4S
        # Régimen General - Base imponible 10%
        "4": (3 * 1200) + (3 * 1300) - 3 * 120,  # S_IVA10B, S_IVA10S
        # Régimen General - Cuota 10%
        "6": (3 * 120) + (3 * 130) - 3 * 12,  # S_IVA10B, S_IVA10S
        # Régimen General - Base imponible 21%
        # S_IVA21B, S_IVA21S
        "7": (3 * 1400) + (3 * 1500) - 3 * 140,
        # Régimen General - Cuota 21%
        # S_IVA21B, S_IVA21S
        "9": (3 * 294) + (3 * 315) - 3 * 29.4,
        # Adq. intracomunitarias de bienes y servicios - Base
        "10": (
            (3 * 100)
            + (3 * 200)
            + (3 * 300)
            + (3 * 400)  # P_IVAx_IC_BC_2
            + (3 * 500)
            + (3 * 600)
            + (3 * 700)  # P_IVAx_SP_IN_1
            + (3 * 800)
            + (3 * 900)  # P_IVAx_IC_BI_2
        ),
        # Adq. intracomunitarias de bienes y servicios - Cuota
        "11": (
            (3 * 4)
            + (3 * 20)
            + (3 * 63)
            + (3 * 16)  # P_IVAx_IC_BC_2
            + (3 * 50)
            + (3 * 126)
            + (3 * 28)  # P_IVAx_SP_IN_1
            + (3 * 80)
            + (3 * 189)  # P_IVAx_IC_BI_2
        ),
        # Op. inv. del suj. pasivo (excepto adq. intracom.) - Base
        "12": (
            (3 * 110)
            + (3 * 120)
            + (3 * 130)
            + (3 * 140)  # P_IVAx_SP_EX_1
            + (3 * 150)
        ),
        # Op. inv. del suj. pasivo (excepto adq. intracom.) - Cuota
        "13": (
            (3 * 4.4)
            + (3 * 12)
            + (3 * 27.3)
            + (3 * 5.6)  # P_IVAx_SP_EX_1
            + (3 * 15)
        ),
        # Modificación bases y cuotas - Base (Compras y ventas)
        "14": (
            (-1)
            * (
                1000
                + 1100
                - 100
                + 1200  # S_IVA4B, S_IVA4S
                + 1300
                - 120
                + 1400  # S_IVA10B, S_IVA10S
                + 1500
                - 140
                + 100  # S_IVA21B,S_IVA21S
                + 200
                + 300
                + 400  # P_IVAx_IC_BC_2
                + 500
                + 600
                + 700  # P_IVAx_SP_IN_1
                + 800
                + 900
                + 110  # P_IVAx_IC_BI_2
                + 120
                + 130
                + 140  # P_IVAx_SP_EX_1
                + 150
            )  # P_IVAx_ISP_2
        ),
        # Modificación bases y cuotas - Cuota (Compras y ventas)
        "15": (
            (-1)
            * (
                40
                + 44
                - 4
                + 120  # S_IVA4B, S_IVA4S
                + 130
                - 12
                + 294  # S_IVA10B, S_IVA10S
                + 315
                - 29.4
                + 4  # S_IVA21B, S_IVA21S
                + 20
                + 63
                + 16  # P_IVAx_IC_BC_2
                + 50
                + 126
                + 28  # P_IVAx_SP_IN_1
                + 80
                + 189
                + 4.4  # P_IVAx_IC_BI_2
                + 12
                + 27.3
                + 5.6  # P_IVAx_SP_EX_1
                + 15
            )
        ),
        # Recargo equivalencia - Base imponible 0.5%
        "16": (3 * 1700),  # S_REQ05
        # Recargo equivalencia - Cuota 0.5%
        "18": (3 * 8.5),  # S_REQ05
        # Recargo equivalencia - Base imponible 1.4%
        "19": (3 * 1800),  # S_REQ014
        # Recargo equivalencia - Cuota 1.4%
        "21": (3 * 25.2),  # S_REQ014
        # Recargo equivalencia - Base imponible 5.2%
        "22": (3 * 1900),  # S_REQ52
        # Recargo equivalencia - Cuota 5.2%
        "24": (3 * 98.8),  # S_REQ52
        # Mod. bases y cuotas del recargo de equivalencia - Base
        "25": (-1) * (1700 + 1800 + 1900),  # S_REQ05, S_REQ014, S_REQ52
        # Mod. bases y cuotas del recargo de equivalencia - Cuota
        "26": (-1) * (8.5 + 25.2 + 98.8),  # S_REQ05, S_REQ014, S_REQ52
        # Cuotas soportadas en op. int. corrientes - Base
        "28": (
            (3 * 110)
            + (3 * 120)
            + (3 * 130)
            + (3 * 140)  # P_IVAx_SP_EX_2
            + (3 * 150)
            + (3 * 210)  # P_IVAx_ISP_1
            + (3 * 220)
            + (3 * 230)
            + (3 * -21)
            + (3 * -22)
            + (3 * -23)
            + (3 * 240)  # P_IVAx_SC
            + (3 * 250)
            + (3 * 260)
            + (3 * 270)  # P_IVAx_BC
            + (3 * 280)
            + (3 * 290)  # P_REQ05, P_REQ014, P_REQ5.2
        ),
        # Cuotas soportadas en op. int. corrientes - Cuota
        "29": (
            (3 * 4.4)
            + (3 * 12)
            + (3 * 27.3)
            + (3 * 5.6)  # P_IVAx_SP_EX_2
            + (3 * 15)
            + (3 * 8.4)  # P_IVAx_ISP_1
            + (3 * 22)
            + (3 * 48.3)
            + (3 * -0.84)
            + (3 * -2.2)
            + (3 * -4.83)
            + (3 * 9.6)  # P_IVAx_SC
            + (3 * 25)
            + (3 * 54.6)
            + (3 * 1.35)  # P_IVAx_BC
            + (3 * 3.92)
            + (3 * 15.08)  # P_REQ05, P_REQ014  # P_REQ5.2
        ),
        # Cuotas soportadas en op. int. bienes de inversión - Base
        "30": (3 * 310) + (3 * 320) + (3 * 330),  # P_IVAx_BI
        # Cuotas soportadas en op. int. bienes de inversión - Cuota
        "31": (3 * 12.4) + (3 * 32) + (3 * 69.3),  # P_IVAx_BI
        # Cuotas soportadas en las imp. bienes corrientes - Base
        "32": (3 * 340) + (3 * 350) + (3 * 360),  # P_IVAx_IBC
        # Cuotas soportadas en las imp. bienes corrientes - Cuota
        "33": (3 * 13.6) + (3 * 35) + (3 * 75.6),  # P_IVAx_IBC
        # Cuotas soportadas en las imp. bienes de inversión - Base
        "34": (3 * 370) + (3 * 380) + (3 * 390),  # P_IVAx_IBI
        # Cuotas soportadas en las imp. bienes de inversión - Cuota
        "35": (3 * 14.8) + (3 * 38) + (3 * 81.9),  # P_IVAx_IBI
        # En adq. intra. de bienes y servicios corrientes - Base
        "36": (
            (3 * 100)
            + (3 * 200)
            + (3 * 300)
            + (3 * 400)  # P_IVAx_IC_BC_1
            + (3 * 500)
            + (3 * 600)  # P_IVAx_SP_IN_2
        ),
        # En adq. intra. de bienes y servicios corrientes - Cuota
        "37": (
            (3 * 4)
            + (3 * 20)
            + (3 * 63)
            + (3 * 16)  # P_IVAx_IC_BC_1
            + (3 * 50)
            + (3 * 126)  # P_IVAx_SP_IN_2
        ),
        # En adq. intra. de bienes de inversión - Base
        "38": (3 * 700) + (3 * 800) + (3 * 900),  # P_IVAx_IC_BI_1
        # En adq. intra. de bienes de inversión - Cuota
        "39": (3 * 28) + (3 * 80) + (3 * 189),  # P_IVAx_IC_BI_1
        # Rectificación de deducciones - Base
        "40": (
            (-1)
            * (
                270
                + 280
                + 290
                + 240  # P_REQ05, P_REQ014, P_REQ5.2
                + 250
                + 260
                + 210  # P_IVAx_BC
                + 220
                + 230
                - 21
                - 22
                - 23
                + 310  # P_IVAx_SC
                + 320
                + 330
                + 340  # P_IVAx_BI
                + 350
                + 360
                + 370  # P_IVAx_IBC
                + 380
                + 390
                + 100  # P_IVAx_IBI
                + 200
                + 300
                + 700  # P_IVAx_IC_BC_1
                + 800
                + 900
                + 400  # P_IVAx_IC_BI_1
                + 500
                + 600
                + 110  # P_IVAx_SP_IN_2
                + 120
                + 130
                + 140  # P_IVAx_SP_EX_2
                + 150
            )
        ),
        # Rectificación de deducciones - Cuota
        "41": (
            (-1)
            * (
                1.35
                + 3.92
                + 15.08
                + 9.6  # P_REQ05, P_REQ014, P_REQ5.2
                + 25
                + 54.6
                + 8.4  # P_IVAx_BC
                + 22
                + 48.3
                - 0.84
                - 2.2
                - 4.83
                + 12.4  # P_IVAx_SC
                + 32
                + 69.3
                + 13.6  # P_IVAx_BI
                + 35
                + 75.6
                + 14.8  # P_IVAx_IBC
                + 38
                + 81.9
                + 4  # P_IVAx_IBI
                + 20
                + 63
                + 28  # P_IVAx_IC_BC_1
                + 80
                + 189
                + 16  # P_IVAx_IC_BI_1
                + 50
                + 126
                + 4.4  # P_IVAx_SP_IN_2
                + 12
                + 27.3
                + 5.6  # P_IVAx_SP_EX_2
                + 15
            )
        ),
        # Compensaciones Rég. especial A. G. y P. - Cuota compras
        "42": 0,
        # Regularización bienes de inversión
        "43": 0,
        # Regularización por aplicación del porcentaje definitivo de prorrata
        "44": 0,
        # Entregas intra. de bienes y servicios - Base ventas
        "59": (2 * 2400) + (2 * 2500),  # S_IVA0_IC, S_IVA0_SP_I
        # Exportaciones y operaciones asimiladas - Base ventas
        "60": (2 * 2000) + (2 * 2600),  # S_IVA0_E + S_IVA0
        # Importes de las entregas de bienes y prestaciones de servicios
        # a las que habiéndoles sido aplicado el régimen especial del
        # criterio de caja hubieran resultado devengadas conforme a la regla
        # general de devengo contenida en el art. 75 LIVA - Base imponible
        "62": 0,
        # Importes de las entregas de bienes y prestaciones de servicios
        # a las que habiéndoles sido aplicado el régimen especial del
        # criterio de caja hubieran resultado devengadas conforme a la regla
        # general de devengo contenida en el art. 75 LIVA - Cuota
        "63": 0,
        # Importe de las adquisiciones de bienes y servicios a las que sea
        # de aplicación o afecte el régimen especial del criterio de caja
        # conforme a la ley general de devengo contenida en el artículo
        # 75 de LIVA - Base imponible
        "74": 0,
        # Importe de las adquisiciones de bienes y servicios a las que sea
        # de aplicación o afecte el régimen especial del criterio de caja
        # conforme a la ley general de devengo contenida en el artículo
        # 75 de LIVA - Cuota
        "75": 0,
    }

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Create model
        cls.model303 = cls.env["l10n.es.aeat.mod303.report"].create(
            {
                "name": "9990000000303",
                "company_id": cls.company.id,
                "company_vat": "1234567890",
                "contact_name": "Test owner",
                "statement_type": "N",
                "support_type": "T",
                "contact_phone": "911234455",
                "year": 2024,
                "period_type": "1T",
                "date_start": "2024-01-01",
                "date_end": "2024-03-31",
                "journal_id": cls.journal_misc.id,
            }
        )
        cls.model303_4t = cls.model303.copy(
            {
                "name": "9994000000303",
                "period_type": "4T",
                "date_start": "2024-09-01",
                "date_end": "2024-12-31",
            }
        )


class TestL10nEsAeatMod303(TestL10nEsAeatMod303Base):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Purchase invoices
        cls._invoice_purchase_create("2024-01-01")
        cls._invoice_purchase_create("2024-01-02")
        purchase = cls._invoice_purchase_create("2024-01-03")
        cls._invoice_refund(purchase, "2024-01-18")
        # Sale invoices
        cls._invoice_sale_create("2024-01-11")
        cls._invoice_sale_create("2024-01-12")
        sale = cls._invoice_sale_create("2024-01-13")
        cls._invoice_refund(sale, "2024-01-14")
        # Invoices for testing partial compensation
        cls.taxes_sale = {"S_IVA21B": (2000, 420)}
        cls.taxes_purchase = {"P_IVA21_BC": (500, 105)}
        cls._invoice_sale_create("2025-01-01")
        cls._invoice_purchase_create("2025-01-01")
        cls.taxes_sale = {"S_IVA21B": (100, 21)}
        cls.taxes_purchase = {"P_IVA21_BC": (4000, 840)}
        cls._invoice_sale_create("2025-04-01")
        cls._invoice_purchase_create("2025-04-01")
        cls.taxes_sale = {"S_IVA21B": (3000, 630)}
        cls.taxes_purchase = {"P_IVA21_BC": (100, 21)}
        cls._invoice_sale_create("2025-07-01")
        cls._invoice_purchase_create("2025-07-01")
        cls.taxes_sale = {"S_IVA21B": (1350, 283.50)}
        cls.taxes_purchase = {"P_IVA21_BC": (100, 21)}
        cls._invoice_sale_create("2025-10-01")
        cls._invoice_purchase_create("2025-10-01")

    def _check_tax_lines(self):
        for field, result in iter(self.taxes_result.items()):
            _logger.debug("Checking tax line: %s" % field)
            lines = self.model303.tax_line_ids.filtered(
                lambda x, field=field: x.field_number == int(field)
            )
            self.assertAlmostEqual(
                sum(lines.mapped("amount")),
                result,
                2,
                "Incorrect result in field %s" % field,
            )

    def test_model_303(self):
        _logger.debug("Calculate AEAT 303 1T 2024")
        self.model303.button_calculate()
        # Test default counterpart.
        self.assertEqual(
            self.model303.counterpart_account_id.id, self.accounts["475000"].id
        )
        self.assertEqual(self.model303.state, "calculated")
        # Fill manual fields
        self.model303.write(
            {
                "porcentaje_atribuible_estado": 95,
                "potential_cuota_compensar": 250,
                "cuota_compensar": 250,
                "casilla_77": 455,
            }
        )
        self.assertAlmostEqual(self.model303.remaining_cuota_compensar, 0)
        if self.debug:
            self._print_tax_lines(self.model303.tax_line_ids)
        self._check_tax_lines()
        # Check result
        _logger.debug("Checking results")
        devengado = sum(
            self.taxes_result.get(b, 0.0)
            for b in ("3", "6", "9", "11", "13", "15", "18", "21", "24", "26")
        )
        deducir = sum(
            self.taxes_result.get(b, 0.0)
            for b in ("29", "31", "33", "35", "37", "39", "41", "42", "43", "44")
        )
        subtotal = round(devengado - deducir, 3)
        estado = round(subtotal * 0.95, 3)
        result = round(estado + 455 - 250, 3)
        self.assertAlmostEqual(self.model303.total_devengado, devengado, 2)
        self.assertAlmostEqual(self.model303.total_deducir, deducir, 2)
        self.assertAlmostEqual(self.model303.casilla_46, subtotal, 2)
        self.assertAlmostEqual(self.model303.atribuible_estado, estado, 2)
        self.assertAlmostEqual(self.model303.casilla_69, result, 2)
        self.assertAlmostEqual(self.model303.resultado_liquidacion, result, 2)
        self.assertAlmostEqual(
            self.model303_4t.tax_line_ids.filtered(
                lambda x: x.field_number == 80
            ).amount,
            0,
        )
        self.assertEqual(self.model303.result_type, "I")
        # Export to BOE
        export_to_boe = self.env["l10n.es.aeat.report.export_to_boe"].create(
            {"name": "test_export_to_boe.txt"}
        )
        export_config_xml_ids = [
            "l10n_es_aeat_mod303.aeat_mod303_2023_main_export_config",
            "l10n_es_aeat_mod303.aeat_mod303_2024_10_main_export_config",
        ]
        for xml_id in export_config_xml_ids:
            export_config = self.env.ref(xml_id)
            self.assertTrue(export_to_boe._export_config(self.model303, export_config))
        with self.assertRaises(exceptions.ValidationError):
            self.model303.cuota_compensar = -250
        self.model303.button_post()
        self.assertTrue(self.model303.move_id)
        self.assertEqual(self.model303.move_id.ref, self.model303.name)
        self.assertEqual(
            self.model303.move_id.journal_id,
            self.model303.journal_id,
        )
        self.assertEqual(
            self.model303.move_id.line_ids.mapped("partner_id"),
            self.env.ref("l10n_es_aeat.res_partner_aeat"),
        )
        codes = self.model303.move_id.mapped("line_ids.account_id.code")
        self.assertIn("475000", codes)
        self.assertIn("477000", codes)
        self.assertIn("472000", codes)
        self.model303.button_unpost()
        self.assertFalse(self.model303.move_id)
        self.assertEqual(self.model303.state, "cancelled")
        self.model303.button_recover()
        self.assertEqual(self.model303.state, "draft")
        self.assertEqual(self.model303.calculation_date, False)
        self.model303.button_cancel()
        self.assertEqual(self.model303.state, "cancelled")
        # Check 4T without exonerated
        self.model303_4t.button_calculate()
        self.assertAlmostEqual(
            self.model303_4t.tax_line_ids.filtered(
                lambda x: x.field_number == 80
            ).amount,
            0,
        )
        # Check 4T with exonerated
        self.model303_4t.exonerated_390 = "1"
        self.model303_4t.button_calculate()
        self.assertAlmostEqual(
            self.model303_4t.tax_line_ids.filtered(
                lambda x: x.field_number == 80
            ).amount,
            14280.0,
        )
        self.assertAlmostEqual(self.model303_4t.casilla_88, 46480.0)
        # Check change of period type
        self.model303_4t.period_type = "1T"
        self.assertEqual(self.model303_4t.exonerated_390, "2")

    @classmethod
    def change_taxes_negative_special_case(cls):
        cls.taxes_sale = {
            # tax code: (base, tax_amount)
            "S_IVA4B": (1000, 40),
            "S_IVA21B//neg": (-140, -29.4),
        }
        cls.taxes_purchase = {
            # tax code: (base, tax_amount)
            "P_IVA4_BC": (240, 9.6),
            "P_IVA21_SC//neg": (-23, -4.83),
        }
        cls.taxes_result = {
            # Régimen General - Base imponible 4%
            "1": 1000,  # S_IVA4B
            # Régimen General - Cuota 4%
            "3": 40,  # S_IVA4B
            # Régimen General - Base imponible 21%
            "7": -140,  # S_IVA21B
            # Régimen General - Cuota 21%
            "9": -29.4,  # S_IVA21B
            # Modificación bases y cuotas - Base (Compras y ventas)
            "14": 0,
            # Modificación bases y cuotas - Cuota (Compras y ventas)
            "15": 0,
            # Cuotas soportadas en op. int. corrientes - Base
            "28": 240 - 23,  # P_IVA4_IC_BC, P_IVA21_SC
            # Cuotas soportadas en op. int. corrientes - Cuota
            "29": 9.6 - 4.83,  # P_IVA4_IC_BC, P_IVA21_SC
        }

    def test_model_303_negative_special_case(self):
        self.change_taxes_negative_special_case()
        # It requires a different year from the invoices of the setup
        self._invoice_sale_create("2023-01-01")
        self._invoice_purchase_create("2023-01-01")
        self.model303.date_start = "2023-01-01"
        self.model303.date_end = "2023-03-31"
        self.model303.button_calculate()
        self._check_tax_lines()

    def test_model_303_partial_compensation(self):
        model303_1T = self.env["l10n.es.aeat.mod303.report"].create(
            {
                "name": "3030000020251",
                "company_id": self.company.id,
                "company_vat": "1234567890",
                "contact_name": "Test owner",
                "statement_type": "N",
                "support_type": "T",
                "contact_phone": "911234455",
                "year": 2025,
                "period_type": "1T",
                "date_start": "2025-01-01",
                "date_end": "2025-03-31",
                "journal_id": self.journal_misc.id,
            }
        )
        model303_1T.button_calculate()
        model303_1T.button_confirm()
        model303_1T.button_post()
        # Check move lines from 303 1T 2025
        self.assertRecordValues(
            model303_1T.move_id.line_ids.sorted("balance"),
            [
                {
                    "account_id": self.accounts["475000"].id,
                    "debit": 0.0,
                    "credit": 315.0,
                },
                {
                    "account_id": self.accounts["472000"].id,
                    "debit": 0.0,
                    "credit": 105.0,
                },
                {
                    "account_id": self.accounts["477000"].id,
                    "debit": 420.0,
                    "credit": 0.0,
                },
            ],
        )

        model303_2T = model303_1T.copy(
            {
                "name": "3030000020252",
                "period_type": "2T",
                "date_start": "2025-04-01",
                "date_end": "2025-06-30",
            }
        )
        model303_2T.button_calculate()
        model303_2T.button_confirm()
        model303_2T.button_post()
        account_470 = self.env["account.account"].search(
            [("company_id", "=", self.company.id), ("code", "=", "470000")]
        )
        # Check move lines from 303 2T 2025
        self.assertRecordValues(
            model303_2T.move_id.line_ids.sorted("balance"),
            [
                {
                    "account_id": self.accounts["472000"].id,
                    "debit": 0.0,
                    "credit": 840.0,
                },
                {
                    "account_id": self.accounts["477000"].id,
                    "debit": 21.0,
                    "credit": 0.0,
                },
                {"account_id": account_470.id, "debit": 819.0, "credit": 0.0},
            ],
        )

        model303_3T = model303_1T.copy(
            {
                "name": "3030000020253",
                "period_type": "3T",
                "date_start": "2025-07-01",
                "date_end": "2025-09-30",
            }
        )
        model303_3T.button_calculate()
        model303_3T.potential_cuota_compensar = 819
        model303_3T.cuota_compensar = 609
        model303_3T.button_confirm()
        model303_3T.button_post()
        # Check move lines from 303 3T 2025
        self.assertRecordValues(
            model303_3T.move_id.line_ids.sorted("balance"),
            [
                {"account_id": account_470.id, "debit": 0.0, "credit": 609.0},
                {
                    "account_id": self.accounts["472000"].id,
                    "debit": 0.0,
                    "credit": 21.0,
                },
                {
                    "account_id": self.accounts["477000"].id,
                    "debit": 630.0,
                    "credit": 0.0,
                },
            ],
        )

        model303_4T = model303_1T.copy(
            {
                "name": "3030000020254",
                "period_type": "4T",
                "date_start": "2025-10-01",
                "date_end": "2025-12-31",
            }
        )
        model303_4T.button_calculate()
        model303_4T.button_confirm()
        model303_4T.button_post()
        # Check move lines from 303 4T 2025
        self.assertRecordValues(
            model303_4T.move_id.line_ids.sorted("balance"),
            [
                {"account_id": account_470.id, "debit": 0.0, "credit": 210.0},
                {
                    "account_id": self.accounts["475000"].id,
                    "debit": 0.0,
                    "credit": 52.5,
                },
                {
                    "account_id": self.accounts["472000"].id,
                    "debit": 0.0,
                    "credit": 21.0,
                },
                {
                    "account_id": self.accounts["477000"].id,
                    "debit": 283.50,
                    "credit": 0.0,
                },
            ],
        )
