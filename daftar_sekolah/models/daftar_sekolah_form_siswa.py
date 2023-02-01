from odoo import api,fields, models, _

class DaftarSekolahFormSiswa(models.Model):
    _name = "daftar.sekolah.form.siswa"
    _description = "Form Data Siswa"

    nama_siswa = fields.Char(string="Nama Siswa")
    umur_siswa = fields.Integer(string="Umur Siswa")
    tgl_lahir_siswa = fields.Date(string="Tangal Lahir")
    jenis_kelamin_siswa = fields.Selection([
        ('laki','Laki - Laki'),
        ('perempuan','Perempuan'),
        ('ragil','Ragil Jerman'),
    ],string="Jenis Kelamin")