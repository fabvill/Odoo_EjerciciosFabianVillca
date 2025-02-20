from odoo import models

class RealEstate(models.Model):
    _name = 'real.estate.property'
    _description = "Real Estate Property"
    
    name = fields.Char(default="House", required=True)
    price = fields.Float()