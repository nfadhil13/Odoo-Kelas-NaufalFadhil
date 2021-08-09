from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    tanggal_lahir = fields.Date(string="Tanggal Lahir")
    age = fields.Integer(
        string='Umur',
        compute='_compute_age',
        store= False,
        )
    isDosen = fields.Boolean(string='Apakah Dosen ?')
    kelas_id = fields.Many2one('kelas.kelas', string='Kelas')
    ijazah = fields.Binary(string='Ijazah')


    @api.constrains('tanggal_lahir')
    def _check_tanggal_lahir(self):
        for res_partner in self:
            tanggal_lahir = res_partner.tanggal_lahir
            if tanggal_lahir and tanggal_lahir > fields.Date.today() :
                raise models.ValidationError(
                    'Tanggal lahir harus sebelum hari ini!'
                ) 

    @api.depends('tanggal_lahir')
    def _compute_age(self):
        today = fields.Date.today()
        for res_partner in self:
            if res_partner.tanggal_lahir:
                delta = today - res_partner.tanggal_lahir
                res_partner.age = int (delta.days / 365)
            else:
                res_partner.age = 0