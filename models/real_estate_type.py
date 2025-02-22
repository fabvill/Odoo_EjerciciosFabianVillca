from odoo import fields, models

class EstateType(models.Models):
    _name="real.estate.type"
    _description="test"

    name = fields.Char(string="Name")
    