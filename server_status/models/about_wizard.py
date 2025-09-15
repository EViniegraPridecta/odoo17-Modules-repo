from odoo import models, fields, api # type: ignore

class AboutWizard(models.TransientModel):
    _name = "about.wizard"
    _description = "Acerca de Odoo"

    about_text = fields.Html(string="Acerca de", readonly=True)

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        res["about_text"] = """
        <h3 style="text-align:center;">AVISO – ODOO COMMUNITY 17.0</h3>
        <p>
        En cumplimiento de lo dispuesto por la normativa vigente y con el fin de informar de manera transparente a nuestros usuarios y clientes, se hace de su conocimiento lo siguiente:
        </p>

        <h4>1. Naturaleza del Software</h4>
        <p>
        Odoo Community versión 17.0 y su adaptación es un sistema de planificación de recursos empresariales (ERP) de código abierto, distribuido bajo licencia LGPL v3 (GNU Lesser General Public License), lo que implica que su uso, descarga, instalación y personalización son libres y gratuitos, sin obligación de pago de licencias.
        </p>
        <p>
        El código fuente y la documentación oficial pueden ser consultados en el sitio web oficial:
        <a href="https://www.odoo.com" target="_blank">https://www.odoo.com</a>.
        </p>

        <h4>2. Capacidad de Registro</h4>
        <p>
        La versión Community de Odoo permite la creación y administración de un número ilimitado de registros en las siguientes categorías:
        </p>
        <ul>
            <li>Facturas</li>
            <li>Clientes y proveedores (contactos)</li>
            <li>Productos</li>
            <li>Servicios</li>
            <li>Usuarios</li>
        </ul>
        <p>
        Dicha capacidad ilimitada está sujeta únicamente a los recursos técnicos del servidor en el que se instale la aplicación, sin existir restricciones impuestas por el software en relación con el volumen de datos gestionados.
        </p>

        <h4>3. Capacidad de Almacenamiento</h4>
        <p>
        El sistema que se encuentra instalado es Odoo versión 17.0 en modalidad Community y se encuentra alojado en infraestructura de nube pública, la cual permite un almacenamiento de, al menos, 1 Gigabyte (GB) de datos e información.
        </p>

        <h4>4. Cumplimiento Normativo</h4>
        <p>
        Odoo Community versión 17.0, a través de sus módulos de Contabilidad y Facturación, permite la generación de facturas electrónicas en cumplimiento con la normativa fiscal española, incluyendo los requisitos de numeración correlativa, formato de documento, integridad de la información y conservación, conforme a lo establecido por la Agencia Estatal de Administración Tributaria (AEAT).
        </p>

        <h4>5. Responsabilidad de Implementación y Configuración</h4>
        <p>
        Se informa que la correcta parametrización, personalización y cumplimiento de obligaciones legales derivadas del uso de Odoo Community 17.0 son responsabilidad del usuario o de la empresa que lo implemente.
        </p>
        <p>
        El uso del software no exime de la obligación de observar la legislación aplicable en materia fiscal, mercantil y de protección de datos.
        </p>
        """
        return res
