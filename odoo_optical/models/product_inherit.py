from odoo import models, fields


class addlensdyameters(models.Model):
    _inherit = 'product.template'
    cly = fields.Char()
    sph = fields.Char()
    axis = fields.Char()
    prism = fields.Char()
    color = fields.Char()