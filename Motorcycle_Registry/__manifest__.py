{
    'name': 'Motorcycle Registry',
    'summary': """Manage Registration of Motorcycles""",
    'description': """Motorcycle Registry
    ====================
    This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.
    """,
    'license': 'OPL-1',
    'author': 'visv-odoo',
    'website': 'https://github.com/visv-odoo/Training-Exerisise-motorbike-odoo.git',
    'category': 'Kawiil',
    'depends': ['base'],
    'data': [
        'security/registry_groups.xml',
        'security/ir.model.access.csv',
        'security/registry_security.xml',
        'data/motorcycle_registry_data.xml',
        'views/motorcycle_registry_menuitems.xml',
        'views/registry_views.xml',
    ],
    'demo': [
        'demo/registrationDemo.xml',
    ],
    'application': True,
}