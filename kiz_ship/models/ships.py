# Copyright (C) 2021 Picg

from odoo import api, fields, models

class ShipsShip(models.Model):
    _name = "ships.ship"
    _description = "ship"

    name = fields.Char("ship", required=True)
    sno = fields.Char("sno", required=True)
    note = fields.Text(string="Description")
    lead_id = fields.Many2one(
        "crm.lead",
        string="Lead",
        index=True,
        tracking=True,
    )
