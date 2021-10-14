#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import database
import os
import filetype
import re
import validators
from datetime import datetime

cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

events = database.Food("", "root", "", "")
form = cgi.FieldStorage()

errors = ""

files_valid = True
file_obj = form['foto-comida']
if not isinstance(file_obj, list):
    file_obj = [form['foto-comida']]

# Check that all files are valid
for file_elem in file_obj:
    if file_elem.filename:
        size = os.fstat(file_elem.file.fileno()).st_size
        tipo_real = filetype.guess(file_elem.file)
        file_elem.file.seek(0, 0)
        if size > 100000 * 1000:
            files_valid = False
            errors += f"""
            <li>Tamaño de archivo {file_elem.filename} muy grande, el tamaño del archivo es de {size}, el máximo 
            permitido es de 100MB</li>
            """
        if tipo_real.mime != 'image/jpeg' and tipo_real.mime != 'image/jpg' and tipo_real.mime != 'image/png':
            files_valid = False
            errors = errors + f"""
            <li>Tipo de archivo inválido: {tipo_real.mime}. Tipos permitidos: jpg, jpeg, png</li>
            """

if files_valid:
    events.add_evento(form)

# region validation
matches_one = False
valid_regiones = events.get_regiones()
region = form["region"].value
if (region.strip(),) not in valid_regiones:
    errors += f"""
    <li>Región seleccionada inválida: {region}</li>
    """

# comuna validation
valid_comunas = events.get_comunas_of_region(region)
comuna = form["comuna"].value
if ((comuna.strip()),) not in valid_comunas:
    errors += """
    <li>Comuna seleccionada inválida</li>
    """

# sector validation
if len(form["sector"].value) > 100:
    errors += """
    <li>Sector supera el limite de caracteres (max. 100)</li>
    """

# nombre validation
largo_nombre = len(form["nombre"].value)
if largo_nombre == 0:
    errors += """
    <li>Nombre no ingresado</li>
    """
elif largo_nombre > 200:
    errors += """
    <li>Nombre ingresado supera el limite de caracteres (max. 200)</li>
    """

# email validation
email = form["email"].value
if not validators.email(email):
    errors += """
    <li>Email ingresado es inválido<li>
    """

# celular validation
celular_regex = r"""^[+]?[0-9]{9,12}\b"""
celular = form["celular"].value
if not re.fullmatch(celular_regex, celular):
    errors += """
    <li>Celular ingresado es inválido</li>
    """

# red social validation
redes = form.getlist("red-social")
ids = form.getlist("red-id")
for red in redes:
    if red not in ["twitter", "facebook", "instagram", "tiktok", "otros"]:
        errors += """
        <li>Red social no existente</li>
        """

id_regex = r"""^@?[A-Za-z\d\_\.]+$"""
url_regex = r"""^(https?://)?(www.)?[A-Za-z\d]+\.([A-Za-z\d])+/@?[A-Za-z\d\_\.]+/?$"""
for id_element in ids:
    if not re.fullmatch(id_regex, id_element) and not re.fullmatch(url_regex, id_element):
        errors += """
        <li>ID o URL de red social ingresado inválido</li>
        """

# fecha validation

fecha_inicio = form["dia-hora-inicio"].value
inicio_valid = True

try:
    inicio_valid = bool(datetime.strptime(fecha_inicio, "%Y-%m-%d %H:%M"))
except ValueError:
    inicio_valid = False

if not inicio_valid:
    errors += """
    <li>Fecha de inicio inválida, formato admitido: yyyy-mm-dd hh:mm</li>
    """

fecha_termino = form["dia-hora-termino"].value
termino_valid = True

try:
    termino_valid = bool(datetime.strptime(fecha_termino, "%Y-%m-%d %H:%M"))
except ValueError:
    termino_valid = False

if not termino_valid:
    errors += """
    <li>Fecha de término inválida, formato admitido: yyyy-mm-dd hh:mm</li>
    """

# tipo validation
valid_tipos = ["Al Paso", "Alemana", "Árabe", "Argentina", "Asiática", "Australiana", "Brasileña", "Café y Snacks",
               "Carnes", "Casera", "Chilena", "China", "Cocina de Autor", "Comida Rápida", "Completos", "Coreana",
               "Cubana", "Española", "Exótica", "Francesa", "Gringa", "Hamburguesa", "Helados", "India",
               "Internacional", "Italiana", "Latinoamericana", "Mediterránea", "Mexicana", "Nikkei", "Parrillada",
               "Peruana", "Pescados y mariscos", "Picoteos", "Pizzas", "Pollos y Pavos", "Saludable", "Sándwiches",
               "Suiza", "Japonesa", "Sushi", "Tapas", "Thai", "Vegana", "Vegetariana"]
tipo = form["tipo-comida"].value
if tipo not in valid_tipos:
    errors += """
    <li>Tipo de comida ingresado inválido
    """

header = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../css/general.css">
    <script src="../JQuery/jquery-3.6.0.js"></script>
    <script src="../js/navigator.js"></script>
    <title>Portada</title>
</head>
<body onload="generateLastEventsTable();">

<div id="title" onclick="goTo('portada.py')" class="text-button">
    HambreTengo
</div>

<div id="main-buttons" class="btn-group">
    <button class="btn-group__button" onclick="goTo('../informar_evento.html')">Informar evento</button>
    <button class="btn-group__button" onclick="goTo('listado_de_eventos.py')">Ver listado de eventos</button>
    <button class="btn-group__button" onclick="goTo('../estadisticas.html')">Estadísticas</button>
</div>

<div id='success-msg'>
    <p>Su información ha sido recibida</p>
</div>
<ul>
"""

print(header, file=utf8stdout)
print(errors, file=utf8stdout)
print("</ul>", file=utf8stdout)
