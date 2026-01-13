from odoo import models, api
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _get_delivery_methods(self):
        carriers = super(SaleOrder, self)._get_delivery_methods()

        cart_tags = self.order_line.mapped('product_id.all_restrictions_tags_id')
        _logger.info("Delivery")
        _logger.info("DEBUG CART TAGS: %s", cart_tags)
        _logger.info("DEBUG TAG NAMES: %s", cart_tags.mapped('name'))

        if not cart_tags:
            return carriers

        def is_available(carrier):
            forbidden = carrier.restriction_tags_ids
            return not (forbidden & cart_tags)

        available_carriers = carriers.filtered(is_available)

        _logger.info("CARRIERS RESTANTS: %s", available_carriers.mapped('name'))

        return available_carriers
