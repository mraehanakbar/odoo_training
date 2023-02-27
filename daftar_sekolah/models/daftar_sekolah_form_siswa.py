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


    def get_data_email_login(self):
        try:
            search_data = self.env['employee.data'].search([('email_employee', '=', self.env.user.login)])
            position = search_data.mapped('organization_employee')[0]
            return position
        except:
            position = ''
            return position

    related_fields = fields.Many2one('employee.data', string='Superior',index=True)
    login_users = fields.Many2one('res.users', string='Name', index=True, tracking =2, default=lambda self: self.env.user) 
    departement_employee = fields.Char(string="departement employee", default= get_data_email_login, readonly=True)
    email_data_employee = fields.Char(related='related_fields.email_employee')
    employee_organization = fields.Selection(related='related_fields.organization_employee')
    current_organization = fields.Char(string="curr organization")

    @api.onchange('employee_organization')
    def get_employee_organization(self):
        if self.employee_organization == "TECHNOLOGY":
            self.current_organization = "TECHNOLOGY"



