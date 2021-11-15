function displayDetails(key, max) {
    let bg = document.getElementsByClassName("bg")
    if (bg.length !== 0) {
        bg[0].classList.remove("bg");
    }
    for (let i = 0; i < max; i++) {
        let id = "info-" + i;
        if (i === key) {
            document.getElementById(id).style.display = "block";
        } else {
            document.getElementById(id).style.display = "none";
        }
    }
}

let currentPage = 0;

function displayPage(step, last) {
    let nextFirst = (currentPage + step) * 5
    if (nextFirst < last && nextFirst >= 0) {
        currentPage += step;
        let firstElement = 5 * currentPage;
        for (let i = 0; i < last; i++) {
            let id = "event-" + i;
            if (i < firstElement || i >= firstElement + 5) {
                document.getElementById(id).style.display = "none";
            } else {
                document.getElementById(id).style.display = "table-row";
            }
        }
    }
}

function popUpImage(imgPath, imgAlt) {
    $("#pop-up-img").attr("display", "initial");
    $("#pop-up-img p").html("" +
        "<img class=\"pop-up__img\" " +
        "src=\" ../media/" + imgPath +
        "\" alt=\"" + imgAlt + "\">");
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