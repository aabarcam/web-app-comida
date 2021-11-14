#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgitb
import database
import validators
from datetime import datetime

cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

events = database.Food("", "root", "", "")

x = events.get_regiones()
"""
print(x, file = utf8stdout)
print("<br>", file=utf8stdout)
print(str(type(x)), file=utf8stdout)
print("<br>", file=utf8stdout)
print(('Región de Antofagasta',), file=utf8stdout)
print("<br>", file=utf8stdout)
print(('Región de Antofagasta',) in x, file=utf8stdout)
"""
"""
email = "aabarcam@gmail.com"

fecha = "2021-10-12 20:04:00"
print(fecha, file=utf8stdout)
print("<br>", file=utf8stdout)


try:
    res = bool(datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S"))
except ValueError:
    res = False

print("<br>", file=utf8stdout)
print(res, file=utf8stdout)
"""

reg = []
for tup in x:
    reg += tup
    print(tup[0], "<br>", file=utf8stdout)

print(reg, file=utf8stdout)
print("<br>", file=utf8stdout)
# print(x, file=utf8stdout)
