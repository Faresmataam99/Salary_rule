# -*- coding: utf-8 -*-
{
    'name': "SIBIC - Règles salariales - Algérienne",
    'summary': """ Intégration des règles salariales de la paie en fonction des réglementations algérienne """,
    'description': """ Ce module contient les règles salariales (avec les structures et les catégorris recpectivement) de la paie en fonction des réglementations algérienne """,

    'version'       : "17.0",
    'category'      : "Human Resources/Employees",
    
    'sequence': 1,
    
    'company'       : 'SIBIC',
    'author'        : 'SIBIC',
    'maintainer'    : 'SIBIC',

    'website': "https://www.sibic.dz/",
    'support' : "contact@sibic.dz",


    'depends': [
        'base',
        'sibic_hr_dz',
        'hr_payroll'
        #'sibic_hr_payroll_dz',
    ],

    'data':[
        'data/hr_payroll_leave_type.xml',
        'data/hr_payroll_category.xml',
        'data/hr_payroll_salary_rule.xml',
        'data/hr_payroll_structure.xml',
        'data/hr_payroll_entry_type.xml',
        'data/hr.payslip.input.type.csv',
    ],
    
    'license'       : 'LGPL-3',
    
    'installable': True,
    'auto_install': False,
    'application': True,
}
