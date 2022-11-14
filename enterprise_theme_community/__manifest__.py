{
    'name': 'Enterprise Theme (Community)',
    'version': '16.0.1.0',
    'website': 'https://github.com/ruiznorlan/web',
    'category': 'Hidden',
    'sequence': 45,
    'summary': 'This module allows you to customize Odoo community like the enterprise edition',
    'depends': [
        'web'
    ],
    'assets': {
        'web._assets_primary_variables': [
            '/enterprise_theme_community/static/src/scss/primary_variables.scss',
        ],
        'web.assets_backend': [
            '/enterprise_theme_community/static/src/scss/enterprise_theme.scss',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
    'author': 'Norlan Ruiz',
}
