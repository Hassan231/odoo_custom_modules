from odoo import models, fields
class SalesOrder(models.Model):
   _inherit = 'sale.order'

   delivery_priority = fields.Selection([
       ('normal','Normal'),
       ('urgent','Urgent'),
       ('datewise','Datewise'),
   ],string='Delivery Priority',default='normal')



