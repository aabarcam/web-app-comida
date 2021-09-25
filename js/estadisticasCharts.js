function generateEventsPerDay() {
    let data = {
        labels: ['2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18', '2022-01-19', '2022-01-20',
            '2022-01-21', '2022-01-22', '2022-01-23', '2022-01-24'],
        datasets: [{
            label: 'Cantidad de eventos',
            data: [2, 5, 0, 1, 3, 4, 0, 3, 3, 1],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    };
    let ctx = document.getElementById('events-per-day-chart').getContext('2d');
    let eventsPerDay = new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

let tipos = ["Al Paso", "Alemana", "Árabe", "Argentina", "Asiática", "Australiana", "Brasileña", "Café y Snacks",
    "Carnes", "Chilena", "Otros"];

function generateEventsPerType() {
    let ctx = document.getElementById('events-per-type-chart').getContext('2d');
    let data = {
        labels: tipos,
        datasets: [{
            label: 'Cantidad de eventos',
            data: [1, 3, 2, 1, 3, 2, 1, 3, 2, 6, 4],
            backgroundColor: [
                'rgba(255, 99, 132, 0.5)',
                'rgba(54, 162, 235, 0.5)',
                'rgba(255, 206, 86, 0.5)',
                'rgba(75, 192, 192, 0.5)',
                'rgba(153, 102, 255, 0.5)',
                'rgba(255, 159, 64, 0.5)',
                'rgba(107, 199, 122, 0.5)',
                'rgba(255, 62, 62, 0.5)',
                'rgba(255, 247, 91, 0.5)',
                'rgba(53, 100, 101, 0.5)',
                'rgba(176, 60, 211, 0.5)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(107, 199, 122, 1)',
                'rgba(255, 62, 62, 1)',
                'rgba(255, 247, 91, 1)',
                'rgba(53, 100, 101, 1)',
                'rgba(176, 60, 211, 1)'
            ],
            borderWidth: 1,
            hoverOffset: 4
        }]
    };
    let eventsPerType = new Chart(ctx, {
        type: 'pie',
        data: data,
        options: {
            maintainAspectRatio: false
        }
    });
}

function generateEventsPerTime() {
    let ctx = document.getElementById("events-time-of-day").getContext("2d");
    let data = {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
            'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        datasets: [
            {
                label: "Eventos en la mañana",
                backgroundColor: "rgba(252, 255, 150, 0.8)",
                data: [3, 4, 2, 1, 5, 3, 5, 6, 7, 2, 3, 5]
            },
            {
                label: "Eventos al medio día",
                backgroundColor: "rgba(255, 145, 77, 0.8)",
                data: [4, 3, 5, 8, 2, 3, 5, 2, 5, 1, 6, 2]
            },
            {
                label: "Eventos en la tarde",
                backgroundColor: "rgba(92, 98, 184, 0.8)",
                data: [2, 2, 6, 5, 4, 7, 2, 4, 8, 3, 5, 7]
            }
        ]
    };

    let eventsPerTime = new Chart(ctx, {
        type: 'bar',
        data: data,
        options: {
            barValueSpacing: 20,
            scales: {
                yAxes: [{
                    ticks: {
                        min: 0,
                    }
                }]
            }
        }
    });
}


function generateEstadisticas() {
    generateEventsPerDay();
    generateEventsPerType();
    generateEventsPerTime();
}