# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class NeurotechAssurance(models.Model):

    _name = 'neurotech.assurance'

    name = fields.Char(string="Nom de l'assurance")
    address = fields.Char(string="Adresse")
    date = fields.Date(string="Date de création")
    reduction = fields.Float(string="Taux de réduction")