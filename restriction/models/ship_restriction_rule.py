from odoo import models, fields

class ShipRestrictionRule(models.Model):
    _inherit = "delivery.carrier"
    _description = "the lists of restictions for the shipper"

    restriction_tags_ids = fields.Many2many('ship.restriction.tag', string="Restrictions")
