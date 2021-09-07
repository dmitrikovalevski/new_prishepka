'use strict'


$("#comment-form").on('submit', function(event) {
    /*if ($("#id_body").val() == '') {
        $("#id_body").attr('placeholder', 'Введите текст что бы ставить комментарий..');
    } else {
        event.preventDefault();
    };*/
	event.preventDefault();
	create_comment();
});

function create_comment() {
	let token = document.cookie.split('=')[1];

	let fulllink = window.location.href;
	let pk = fulllink.split('/').slice(-2, -1).join();

	let comment = $("#id_body").val();
	console.log(comment);

	$.ajax({
		url: $("#submit-form").attr("data-ajax-target"),
		type: 'POST',
		headers: {
		    'X-CSRFToken': token,
		},
		data: {
		    service_pk: pk,
			comment: comment,
		},
		success: function(data) {
			let check;
			if (data['image'] == '') {
				check = '/static/image/user1.png';
			} else {
				check = data['image'];
			};
			$("#id_body").val('');
			$("#new-block-comment").append("<div class='container bt-3 border' id='comment_" + data['comment_pk'] + "'>" +
	        "<img src='" + check + "' height='25' id='image-comment'>" +
	        "<a href='/user/account/" + data['user_pk'] + "'>" + data['user'] + "</a>" +
	        "<p class='mt-2' id='body-comment'>" + data['body'] + "</p>" +
	        "<p class='d-flex justify-content-end'><button id='button_' class='btn btn-secondary btn-sm' data-ajax-target='/detail/" + data['service_pk'] + "/' onclick='deleteComment(" + data['comment_pk'] + ")'>удалить</button></p>" +
	        "<p class='d-flex justify-content-end' id='date-created-comment'>" + data['date_created'] + "</p></div>");
		},

		error: function(xhr, errormsg, err) {
			$("#new-block-comment").html("<div class='container bt-3 border' id='block-comment'>" + errormsg + "</div>");
		}
	});
};



