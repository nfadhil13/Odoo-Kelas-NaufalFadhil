from odoo import models, fields, api

class KelasKelas(models.Model):
    _name = 'kelas.kelas'

    name = fields.Char(string='Nama Kelas')
    partner_id =  fields.One2many(
        comodel_name='res.partner',
        inverse_name='kelas_id',
        string='Anggota Kelas',
    )
    wali_kelas   = fields.Many2one('res.partner', string='Wali Kelas', domain=[("isDosen", "=", True)])
    nama_wali_kelas = fields.Char(
        string = "Wali Kelas",
        related = "wali_kelas.name",
        readonly=True
    )
    matkul_ids = fields.Many2many(
        comodel_name='mata.kuliah', 
        string='Mata Kuliah'
    )
    