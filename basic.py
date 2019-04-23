# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 17:23:06 2019

@author: renxlc
"""

# !/usr/bin/env python3
from decimal import getcontext, Decimal

print("Float Result:", 0.1 + 0.2)
getcontext().prec = 1
print("Decimal Result:", Decimal(0.1) + Decimal(0.2))

