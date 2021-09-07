'use strict'

// При нажатии
$("#button_").click(function(event) {
    event.preventDefault();
    deleteComment(pk);
});

// Отработает функция в которую заходит pk из html
function deleteComment(pk) {

    // Модальное окно
    let confirmation = confirm('Вы хотите удалить комментарий?');
    if (confirmation) {
        const token = document.cookie.split('=')[1];
        // int в str
        let tail = String(pk);

        $.ajax({
            url: $("#button_" + tail).attr("data-ajax-target"),
            type: 'DELETE',
            headers:{
                'X-CSRFToken': token,
            },
            data: {
                comment_pk: pk,
            },
            success: function (data) {
                $("#comment_" + tail).html("<p class='mt-2' id='body-comment'>" + data['message'] + "</p>");
            },
            error: function(err) {
                $("#comment_" + tail).html("<p class='mt-2' id='body-comment'>" + data['message'] + "</p>");
            },
        });
    }
};