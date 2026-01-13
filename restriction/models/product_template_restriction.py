from odoo import models, fields

class ProductTemplateRestriction(models.Model):
    _inherit = "product.template"
    _description = "Tags de restrictions associés au produit"

    restriction_tags_ids = fields.Many2many(
            'ship.restriction.tag',
            'restriction_prod_templ_ship_rest_tag_rel',
            string="restriction_tag ids")
