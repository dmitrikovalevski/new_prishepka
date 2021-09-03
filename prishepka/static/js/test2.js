


$("#send_service").on("click", function(event) {
    event.preventDefault();
    addNewService();
});

function addNewService() {
    let form = document.forms.service_form;
    let data = new FormData(form);

    let action = function(data) {
        $("#id_picture").val("");
        $("#id_title").val("");
        $("#id_descriptions").val("");
        $("#id_price").val("");
        console.log(data);
        $("#id_modal_content").html("<div class='modal-header'>" +
        "<button type='button' class='btn-close' data-bs-dismiss='modal' aria-label='Close'></button>" +
        "</div>" +
        "<div class='modal-body'>" + data['message'] +
        "</div>" +
        "<div class='modal-footer'>" +
        "<a href='{% url 'home' %}' class='btn btn-primary'>На главную</a>" +
        "<button type='button' class='btn btn-primary' data-bs-dismiss='modal'>Продолжить</button>" +
        "</div>")
    };

    $.ajax({
        url: $("#send_service").attr('data-ajax-target'),
        type: 'POST',
        data: data,
        contentType: false,
        processData: false,
        success: action,
        error: action,
    });
};
