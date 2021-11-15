#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import database
import os
import filetype
import re
import math
from datetime import datetime

cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

events = database.Food("root", "")
form = cgi.FieldStorage()

succ_msg = """<p id='success-msg'>Su información ha sido recibida</p>"""

err_msg = """<p id='error-msg'>Ha ocurrido un error con el envío de la información, por favor haga click en 'Volver' 
para regresar al formulario y reenviarlo</p>"""

errors = False

file_obj = form['foto-comida']
if not isinstance(file_obj, list):
    file_obj = [form['foto-comida']]

# Check that all files are valid
for file_elem in file_obj:
    if file_elem.filename:
        size = os.fstat(file_elem.file.fileno()).st_size
        tipo_real = filetype.guess(file_elem.file)
        file_elem.file.seek(0, 0)
        if size > 100 * 1000 * 1000:  # 100MB
            errors = True
            err_msg += f"""
            <p>Tamaño de archivo {file_elem.filename} muy grande, el tamaño del archivo es de 
            {math.ceil(size / 1000) / 1000}MB, el máximo  permitido es de 100MB</p>
            """
        if tipo_real.mime != 'image/jpeg' and tipo_real.mime != 'image/jpg' and tipo_real.mime != 'image/png':
            errors = True

# region validation
valid_regiones = events.get_regiones()
region = form["region"].value
if (region.strip(),) not in valid_regiones:
    errors = True

# comuna validation
valid_comunas = events.get_comunas_of_region(region)
comuna = form["comuna"].value
if ((comuna.strip()),) not in valid_comunas:
    errors = True

# sector validation
if len(form["sector"].value) > 100:
    errors = True

# nombre validation
nombre = form["nombre"].value.strip()
nombre_regex = r"""^\s?[A-Za-z\-á-ú]+[A-Za-z\-\sá-úä-ü]*$"""
if not re.fullmatch(nombre_regex, nombre):
    errors = True

elif len(nombre) > 200:
    errors = True

# email validation
email = form["email"].value
email_regex = r"""^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$"""
if not re.fullmatch(email_regex, email):
    errors = True

# celular validation
celular_regex = r"""^[+]?[0-9]{9,12}\b"""
celular = form["celular"].value
if not re.fullmatch(celular_regex, celular) and celular != "":
    errors = True

# red social validation
redes = form.getlist("red-social")
ids = form.getlist("red-id")
for red in redes:
    if red not in ["twitter", "facebook", "instagram", "tiktok", "otra"]:
        errors = True

id_regex = r"""^@?[A-Za-z\d\_\.]+$"""
url_regex = r"""^(https?://)?(www.)?[A-Za-z\d]+\.([A-Za-z\d])+/@?[A-Za-z\d\_\.]+/?$"""
for id_element in ids:
    if id_element == "":
        continue
    if not re.fullmatch(id_regex, id_element) and not re.fullmatch(url_regex, id_element):
        errors = True

# fecha validation

fecha_inicio = form["dia-hora-inicio"].value
inicio_valid = True

try:
    inicio_valid = bool(datetime.strptime(fecha_inicio, "%Y-%m-%d %H:%M"))
except ValueError:
    inicio_valid = False

if not inicio_valid:
    errors = True

fecha_termino = form["dia-hora-termino"].value
termino_valid = True

try:
    termino_valid = bool(datetime.strptime(fecha_termino, "%Y-%m-%d %H:%M"))
except ValueError:
    termino_valid = False

if not termino_valid:
    errors = True

# tipo validation
valid_tipos = ["Al Paso", "Alemana", "Árabe", "Argentina", "Asiática", "Australiana", "Brasileña", "Café y Snacks",
               "Carnes", "Casera", "Chilena", "China", "Cocina de Autor", "Comida Rápida", "Completos", "Coreana",
               "Cubana", "Española", "Exótica", "Francesa", "Gringa", "Hamburguesa", "Helados", "India",
               "Internacional", "Italiana", "Latinoamericana", "Mediterránea", "Mexicana", "Nikkei", "Parrillada",
               "Peruana", "Pescados y mariscos", "Picoteos", "Pizzas", "Pollos y Pavos", "Saludable", "Sándwiches",
               "Suiza", "Japonesa", "Sushi", "Tapas", "Thai", "Vegana", "Vegetariana"]
tipo = form["tipo-comida"].value
if tipo not in valid_tipos:
    errors = True

if not errors:
    events.add_evento(form)

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
<body class='bg' onload="generateLastEventsTable();">

<div id="title" onclick="goTo('portada.py')" class="text-button">
    HambreTengo
</div>

<div id="main-buttons" class="btn-group">
    <button class="btn-group__button" onclick="goTo('../informar_evento.html')">Informar evento</button>
    <button class="btn-group__button" onclick="goTo('listado_de_eventos.py')">Ver listado de eventos</button>
    <button class="btn-group__button" onclick="goTo('../estadisticas.html')">Estadísticas</button>
</div>
"""

success = """
<div id="back-to-portada" onclick="goTo('portada.py')" class="text-button text-button--small">
    Volver a la portada
</div>
"""

return_to_form = """
<div id="back" onclick="goBack()" class="text-button text-button--small">
    Volver
</div>
"""

footer = """
</body>
</html>
"""

print(header, file=utf8stdout)

if errors:
    print(err_msg, file=utf8stdout)
    print(return_to_form, file=utf8stdout)
else:
    print(succ_msg, file=utf8stdout)
    print(success, file=utf8stdout)

print(footer, file=utf8stdout)
