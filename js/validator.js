function validate() {
    hideWarnings();
    let errors = 0;

    // region validation
    let region = document.getElementsByName("region")[0].value;
    if (region === "") {
        errors++;
        document.getElementById("region-warning").style.visibility = "visible";
    }

    // comuna validation
    let comuna = document.getElementsByName("comuna")[0].value;
    if (comuna === "") {
        errors++;
        document.getElementById("comuna-warning").style.visibility = "visible";
    }

    // sector validation
    let sector = document.getElementsByName("sector")[0].value;
    if (sector.length > 100) {
        errors++;
        document.getElementById("sector-warning").style.visibility = "visible";
    }

    // nombre validation
    let nombre = document.getElementsByName("nombre")[0].value;
    if (nombre === "" || nombre.length > 200) {
        errors++;
        document.getElementById("nombre-warning").style.visibility = "visible";
    }

    // email validation
    let email = document.getElementsByName("email")[0].value;
    let emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (!emailRegex.test(email)) {
        errors++;
        document.getElementById("email-warning").style.visibility = "visible";
    }

    // celular validation
    let celular = document.getElementsByName("celular")[0].value;
    let celularRegex = /^[+]?[0-9]{10,12}/;
    if (!celularRegex.test(celular) && celular !== "") {
        errors++;
        document.getElementById("celular-warning").style.visibility = "visible";
    }

    // red social validation
    let redes = document.getElementsByName("red-social");
    let ids = document.getElementsByName("red-id");
    let blankRegex = /^\s*$/;
    if (redes.length > 5) {
        errors++;
        document.getElementById("red-social-warning").style.visibility = "visible";
    }
    for (const redesKey in redes) {
        let red = redes[redesKey].value;
        let id = ids[redesKey].value;
        if (!blankRegex.test(id) && red === "") {
            let warningId = "red-social-warning-"+redesKey;
            errors++;
            document.getElementById(warningId).style.visibility = "visible";
        }
    }

    // fecha validation
    let fechaRegex = /^\d{4}-\d{2}-\d{2},(2[0-3]|[01]\d):[0-5]\d$/;
    let fechaI = document.getElementsByName("dia-hora-inicio")[0].value;
    if (!fechaRegex.test(fechaI)) {
        errors++;
        document.getElementById("dia-hora-inicio-warning").style.visibility = "visible";
    }

    let fechaT = document.getElementsByName("dia-hora-termino")[0].value;
    if (!fechaRegex.test(fechaT)) {
        errors++;
        document.getElementById("dia-hora-termino-warning").style.visibility = "visible";
    }

    // tipo validation
    let tipo = document.getElementsByName("tipo-comida")[0].value;
    if (tipo === "") {
        errors++;
        document.getElementById("tipo-comida-warning").style.visibility = "visible";
    }

    // fotos validation
    let validFiles = true;
    let atLeastOne = false;
    let fileRegex = /\.(gif|jpe?g|png|webp)$/i;
    let files = document.getElementsByName("foto-comida");
    for (const filesKey in files) {
        if (isNaN(filesKey)) {
            break;
        }
        atLeastOne = atLeastOne || fileRegex.test(files[filesKey].value);
        validFiles = validFiles && (fileRegex.test(files[filesKey].value) || files[filesKey].value === "");
    }
    if (files.length < 1 || files.length > 5 || !validFiles || !atLeastOne) {
        errors++;
        document.getElementById("foto-comida-warning").style.visibility = "visible";
    }

    if (errors === 0) {
        confirm();
    }
}

function hideWarnings() {
    $("p[id*='warning']").each(function() {
        $(this).css("visibility", "hidden");
    });
}

function confirm() {
    $( "#dialog-confirm" ).attr("display", "initial");
    $( function() {
        $( "#dialog-confirm" ).dialog({
            draggable: false,
            resizable: false,
            height: "auto",
            width: 400,
            modal: true,
            buttons: {
                "Si, estoy seguro": function () {
                    $(this).dialog("close");
                    successDialog();
                },
                "No, no estoy seguro, quiero volver al formulario": function () {
                    $(this).dialog("close");
                }
            }
        });
    } );
}

function successDialog() {
    $( "#dialog-success" ).attr("display", "initial");
    $( function() {
        $( "#dialog-success" ).dialog({
            draggable: false,
            resizable: false,
            height: "auto",
            width: 400,
            modal: true,
            buttons: {
                "Volver a la portada": function () {
                    $(this).dialog("close");
                    goToPortada();
                }
            }
        });
    } );
}