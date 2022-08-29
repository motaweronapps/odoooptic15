# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    optometrist_id = fields.Many2one('hr.employee', required=True, domain=[('is_optometrist', '=', True)], ondelete='restrict', copy=True)
    prescription_note = fields.Text(string="Prescription Note", copy=True)

    lens_visible_sph = fields.Boolean(default=lambda x: x.env.user.company_id.lens_visible_sph)
    lens_visible_cyl = fields.Boolean(default=lambda x: x.env.user.company_id.lens_visible_cyl)
    lens_visible_axis = fields.Boolean(default=lambda x: x.env.user.company_id.lens_visible_axis)
    lens_visible_prism = fields.Boolean(default=lambda x: x.env.user.company_id.lens_visible_prism)
    lens_visible_add = fields.Boolean(default=lambda x: x.env.user.company_id.lens_visible_add)
    lens_visible_va = fields.Boolean(default=lambda x: x.env.user.company_id.lens_visible_va)
    lens_visible_pd = fields.Boolean(default=lambda x: x.env.user.company_id.lens_visible_pd)
    lens_visible_far_near = fields.Boolean(default=lambda x: x.env.user.company_id.lens_visible_far_near)

    right_sph = fields.Many2one('optical.sph.type', rel='sale_order_optical_sph_type_right', ondelete='restrict', copy=True)
    right_cyl = fields.Many2one('optical.cyl.type', rel='sale_order_optical_cyl_type_right', ondelete='restrict', copy=True)
    right_axis = fields.Many2one('optical.axis.type', rel='sale_order_optical_axis_type_right', ondelete='restrict', copy=True)
    right_prism = fields.Many2one('optical.prism.type', rel='sale_order_optical_prism_type_right', ondelete='restrict', copy=True)
    right_add = fields.Many2one('optical.add.type', rel='sale_order_optical_add_type_right', ondelete='restrict', copy=True)
    right_va = fields.Char(string="VA", copy=True)
    right_pd = fields.Char(string="PD", copy=True)

    left_sph = fields.Many2one('optical.sph.type', rel='sale_order_optical_sph_type_left', ondelete='restrict', copy=True)
    left_cyl = fields.Many2one('optical.cyl.type', rel='sale_order_optical_cyl_type_left', ondelete='restrict', copy=True)
    left_axis = fields.Many2one('optical.axis.type', rel='sale_order_optical_axis_type_left', ondelete='restrict', copy=True)
    left_prism = fields.Many2one('optical.prism.type', rel='sale_order_optical_prism_type_left', ondelete='restrict', copy=True)
    left_add = fields.Many2one('optical.add.type', rel='sale_order_optical_add_type_left', ondelete='restrict', copy=True)
    left_va = fields.Char(string="VA", copy=True)
    left_pd = fields.Char(string="PD", copy=True)

    near_right_sph = fields.Many2one('optical.sph.type', rel='sale_order_optical_sph_type_right_near', ondelete='restrict', copy=True)
    near_right_cyl = fields.Many2one('optical.cyl.type', rel='sale_order_optical_cyl_type_right_near', ondelete='restrict', copy=True)
    near_right_axis = fields.Many2one('optical.axis.type', rel='sale_order_optical_axis_type_right_near', ondelete='restrict', copy=True)
    near_right_prism = fields.Many2one('optical.prism.type', rel='sale_order_optical_prism_type_right_near', ondelete='restrict', copy=True)
    near_right_add = fields.Many2one('optical.add.type', rel='sale_order_optical_add_type_right_near', ondelete='restrict', copy=True)
    near_right_va = fields.Char(string="VA", copy=True)
    near_right_pd = fields.Char(string="PD", copy=True)

    near_left_sph = fields.Many2one('optical.sph.type', rel='sale_order_optical_sph_type_left_near', ondelete='restrict', copy=True)
    near_left_cyl = fields.Many2one('optical.cyl.type', rel='sale_order_optical_cyl_type_left_near', ondelete='restrict', copy=True)
    near_left_axis = fields.Many2one('optical.axis.type', rel='sale_order_optical_axis_type_left_near', ondelete='restrict', copy=True)
    near_left_prism = fields.Many2one('optical.prism.type', rel='sale_order_optical_prism_type_left_near', ondelete='restrict', copy=True)
    near_left_add = fields.Many2one('optical.add.type', rel='sale_order_optical_add_type_left_near', ondelete='restrict', copy=True)
    near_left_va = fields.Char(string="VA", copy=True)
    near_left_pd = fields.Char(string="PD", copy=True)

    def get_report_lens_details(self):
        self.ensure_one()

        def x_append(l, val, condition=True):
            if condition:
                l.append(val)

        table1 = []
        table2 = []

        heading1 = ""
        heading2 = ""

        vals = []
        x_append(vals, {"value": "RX", "type": "col_head"})
        x_append(vals, {"value": "SPH", "type": "col_head"}, condition=self.lens_visible_sph)
        x_append(vals, {"value": "CYL", "type": "col_head"}, condition=self.lens_visible_cyl)
        x_append(vals, {"value": "AXIS", "type": "col_head"}, condition=self.lens_visible_axis)
        x_append(vals, {"value": "PRISM", "type": "col_head"}, condition=self.lens_visible_prism)
        x_append(vals, {"value": "ADD", "type": "col_head"}, condition=self.lens_visible_add)
        x_append(vals, {"value": "VA", "type": "col_head"}, condition=self.lens_visible_va)
        x_append(vals, {"value": "PD", "type": "col_head"}, condition=self.lens_visible_pd)
        table1.append(vals)

        vals = []
        x_append(vals, {"value": "O.D (Right)", "type": "row_head"})
        x_append(vals, {"value": self.right_sph.name, "type": "value"}, condition=self.lens_visible_sph)
        x_append(vals, {"value": self.right_cyl.name, "type": "value"}, condition=self.lens_visible_cyl)
        x_append(vals, {"value": self.right_axis.name, "type": "value"}, condition=self.lens_visible_axis)
        x_append(vals, {"value": self.right_prism.name, "type": "value"}, condition=self.lens_visible_prism)
        x_append(vals, {"value": self.right_add.name, "type": "value"}, condition=self.lens_visible_add)
        x_append(vals, {"value": self.right_va, "type": "value"}, condition=self.lens_visible_va)
        x_append(vals, {"value": self.right_pd, "type": "value"}, condition=self.lens_visible_pd)
        table1.append(vals)

        vals = []
        x_append(vals, {"value": "O.S (Left)", "type": "row_head"})
        x_append(vals, {"value": self.left_sph.name, "type": "value"}, condition=self.lens_visible_sph)
        x_append(vals, {"value": self.left_cyl.name, "type": "value"}, condition=self.lens_visible_cyl)
        x_append(vals, {"value": self.left_axis.name, "type": "value"}, condition=self.lens_visible_axis)
        x_append(vals, {"value": self.left_prism.name, "type": "value"}, condition=self.lens_visible_prism)
        x_append(vals, {"value": self.left_add.name, "type": "value"}, condition=self.lens_visible_add)
        x_append(vals, {"value": self.left_va, "type": "value"}, condition=self.lens_visible_va)
        x_append(vals, {"value": self.left_pd, "type": "value"}, condition=self.lens_visible_pd)
        table1.append(vals)

        if self.lens_visible_far_near:
            heading1 = "Far Vision"
            heading2 = "Near Vision"

            vals = []
            x_append(vals, {"value": "RX", "type": "col_head"})
            x_append(vals, {"value": "SPH", "type": "col_head"}, condition=self.lens_visible_sph)
            x_append(vals, {"value": "CYL", "type": "col_head"}, condition=self.lens_visible_cyl)
            x_append(vals, {"value": "AXIS", "type": "col_head"}, condition=self.lens_visible_axis)
            x_append(vals, {"value": "PRISM", "type": "col_head"}, condition=self.lens_visible_prism)
            x_append(vals, {"value": "ADD", "type": "col_head"}, condition=self.lens_visible_add)
            x_append(vals, {"value": "VA", "type": "col_head"}, condition=self.lens_visible_va)
            x_append(vals, {"value": "PD", "type": "col_head"}, condition=self.lens_visible_pd)
            table2.append(vals)

            vals = []
            x_append(vals, {"value": "O.D (Right)", "type": "row_head"})
            x_append(vals, {"value": self.near_right_sph.name, "type": "value"}, condition=self.lens_visible_sph)
            x_append(vals, {"value": self.near_right_cyl.name, "type": "value"}, condition=self.lens_visible_cyl)
            x_append(vals, {"value": self.near_right_axis.name, "type": "value"}, condition=self.lens_visible_axis)
            x_append(vals, {"value": self.near_right_prism.name, "type": "value"}, condition=self.lens_visible_prism)
            x_append(vals, {"value": self.near_right_add.name, "type": "value"}, condition=self.lens_visible_add)
            x_append(vals, {"value": self.near_right_va, "type": "value"}, condition=self.lens_visible_va)
            x_append(vals, {"value": self.near_right_pd, "type": "value"}, condition=self.lens_visible_pd)
            table2.append(vals)

            vals = []
            x_append(vals, {"value": "O.S (Left)", "type": "row_head"})
            x_append(vals, {"value": self.near_left_sph.name, "type": "value"}, condition=self.lens_visible_sph)
            x_append(vals, {"value": self.near_left_cyl.name, "type": "value"}, condition=self.lens_visible_cyl)
            x_append(vals, {"value": self.near_left_axis.name, "type": "value"}, condition=self.lens_visible_axis)
            x_append(vals, {"value": self.near_left_prism.name, "type": "value"}, condition=self.lens_visible_prism)
            x_append(vals, {"value": self.near_left_add.name, "type": "value"}, condition=self.lens_visible_add)
            x_append(vals, {"value": self.near_left_va, "type": "value"}, condition=self.lens_visible_va)
            x_append(vals, {"value": self.near_left_pd, "type": "value"}, condition=self.lens_visible_pd)
            table2.append(vals)

        data = {'tables': [{"heading": heading1, "table": table1},]}
        if table2:
            data["tables"].append({"heading": heading2, "table": table2},)
        return data


