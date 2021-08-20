'use strict'


$("#comment-form").on('submit', function(event) {
	event.preventDefault();
	create_comment();
});



function create_comment() {
	let token = document.cookie.split('=')[1];


	$.ajax({
		url: $("#submit-form").attr("data-ajax-target"),
		type: 'POST',
		data: { 
			the_comment: $("#id_body").val(),
			'csrfmiddlewaretoken': token,
			 },

		success: function(json) {
			let check;

			if (json['image'] == '') {
				check = '/static/image/user1.png';
			} else {
				check = json['image'];
			};

			$("#id_body").val('');
			$("#new-block-comment").append("<div class='container bt-3 border' id='comment_" + json['comment_pk'] + "'>" +
	        "<img src='" + check + "' height='25' id='image-comment'>" +
	        "<a href='/user/account/" + json['user_pk'] + "'>" + json['user'] + "</a>" +
	        "<p class='mt-2' id='body-comment'>" + json['body'] + "</p>" +
	        "<p class='d-flex justify-content-end'><button id='button_" + json['comment_pk'] + "' class='btn btn-secondary btn-sm' data-ajax-target='/detail/" + json['service_pk'] + "/' onclick='deleteComment(" + json['comment_pk'] + ")'>удалить</button></p>" +
	        "<p class='d-flex justify-content-end' id='date-created-comment'>" + json['date_created'] + "</p></div>");
		},

		error: function(xhr, errormsg, err) {
			$("#new-block-comment").html("<div class='container bt-3 border' id='block-comment'>" + errormsg + "</div>");
		}
	});
};


    // Извлечение части пути из линка, который указывается в строке get браузера

	//let fullLink = window.location.href;
	//let head = fullLink.split('/').slice(0, 5).join('/');
	//console.log(head);


