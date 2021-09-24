let events = {
    "events": [
        {
            "fechaInicio": "2022-01-22",
            "horaInicio": "09:00",
            "fechaTermino": "2022-01-22",
            "horaTermino": "13:00",
            "region": "Santiago",
            "comuna": "Santiago",
            "sector": "Parque O'Higgins",
            "tipoComida": "Chilena",
            "descripcion": "Empanadas de pino, queso, helado, camarón, manzana",
            "contacto": {
                "nombre": "Juan Perez",
                "email": "juan.perez@hotmail.com",
                "celular": "+56912899821",
                "redes": [
                    {
                        "red": "Twitter",
                        "id": "jperez"
                    }
                ]
            },
            "fotos": [
                {
                    "path": "img/empanada.jpg",
                    "alt": "Empanadas de horno en una fuente"
                },
                {
                    "path": "img/empanada-2.jpg",
                    "alt": "Cesta con empanadas"
                }
            ]
        },
        {
            "fechaInicio": "2022-01-21",
            "horaInicio": "10:00",
            "fechaTermino": "2022-01-21",
            "horaTermino": "16:00",
            "region": "Santiago",
            "comuna": "La Cisterna",
            "sector": "Metro La Cisterna",
            "tipoComida": "Completos",
            "descripcion": "italiano y variedes, sushipleto, de chocolate",
            "contacto": {
                "nombre": "Sandra Santibañez",
                "email": "ssan@gmail.com",
                "celular": "",
                "redes": [
                    {
                        "red": "Twitter",
                        "id": "sansan"
                    },
                    {
                        "red": "Tiktok",
                        "id": "sand123"
                    }
                ]
            },
            "fotos": [
                {
                    "path": "img/completo.jpg",
                    "alt": "Completos con papas fritas y bebidas en lata"
                }
            ]
        },
        {
            "fechaInicio": "2022-01-19",
            "horaInicio": "07:00",
            "fechaTermino": "2022-01-19",
            "horaTermino": "11:00",
            "region": "Santiago",
            "comuna": "San Bernardo",
            "sector": "Plaza",
            "tipoComida": "Café y Snacks",
            "descripcion": "todo tipo de café y variedad de postres",
            "contacto": {
                "nombre": "Sebastián Morales",
                "email": "sebam@hotmail.cl",
                "celular": "+56912345678",
                "redes": []
            },
            "fotos": [
                {
                    "path": "img/cafe.jpg",
                    "alt": "Mesa con dos tazas de café y una galleta"
                },
                {
                    "path": "img/cafe-2.jpg",
                    "alt": "Taza de café con leche"
                },
                {
                    "path": "img/cafe-3.jpg",
                    "alt": "Taza de café y plato con croissants"
                }
            ]
        },
        {
            "fechaInicio": "2022-01-18",
            "horaInicio": "12:00",
            "fechaTermino": "2022-01-18",
            "horaTermino": "18:00",
            "region": "Antofagasta",
            "comuna": "Antofagasta",
            "sector": "Plaza Colón",
            "tipoComida": "Pescados y mariscos",
            "descripcion": "frito, ceviche, pingüino, helado de pescado",
            "contacto": {
                "nombre": "Jorge Muñoz",
                "email": "jmnz@hotmail.cl",
                "celular": "+56912344321",
                "redes": [
                    {
                        "red": "Facebook",
                        "id": "jorge-munoz"
                    }
                ]
            },
            "fotos": [
                {
                    "path": "img/pescado-frito.jpg",
                    "alt": "Trozos de pescado frito, un limón y salsa"
                }
            ]
        },
        {
            "fechaInicio": "2022-01-15",
            "horaInicio": "16:00",
            "fechaTermino": "2022-01-15",
            "horaTermino": "21:00",
            "region": "Santiago",
            "comuna": "Ñuñoa",
            "sector": "Estadio Nacional",
            "tipoComida": "Helados",
            "descripcion": "caseros, de agua, de crema, de pescado",
            "contacto": {
                "nombre": "Donaldo Toledo",
                "email": "dontoledo@hotmail.cl",
                "celular": "",
                "redes": [
                    {
                        "red": "Instagram",
                        "id": "don.tol1"
                    }
                ]
            },
            "fotos": [
                {
                    "path": "img/helado.jpg",
                    "alt": "Multiples sabores de helado de crema"
                }
            ]
        }
    ]
};

let ev = events["events"];

function generateTable() {
    for (const eventKey in ev) {
        document.getElementById("all-events-table").innerHTML +=
            "<tr id=\"info-row-" + eventKey + "\" onclick=\"generateDetails(this)\">\n" +
            "    <th>" + ev[eventKey]["fechaInicio"] + "<br>" + ev[eventKey]["horaInicio"] + "</th>\n" +
            "    <th>" + ev[eventKey]["fechaTermino"] + "<br>" + ev[eventKey]["horaInicio"] + "</th>\n" +
            "    <th>" + ev[eventKey]["comuna"] + "</th>\n" +
            "    <th>" + ev[eventKey]["sector"] + "</th>\n" +
            "    <th>" + ev[eventKey]["tipoComida"] + ": " + ev[eventKey]["descripcion"] + "</th>\n" +
            "    <th>" + ev[eventKey]["contacto"]["nombre"] + "</th>\n" +
            "    <th>" + ev[eventKey]["fotos"].length + "</th>\n" +
            "</tr>";
    }
}

function generateLastEventsTable() {
    for (const eventKey in ev) {
        document.getElementById("last-events-table").innerHTML +=
            "<tr>\n" +
            "    <th>" + ev[eventKey]["fechaInicio"] + "<br>" + ev[eventKey]["horaInicio"] + "</th>\n" +
            "    <th>" + ev[eventKey]["fechaTermino"] + "<br>" + ev[eventKey]["horaInicio"] + "</th>\n" +
            "    <th>" + ev[eventKey]["comuna"] + "</th>\n" +
            "    <th>" + ev[eventKey]["sector"] + "</th>\n" +
            "    <th>" + ev[eventKey]["tipoComida"] + ": " + ev[eventKey]["descripcion"] + "</th>\n" +
            "    <th>" + "<img src=\"" + ev[eventKey]["fotos"][0]["path"] + "\" alt=\"" + ev[eventKey]["fotos"][0]["alt"] + "\" class=\"tbl__img\" >" + "</th>\n" +
            "</tr>";
    }
}

function generateDetails(el) {
    document.getElementsByClassName("bg")[0].style.height = "auto";
    for (const eventsKey in ev) {
        let currId = "info-row-" + eventsKey;
        if (el === document.getElementById(currId)) {
            writeDetails(eventsKey);
        }
    }

}

function writeDetails(key) {
    let redesBlock = "";
    let redes = ev[key]["contacto"]["redes"];
    let fotosBlock = "";
    let fotos = ev[key]["fotos"];
    for (const redesKey in redes) {
        redesBlock += "<div class=\"details__list\">" + redes[redesKey]["red"] + ": " + redes[redesKey]["id"] + "</div>\n";
    }
    for (const fotosKey in fotos) {
        fotosBlock += "<span class=\"details__list\">" +
            "<img class=\"tbl__img--std-size\" " +
            "src=\"" + fotos[fotosKey]["path"] + "\"" +
            "alt=\"" + fotos[fotosKey]["alt"] + "\"" +
            "onclick=\"popUpImage('"+fotos[fotosKey]["path"]+"','"+fotos[fotosKey]["alt"]+"')\">" +
            "</span>";
    }
    document.getElementById("event-details").style.display = "block";
    document.getElementById("event-details").innerHTML =
        "<p><span>Región: </span>" + ev[key]["region"] + "</p>\n" +
        "<p><span>Comuna: </span>" + ev[key]["comuna"] + "</p>\n" +
        "<p><span>Sector: </span>" + ev[key]["sector"] + "</p>\n" +
        "<p><span>Nombre: </span>" + ev[key]["contacto"]["nombre"] + "</p>\n" +
        "<p><span>E-mail: </span>" + ev[key]["contacto"]["email"] + "</p>\n" +
        "<p><span>Celular: </span>" + ev[key]["contacto"]["celular"] + "</p>\n" +
        "<p>Redes sociales:</p>\n" + redesBlock +
        "<p><span>Fecha inicio: </span>" + ev[key]["fechaInicio"] + "</p>\n" +
        "<p><span>Hora inicio: </span>" + ev[key]["horaInicio"] + "</p>\n" +
        "<p><span>Fecha termino: </span>" + ev[key]["fechaTermino"] + "</p>\n" +
        "<p><span>Hora termino: </span>" + ev[key]["horaTermino"] + "</p>\n" +
        "<p><span>Tipo: </span>" + ev[key]["tipoComida"] + "</p>\n" +
        "<p><span>Descripcion: </span>" + ev[key]["descripcion"] + "</p>\n" +
        "<p>Fotos:</p>\n" + fotosBlock;
}

function popUpImage(imgPath, imgAlt) {
    $("#pop-up-img").attr("display", "initial");
    $("#pop-up-img p").html("" +
        "<img class=\"pop-up__img\" " +
        "src="+imgPath+
        " alt=\""+imgAlt+"\">");
    $(function () {
        $("#pop-up-img").dialog({
            draggable: false,
            resizable: false,
            height: "auto",
            width: "auto",
            modal: true,
            buttons: {
                "Cerrar": function () {
                    $(this).dialog("close");
                }
            }
        });
    });
}