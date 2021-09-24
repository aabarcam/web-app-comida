let socialNetworks = 1;
/* Add up to 5 social network fields up to */
function addSocialNetwork() {
    if (socialNetworks < 5) {
        let newId = "\"red-social-warning-"+socialNetworks+"\"";
        socialNetworks++;
        document.getElementById("social-network-fields").innerHTML +=
            "<select name=\"red-social\" class=\"forml__input forml__input--stacked\" onchange=\"showIdField(this)\">\n" +
            "    <option value=\"\" disabled selected>-- seleccione una red social --</option>\n" +
            "    <option value=\"1\">Twitter</option>\n" +
            "    <option value=\"2\">Instagram</option>\n" +
            "    <option value=\"3\">Facebook</option>\n" +
            "    <option value=\"4\">TikTok</option>\n" +
            "    <option value=\"5\">Otra</option>\n" +
            "</select>\n" +
            "<input class=\"forml__input forml__input--complement\" name=\"red-id\" placeholder=\"Ingrese su ID o URL\">\n" +
            "<p class=\"forml__warning\" id="+newId+">\n" +
            "    Por favor seleccione a que red social corresponde su ID\n" +
            "</p>"
    }
    if (socialNetworks === 5) {
        document.getElementById("add-social").remove();
    }
}

function showIdField(el) {
    let fields = document.getElementsByName("red-social")
    for (const fieldsKey in fields) {
        if (el === fields[fieldsKey]) {
            document.getElementsByName("red-id")[fieldsKey].style.visibility = "visible";
        }
    }
}

function setDates() {
    let n = new Date();
    let y = n.getFullYear();
    let m = n.getMonth() + 1;
    let d = n.getDate();
    let h = n.getHours();
    let min = n.getMinutes();
    let hEnd = (h + 3)%24;
    if (m < 10) {
        m = "0"+m;
    }
    if (d < 10) {
        d = "0"+d;
    }
    if (h < 10) {
        h = "0"+h;
    }
    if (hEnd < 10) {
        hEnd = "0"+hEnd;
    }
    if (min < 10) {
        min = "0"+min;
    }
    document.getElementsByName("dia-hora-inicio")[0].value = y+"-"+m+"-"+d+","+h+":"+min;
    document.getElementsByName("dia-hora-termino")[0].value = y+"-"+m+"-"+d+","+hEnd+":"+min;
}

let tipos = ["Al Paso", "Alemana", "Árabe", "Argentina", "Asiática", "Australiana", "Brasileña", "Café y Snacks",
    "Carnes", "Casera", "Chilena", "China", "Cocina de Autor", "Comida Rápida", "Completos", "Coreana", "Cubana",
    "Española", "Exótica", "Francesa", "Gringa", "Hamburguesa", "Helados", "India", "Internacional", "Italiana",
    "Latinoamericana", "Mediterránea", "Mexicana", "Nikkei", "Parrillada", "Peruana", "Pescados y mariscos",
    "Picoteos", "Pizzas", "Pollos y Pavos", "Saludable", "Sándwiches", "Suiza", "Japonesa", "Sushi", "Tapas", "Thai",
    "Vegana", "Vegetariana"]

function addFoodTypes() {
    for (const tiposKey in tipos) {
        let tipo = tiposKey + 1;
        document.getElementsByName("tipo-comida")[0].innerHTML +=
            "<option value="+tipo+">"+tipos[tiposKey]+"</option>";
    }
}

let files = 1;
/* Add up to 5 social network fields */
function addFileField() {
    if (files < 5) {
        files++;
        document.getElementById("event-images-fields").innerHTML +=
            "<input type=\"file\" name=\"foto-comida\" class=\"forml__input input forml__input--stacked--large\">"
    }
    if (files === 5) {
        document.getElementById("add-image").remove();
    }
}

