'use strict'

// need event 'click'

$("#button_").click(function(event) {
    event.preventDefault();
    deleteComment(pk);
});

function deleteComment(pk) {
    let confirmation = confirm('Вы хотите удалить комментарий?');
    if (confirmation) {
        const token = document.cookie.split('=')[1];
        let tail = String(pk);

        $.ajax({
            url: $("#button_" + tail).attr("data-ajax-target"),
            type: 'POST',
            data: {
                comment_pk: pk,
                'csrfmiddlewaretoken': token,
                 },
            success: function () {
                $("#comment_" + tail).html("<p class='mt-2' id='body-comment'>Ваш комментарий удалён</p>");
            },

            error: function(xhr, errormsg, err) {
                console.log(errormsg);
            },
        });
    }
};