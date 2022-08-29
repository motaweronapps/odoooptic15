# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    lens_visible_sph = fields.Boolean(default=True)
    lens_visible_cyl = fields.Boolean(default=True)
    lens_visible_axis = fields.Boolean(default=True)
    lens_visible_prism = fields.Boolean(default=True)
    lens_visible_add = fields.Boolean(default=True)
    lens_visible_va = fields.Boolean(default=True)
    lens_visible_pd = fields.Boolean(default=True)
    lens_visible_far_near = fields.Boolean(default=False)
