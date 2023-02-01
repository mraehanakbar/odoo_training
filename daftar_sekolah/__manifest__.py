{
    'name' : 'Daftar Sekolah',
    'version' : '1.0',
    'summary':'',
    'sequence':1,
    'description':""" Buat Daftar Sekolah """,
    'category':'Productivity',
    'website':'',
    'license': 'LGPL-3',
    'depends':[
        'sale',
        'mail',
        'website_slides',
        'board'

    ],

    'data':[
        'views/daftar_sekolah_form_siswa.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'demo':[],
    'qweb':[],
    'installable':True,
    'application':True,
    'auto_install':False,
}