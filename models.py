from odoo import models,fields

class Indice(models.Model):
    _name = "jc.indice"

    name = fields.Char("Asignación")
    status = fields.Selection(selection=[("pendiente","Pendiente"),("hecho","Hecho")])