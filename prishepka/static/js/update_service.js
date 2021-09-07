"use strict"

// Переменная с данными усдуги
let getData;

// Получаем данные об услуге
$.ajax({
    url: $("#update_content").attr('data-ajax-target'),
    type: 'GET',
    success: function(data) {
        getData = data;
        // Заполним поля формы
        $("#update_title").val(getData['title']);
        $("#update_description").val(getData['descriptions']);
        $("#update_price").val(getData['price']);
    },
    error: function(data) {
        console.log('Get не отработал');
    },
});

// Запустим скрипт оптравки формы на сервер
$("#send_contextModal").on('click', function(event) {
    event.preventDefault();
    updateContext();
});

function updateContext() {
    // токен
    let token = document.cookie.split('=')[1];

    // Формируем данные для отправки на сервер
    let fData = new FormData();
    if ($("#update_picture")[0].files[0] !== undefined) {
        fData.append('picture', $("#update_picture")[0].files[0]);
    };
    fData.append('pk', getData['pk']);
    fData.append('title', $("#update_title").val());
    fData.append('descriptions', $("#update_descriptions").val());
    fData.append('price', $("#update_price").val());

    $.ajax({
    url: $("#send_contextModal").attr('data-ajax-target'),
    type: 'PUT',
    data: fData,
    headers: {
        'X-CSRFToken': token,
    },
    contentType: false,
    processData: false,
    success: function(data) {
    // если изображения нету, а пользователь добавил новое, тогда добавить картинку
    if (getData['picture'] === null && data['picture'] !== undefined) {
        $("#description_block").before(
            "<img id='service_image' src='" + data['picture'] + "' height='200' class='rounded'>"
        );
    };
    $("#service_title").text(data['title']);
    $("#service_descriptions").text(data['descriptions']);
    $("#service_price").text(data['price']);
    $("#service_image").attr('src', data['picture']);
    },
    error: function(data) {
        console.log(data['message'])
    },
});
};


