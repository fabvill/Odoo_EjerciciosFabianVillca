from odoo import models, fields

class RealEstate(models.Model):
    _name = "real.estate"
    _description = "Real Estate Module"

    name = fields.Char(default="House", required=True)
