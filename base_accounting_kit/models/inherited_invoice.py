from odoo import api, models, fields, _
from datetime import datetime


class AccountMove(models.Model):
    _inherit = 'account.move'


    po_number = fields.Char(string="PO Ref. Number")
    po_date = fields.Date(string=" PO Date")
    pan = fields.Char(string="PAN")

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        """Set PAN Number based on the selected partner."""
        if self.partner_id:
            self.pan = self.partner_id.pan
        else:
            self.pan = False


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    mrp_price = fields.Float(string="MRP Price")
