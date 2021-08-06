from odoo import models, fields, api

class MataKuliah(models.Model):
    _name = 'mata.kuliah'

    name = fields.Char(string='Nama Mata Kuliah')
    kode = fields.Char(string='Kode Matkul')
    kelas_ids =  fields.Many2many(
        comodel_name='kelas.kelas', 
        string='Kelas'
    )
    partner_id = fields.Many2one(
        'res.partner', string='Dosen Pengampu', domain=[("isDosen", "=", True)])

    