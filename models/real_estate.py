from odoo import models, fields

class RealEstate(models.Model):
    _name = "real.estate"
    _description = "Real Estate Module"

    active = fields.Boolean(default=True, invisble=True) 
    name = fields. Char(required=True) 
    date = fields.Date('Date')
    state = fields.Selection(
        [
            ("new", "New"),
            ("received", "Offer Received"),
            ("accepted", "Offer Accepted"), ("sold", "Sold"),
            ("canceled", "Canceled"),
            
        ],
        required=True,
        copy=False,
        default="new"
    )
    postcode = fields.Char()

    def _default_date (self):
        return fields.Date.today()


    date_availability = fields.Date(default=_default_date) 
    expected_price = fields. Float (required=True)
    best_offer = fields.Float() 
    selling_price = fields. Float(readonly=True, copy=False)
    description = fields.Text() 
    bedrooms = fields.Integer(default=2)
    living_area = fields. Integer (string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields. Boolean()
    garden_area = fields. Integer()
    totalarea = fields. Integer()
    garden_orientation = fields. Selection(
        [
        ("north", "North"),
        ("south", "South"),
        ("east", "East"),
        ("west","west"),
        ],
    )
    estate_type_id = fields.Many2one("estate.property.type")
    offer_ids = fields.One2many("real.estate.offer", "property_id")