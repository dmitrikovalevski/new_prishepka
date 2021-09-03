"use strict"

let getData;

$.ajax({
    url: $("#update_button").attr('data-ajax-target'),
    type: 'GET',
    success: function(data) {
        getData = data;
        console.log(getData);
    },
    error: function(data) {
        console.log('ERROR');
    },
});

$("#update_button").on('click', function(event) {
    event.preventDefault();
    updateService();
});

function updateService() {};

/* ("#id_modal_content").html("<div class='modal-header'>" +
            "<h5 class='modal-title' id='exampleModalLabel'>Добавить услугу:</h5>" +
            "<button type='button' class='btn-close' data-bs-dismiss='modal' aria-label='Close'></button>" +
            "</div>" +
            "<div class='modal-body'>" +
            "<form method='POST' enctype='multipart/form-data' name='service_form' id='id_service_form'>" +
            "{% csrf_token %}" +
            "<div class='mb-3'>" +
            "<label for='picture' class='form-label'>Добавте изображение</label>" +
            "<input class='form-control' type='file' id='picture'>" +
            "</div>" +
            "<div class='mb-3'>" +
            "<label for='title' class='col-form-label'>Title:</label>" +
            "<input type='text' class='form-control' id='title'>" +
            "</div>" +
            "<div class='mb-3'>" +
            "<label for='description' class='col-form-label'>Description:</label>" +
            "<textarea class='form-control' rows='8' id='description'></textarea>" +
            "</div>" +
            "<div class='mb-3'>" +
            "<label for='price' class='col-form-label'>Price:</label>" +
            "<input type='text' class='form-control' id='price'>" +
            "</div>" +
            "</form>" +
            "</div>" +
            "<div class='modal-footer'>" +
            "<button type='button' class='btn btn-secondary' data-bs-dismiss='modal'>Отмена</button>" +
            "<button type='button' class='btn btn-primary' data-ajax-target='{% url 'service' %}' id='send_service'>Отправить</button>" +
            "</div>)"); */