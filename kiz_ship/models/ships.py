# Copyright (C) 2021 Picg

from odoo import api, fields, models

class ShipsShip(models.Model):
    _name = "ships.ship"
    _description = "ship"

    name = fields.Char("ship", required=True)
    sno = fields.Char("sno", required=True)
    note = fields.Text(string="Description")
    ship_image = fields.Binary(string="Ship Image")
    ship_ids = fields.One2many(
          comodel_name="crm.lead",
          inverse_name="ship_id",
          string="lead",
    )