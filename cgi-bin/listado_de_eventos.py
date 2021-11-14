#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi
import cgitb

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
    <link rel="stylesheet" href="../JQuery/jquery-ui-1.12.1/jquery-ui.css">
    <script src="../js/eventInfo.js"></script>
    <script src="../js/navigator.js"></script>
    <script src="../JQuery/jquery-3.6.0.js"></script>
    <script src="../JQuery/jquery-ui-1.12.1/jquery-ui.js"></script>
    <title>Listado de eventos</title>
</head>
<body class="bg" onload="generateTable()">

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

footer = """

    </table>
</div>

<div id="event-details" class="details"></div>

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
print(footer, file=utf8stdout)
