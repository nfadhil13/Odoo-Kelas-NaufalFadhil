# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class latihan_fadhil(models.Model):
#     _name = 'latihan_fadhil.latihan_fadhil'
#     _description = 'latihan_fadhil.latihan_fadhil'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
