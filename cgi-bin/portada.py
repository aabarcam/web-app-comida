#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import database

cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

header = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../css/general.css">
    <script src="../JQuery/jquery-3.6.0.js"></script>
    <script src="../js/eventInfo.js"></script>
    <script src="../js/navigator.js"></script>
    <title>Portada</title>
</head>
<body>

<div id="title" onclick="goTo('portada.py')" class="text-button">
    HambreTengo
</div>

<div id="main-buttons" class="btn-group">
    <button class="btn-group__button" onclick="goTo('../informar_evento.html')">Informar evento</button>
    <button class="btn-group__button" onclick="goTo('listado_de_eventos.py')">Ver listado de eventos</button>
    <button class="btn-group__button" onclick="goTo('../estadisticas.html')">Estadísticas</button>
</div>

<div id="welcome-msg" class="cover">
    <p class="cover__text">
        Bienvenido a HambreTengo, la aplicación favorita que le informa
        acerca de todo tipo de eventos de venta de comida a lo largo del país
        en un solo lugar!
    </p>
</div>

<div id="last-events-msg">
    <p class="text">
        Estos son los 5 últimos eventos registrados hasta el momento:
    </p>
</div>

<div id="last-events" class="tbl">
    <table id="last-events-table">
"""

table = f"""
<tr>
    <th class="tbl__col-title">Fecha - hora inicio</th>
    <th class="tbl__col-title">Fecha - hora término</th>
    <th class="tbl__col-title">Comuna</th>
    <th class="tbl__col-title">Sector</th>
    <th class="tbl__col-title">Tipo</th>
    <th class="tbl__col-title">Foto</th>
</tr>
"""

events = database.Food("root", "")
last_5_events = events.get_last_5_events()

# last_5_events = id, dia_hora_inicio, dia_hora_termino, comuna_id, sector, descripcion, tipo


for event in last_5_events:
    comuna = events.get_comuna_name_by_id(event[3])
    foto_path = events.get_all_event_fotos(event[0])[0][0]  # primera foto
    table += f"""
    <tr>
        <th>{event[1]}</th>
        <th>{event[2]}</th>
        <th>{comuna}</th>
        <th>{event[4]}</th>
        <th>{event[6]}: {event[5]}</th>
        <th><img src="../media/{foto_path}" alt="Imagen representativa del evento" class="tbl__img"></th>
    </tr>
    """

footer = """


</table>
</div>

</body>
</html>
"""

print(header, file=utf8stdout)
print(table, file=utf8stdout)
print(footer, file=utf8stdout)
