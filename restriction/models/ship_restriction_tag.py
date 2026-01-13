from odoo import models, fields

class ShipRestrictionTag(models.Model):
    _name = 'ship.restriction.tag'
    _description = 'Liste des tags pour restriction'

    name = fields.Char(string="Nom", required=True)
    color = fields.Integer(string="Couleur")
