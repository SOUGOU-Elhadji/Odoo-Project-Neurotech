# -*- coding: utf-8 -*-


from odoo import api, fields, models, _

class NeurotechInvoice(models.Model):

            _name = 'neurotech.patient.invoice'

            patient_id = fields.Many2one('res.partner', string="Patient")
            date = fields.Date(string="Date de Facturation")
            telephone = fields.Integer(string="Téléphone du patient")
            email = fields.Char(string="Adresse E-mail")
            address_patient = fields.Char(string="Adresse du patient")
            amount_assurance = fields.Float(string="Montant assuré", compute='_get_amount_assurance')
            amount_invoice = fields.Float(string="Montant total", compute='_get_invoice')
            product_invoice_ids = fields.One2many('neurotech.product.invoice', 'invoice_id', string='Lignes de facture')


            # @api.one
            @api.depends('product_invoice_ids')
            def _get_invoice(self):

                self.amount_invoice = sum(line.amount for line in self.product_invoice_ids)

            # @api.one
            @api.depends('patient_id', 'amount_invoice')
            def _get_amount_assurance(self):
                self.amount_assurance = 0
                if self.patient_id and self.amount_invoice:
                    self.amount_assurance = self.patient_id.assurance.reduction * float(self.amount_invoice) / 100


class NeurotechProductInvoice(models.Model):
            _name = 'neurotech.product.invoice'

            name = fields.Char(string='Produit')
            price = fields.Float(string='Prix unitaire')
            qty = fields.Integer(string='Quantité')
            amount = fields.Float(string='Montant', compute='_get_amount')
            invoice_id = fields.Many2one('neurotech.patient.invoice', string='Facture')

            # @api.one
            @api.depends('price', 'qty')
            def _get_amount(self):
                self.amount = 0
                if self.price and self.qty:
                    self.amount = self.price * self.qty





