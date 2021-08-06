from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    age = fields.Integer(string='Umur')
    isDosen = fields.Boolean(string='Apakah Dosen ?')
    kelas_id = fields.Many2one('kelas.kelas', string='Kelas')