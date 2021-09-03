
$("#send_service").on("click", function(event) {
    event.preventDefault();
    addNewService();
});

function addNewService() {
    let token = document.cookie.split('=')[1];

    let fData = new FormData();
    if ($("#picture")[0].files[0] !== undefined) {
        fData.append('picture', $("#picture")[0].files[0]);
    };
    fData.append('title', $("#title").val());
    fData.append('descriptions', $("#description").val());
    fData.append('price', $("#price").val());
    fData.append('csrfmiddlewaretoken', token);


    let action = function(data) {
        $("#picture").val("");
        $("#title").val("");
        $("#description").val("");
        $("#price").val("");
        console.log(data);
        $("#id_modal_content").html("<div class='modal-header'>" +
        "<button type='button' class='btn-close' data-bs-dismiss='modal' aria-label='Close'></button>" +
        "</div>" +
        "<div class='modal-body'>" + data['message'] +
        "</div>" +
        "<div class='modal-footer'>" +
        "<a href='/' class='btn btn-primary'>На главную</a>" +
        "<button type='button' class='btn btn-primary' data-bs-dismiss='modal'>Продолжить</button>" +
        "</div>")
    };

    $.ajax({
        url: $("#send_service").attr('data-ajax-target'),
        type: 'POST',
        data: fData,
        contentType: false,
        processData: false,
        success: action,
        error: action,
    });
};
