

$("#delete_service").click(function(event) {
    event.preventDefault();
});

function deleteService(pk) {
    const csrftoken = document.cookie.split('=')[1];

    let confirmation = confirm('Вы хотите удалить эту услугу?');
    if (confirmation) {
        $.ajax({
            url: $("#delete_service").attr('data-ajax-target'),
            type: 'DELETE',
            headers: {
                'X-CSRFToken': csrftoken,
            },
            data: {
                pk: pk,
            },
            success: function(data) {
                $("#service_content").html(
                "<div>" +
                "<h1>" + data['message'] + "</h1>" +
                "<a href='/' class='btn btn-secondary'>На главную</a>" +
                "</div>");
                $("#service_buttons").hide();
                $("#comment_block_view").hide();
                $("#comment_block").hide();
            },
            error: function(data) {
                $("#service_content").html(
                "<div>" +
                "<h1>" + data['message'] + "</h1>" +
                "<a href='/' class='btn btn-secondary'>На главную</a>" +
                "</div>");
                $("#service_buttons").hide();
                $("#comment_block_view").hide();
                $("#comment_block").hide();
            },
        });
    };
};
