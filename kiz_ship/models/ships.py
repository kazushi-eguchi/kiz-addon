# Copyright (C) 2021 Picg

from odoo import api, fields, models

class ApprovalsApproval(models.Model):
    _name = "ships.ship"
    _description = "ship"

    name = fields.Char("ship", required=True)
    sno = fields.Char("sno", required=True)
    note = fields.Text(string="Description")
