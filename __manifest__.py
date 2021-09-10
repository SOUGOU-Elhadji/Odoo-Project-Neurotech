# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Neurotech  Atelier',
    'version' : '1.1',
    'summary': 'Others',
    'sequence': 15,
    'description': """
Invoicing & Payments
====================
The specific and easy-to-use Invoicing system in Odoo allows you to keep track of your accounting, even when you are not an accountant. It provides an easy way to follow up on your vendors and customers.

You could use this simplified accounting in case you work with an (external) account to keep your books, and you still want to keep track of payments. This module also offers you an easy method of registering payments, without having to encode complete abstracts of account.
    """,
    'category': 'Invoicing Management',
    'website': 'https://www.odoo.com/page/billing',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : ['base', 'web'],
    'data': [
            'views/neurotech_assurance_view.xml',
            'views/neurotech_patient_view.xml',
            'views/neurotech_facture_view.xml',
            'security/ir.model.access.csv',
            'report/neurotech_invoice_report.xml'

    ],
    'demo': [
    
    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
