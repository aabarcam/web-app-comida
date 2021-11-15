#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb
import html

import database

cgitb.enable()

print('Content-type: text/html; charset=UTF-8')
print('')

utf8stdout = open(1, 'w', encoding='utf-8', closefd=False)

events = database.Food("root", "")
all_events = events.get_all_events()

header = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="../css/general.css">
    <link rel="stylesheet" href="../JQuery/jquery-ui-1.12.1/jquery-ui.css">
    <script src="../js/eventInfo.js"></script>
    <script src="../js/navigator.js"></script>
    <script src="../JQuery/jquery-3.6.0.js"></script>
    <script src="../JQuery/jquery-ui-1.12.1/jquery-ui.js"></script>
    <title>Listado de eventos</title>
</head>
<body class="bg" onload='displayPage(0, {len(all_events)})'>

<div id="title" onclick="goTo('portada.py')" class="text-button">
    HambreTengo
</div>

<div id="all-events" class="tbl">
    <table id="all-events-table">
"""

table = f"""
<tr>
    <th class="tbl__col-title">Fecha - hora inicio</th>
    <th class="tbl__col-title">Fecha - hora término</th>
    <th class="tbl__col-title">Comuna</th>
    <th class="tbl__col-title">Sector</th>
    <th class="tbl__col-title">Tipo comida</th>
    <th class="tbl__col-title">Nombre contacto</th>
    <th class="tbl__col-title">Total fotos</th>
</tr>
"""

all_info = f"""
<!-- end of "all-events" div -->
</table>
</div>

<!-- page buttons -->
<div class='centered-buttons'>
    <span id="prev" onclick="displayPage(-1, {len(all_events)})" class="text-button text-button--small">
        Pagina anterior
    </span>
    <span id="next" onclick="displayPage(1, {len(all_events)})" class="text-button text-button--small">
        Pagina siguiente
    </span>
</div>

<div id="event-details" class="details">
"""

# all_events = id, comuna_id, sector, nombre, email, celular, dia_hora_inicio, dia_hora_termino, descripcion, tipo

for eventKey in range(len(all_events)):
    # datos
    event_id = all_events[eventKey][0]
    comuna_id = all_events[eventKey][1]
    comuna = events.get_comuna_name_by_id(comuna_id)
    sector = all_events[eventKey][2]
    nombre = all_events[eventKey][3]
    email = all_events[eventKey][4]
    celular = all_events[eventKey][5]
    inicio = all_events[eventKey][6]
    termino = all_events[eventKey][7]
    descripcion = all_events[eventKey][8]
    tipo = all_events[eventKey][9]
    fotos = events.get_all_event_fotos(event_id)
    region_id = events.get_region_id_by_comuna_id(comuna_id)
    region = events.get_region_by_id(region_id)
    redes = events.get_all_event_redes(event_id)
    table += f"""
    <tr id="event-{eventKey}" class="hidden" onclick="displayDetails({eventKey} , {len(all_events)})">
        <th>{inicio}</th>
        <th>{termino}</th>
        <th>{comuna}</th>
        <th>{sector}</th>
        <th>{tipo}: {descripcion}</th>
        <th>{nombre}</th>
        <th>{len(fotos)}</th>
    </tr>
    """

    all_info += f"""
    <div id="info-{eventKey}" class="hidden">
        <p><span>Región: </span>{region}</p>
        <p><span>Comuna: </span>{comuna}</p>
        <p><span>Sector: </span>{sector}</p>
        <p><span>Nombre: </span>{nombre}</p>
        <p><span>Email: </span>{email}</p>
        <p><span>Celular: </span>{celular}</p>
        <p>Redes sociales:</p>
    """

    for red in redes:
        all_info += f"""
        <div class="details__list">{red[0]}: {red[1]}</div>
        """

    all_info += f"""
    <p><span>Fecha y hora inicio: </span>{inicio}</p>
    <p><span>Fecha y hora termino: </span>{termino}</p>
    <p><span>Tipo: </span>{tipo}</p>
    <p><span>Descripción: </span>{html.escape(descripcion)}</p>
    <p>Fotos: </p><span class="details__list">
    """

    for foto in fotos:
        all_info += f"""
        <img class="tbl__img--std-size" 
        src="../media/{foto[0]}" 
        alt="Evento: {descripcion}" 
        onclick="popUpImage('{foto[0]}', 'Evento: {descripcion}')">
        """

    all_info += "</span></div>"
footer = """
<!-- end of "event-details" div -->
</div>

<div id="pop-up-img" title="Imagen" class="pop-up">
    <p></p>
</div>

<div id="back" onclick="goTo('portada.py')" class="text-button text-button--small">
    Volver a la portada
</div>

</body>
</html>
"""

print(header, file=utf8stdout)
print(table, file=utf8stdout)
print(all_info, file=utf8stdout)
print(footer, file=utf8stdout)
