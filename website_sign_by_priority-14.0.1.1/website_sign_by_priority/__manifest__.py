# -*- encoding: utf-8 -*-
{
    'name': "Website Sign Sending By Priority",
    'version': '14.0.1.1',
    'summary': 'Add Sequence/Priority for sending signature request one by one to each Signer.',
    'category': 'Document Management',
    'website': 'https://apps.odoo.com/apps/modules/14.0/website_sign_by_priority/',
    'description': """
eSign for Odoo, paperless work odoo, Website sign Odoo, odoo digital sign, Web Digital Signature, How Digital Signature work in odoo, Odoo Sign Demonstration, web sign, Sign, Odoo Digital Signature, Digital Signature works, Electronic Signatures, Odoo Sign Demonstration, Digital Signature in Odoo, Electronic signature in Odoo, How Digital Signature works in Odoo, Digital Signature Widget, Odoo POS Signature, Email signature, How to add digital signature, Odoo eSign, Contract Digitized Signature, Web Widget Digitized Signature, Web Digitized Signature, sign by priority, signature in sequence, autograph, sign documents online, how to sign a document online, free document signing, signature app, e signature, create signature online, document sign, eSignature, customer sign, document signature, contract signature, contract sign, odoo sign, document management, document version, simple signature, documents, knowledge, manage document, amazon, quality management, employee document, online signature, account document, pdf export, excel export
    """,
    "live_test_url": "https://odoo.sheliyainfotech.com/contactus?description=demo:website_sign_by_priority&odoo_version=14.0",
    'author': 'Nilesh Sheliya',
    "depends" : ['sign'],
    'data': [
             'security/ir.model.access.csv',
             'views/template.xml',
             'wizard/send_sign_request_view.xml',
             'wizard/saign_send_seq_dialog.xml',
             ],
    "price": 39.00,
    "currency": "EUR",
    'license': 'OPL-1',
    'maintainer': 'Nilesh Sheliya<sheliyanilesh@gmail.com>',
    'support': 'sheliyanilesh@gmail.com',
    "images": ["static/description/hirerchy.png"],
    
    'qweb': [
           
            ],  
    
    'installable': True,
    'application'   : True,
    'auto_install'  : False,
}
