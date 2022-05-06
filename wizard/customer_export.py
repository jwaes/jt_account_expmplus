import logging
from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)


class CustomerExport(models.TransientModel):
    _name = 'jt.account.expmplus.customer.export'


    def generate_customer_xml(self):

        active_model = self.env.context.get('active_model', False)
        active_ids = self.env.context.get('active_ids', [])

        records = self.env[active_model].browse(active_ids)

        #NameError: name 'CustomerType' is not defined
        customers = CustomerType()

        for record in records:
            _logger.info("- %s", record.name)
            # cst = CustomerType.Customer()


