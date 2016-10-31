#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Correcting two related data sets"""


def sum_orders(customers, orders):
   
    total = 0
    total_order = 0
    my_dict = {}

    for customer_id, key1 in customers.iteritems():
        
        for _, key2 in orders.iteritems():
            
            if customer_id == key2['customer_id']:
                total_order += 1
                total += key2['total']
                my_dict[customer_id] = {'name': key1['name'],
                                        'email': key1['email'],
                                        'orders': total_order,
                                        'total': total}

        total = 0
        total_order = 0

    return my_dict
