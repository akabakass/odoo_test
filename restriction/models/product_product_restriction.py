from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ProductProductRestriction(models.Model):
    _inherit = "product.product"
    _description = "Tags de restrictions associés au variant"

    restriction_tags_ids_template = fields.Many2many(
            related = 'product_tmpl_id.restriction_tags_ids',
            readonly = True
            )

    restriction_tags_ids = fields.Many2many(
            'ship.restriction.tag',
            'restriction_prod_product_ship_rest_tag_rel',
            string="restriction_tag ids")


    all_restrictions_tags_id = fields.Many2many(
            'ship.restriction.tag',
            string="restrictions totales",
            compute="_compute_all_tags",
            store=False

            )

    @api.depends('restriction_tags_ids', "product_tmpl_id.restriction_tags_ids")
    def _compute_all_tags(self):
        for product in self:
            product.all_restrictions_tags_id = product.product_tmpl_id.restriction_tags_ids | product.restriction_tags_ids

    @api.constrains('restriction_tags_ids')
    def _check_no_duplicate_tags(self):
        for product in self:
            duplicates = product.restriction_tags_ids & product.product_tmpl_id.restriction_tags_ids
            if duplicates:
                tag_names = ", ".join(duplicates.mapped('name'))
                raise ValidationError(_( "Les tags suivants sont déjà présents sur le modèle et ne peuvent pas être ajoutés à la variante: %s") % tag_names)
