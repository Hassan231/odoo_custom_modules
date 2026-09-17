from odoo import models, fields

class Machine(models.Model):
    _name = 'machine.tracker'
    _description = 'Industrial Machine'

    name = fields.Char(string='Machine Name', required=True)
    location = fields.Char(string='Location')
    status = fields.Selection([
        ('running', 'Running'),
        ('idle', 'Idle'),
        ('maintenance', 'Under Maintenance'),
    ], default='idle', string='Status')