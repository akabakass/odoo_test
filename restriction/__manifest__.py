{
        "name": "restrictions",
        "version": "0.1",
        "depends": ['base', 'website_sale', 'delivery', 'sale', 'product', 'stock'],
        "data": [
            "security/ir.model.access.csv",
            "views/ship_restriction_view.xml",
            "views/product_template_restriction_view.xml",
            "views/product_product_restriction_view.xml"
            ],
        "installable": True,
        "description": "test app",
        "application": True

        }
