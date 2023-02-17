from odoo import api,fields, models, _

class DaftarSekolahFormSiswa(models.Model):
    _name = "daftar.sekolah.form.siswa"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "Form Data Siswa"
    _rec_name = 'nama_siswa'

    nama_siswa = fields.Char(string="Nama Siswa")
    umur_siswa = fields.Integer(string="Umur Siswa")
    tgl_lahir_siswa = fields.Date(string="Tangal Lahir")
    jenis_kelamin_siswa = fields.Selection([
        ('laki','Laki - Laki'),
        ('perempuan','Perempuan'),
        ('ragil','Ragil Jerman'),
    ],string="Jenis Kelamin")

    related_fields = fields.Many2one('employee.data', string='Superior',index=True)
    email_data_employee = fields.Char(related='related_fields.email_employee')
    employee_organization = fields.Selection(related='related_fields.organization_employee')
    current_organization = fields.Char(string="curr organization")

    @api.onchange('employee_organization')
    def get_employee_organization(self):
        if self.employee_organization == "TECHNOLOGY":
            self.current_organization = "TECHNOLOGY"



