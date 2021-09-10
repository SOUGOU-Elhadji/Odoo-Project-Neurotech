# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class NeurotechPatient(models.Model):

        _inherit = 'res.partner'

        name = fields.Char(string="Type de Consultation")
        nameAll = fields.Char(string="Nom Complet")
        date = fields.Date(string="Date de naissance")
        lieu = fields.Char(string="Lieu de naissance")
        #address_patient = fields.Char(string="Adresse du patient")
        age = fields.Integer(string="Age du patient")
        assurance = fields.Many2one('neurotech.assurance', string="Assurance")
        

