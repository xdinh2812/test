from odoo import models, fields


class Student(models.Model):
    _name = 'student'
    _description = 'Student Information'

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
