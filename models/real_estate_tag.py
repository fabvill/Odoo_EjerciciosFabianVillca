from odoo import fields, models

class estateTag(models.Model):
    _name = "real.estate.tag"
    _description = "Tags of Real Estate Model"

    name = fields.Char(requiered=True)