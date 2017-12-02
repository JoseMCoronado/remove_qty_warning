# -*- coding: utf-8 -*-

###################################################################################
#
#    Copyright (C) 2017 GFP SOLUTIONS LLC
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

{
    'name': 'Remove the Check Availability Warning on Sale',
    'category': 'Sale',
    'author': 'GFP Solutions',
    'summary': 'Custom',
    'version': '1.0',
    'description': """

THIS MODULE IS PROVIDED AS IS - INSTALLATION AT USERS' OWN RISK - AUTHOR OF MODULE DOES NOT CLAIM ANY
RESPONSIBILITY FOR ANY BEHAVIOR ONCE INSTALLED.
        """,

    'depends':['sale_stock'],
    'data':[
            'views/ir_sequence.xml',
            'views/mrp_entry_wizard_views.xml',
            'views/sale_order_views.xml',
            'views/mrp_views.xml',
            'views/sale_workorder_views.xml',
            'views/product_template_views.xml',
            'views/ir_model_access.xml',
            ],
    'installable': True,
}
