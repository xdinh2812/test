# __manifest__.py
{
    'name': 'Student Management',
    'version': '1.0',
    'summary': 'Module for managing students',
    'author': 'Cao X',
    'category': 'Education',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        #'security/ir.model.access.csv',
        'views/student_view.xml',
    ],
    'installable': True,
    'application': True,
}
