'use strict'


$("#comment-form").on('submit', function(event) {
	event.preventDefault();
	create_comment();
});



function create_comment() {
	console.log('comment post is working')
	let token = document.cookie.split('=')[1];
	console.log(token)

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
			$("#new-block-comment").append("<div class='container bt-3 border' id='block-comment'>" +
	        "<img src='" + check + "' height='25' id='image-comment'>" +
	        "<a href='/user/account/" + json['user_pk'] + "'>" + json['user'] + "</a>" +
	        "<p class='mt-2' id='body-comment'>" + json['body'] + "</p>" +
	        "<p class='d-flex justify-content-end'><button type='submit' id='delete_comment'>удалить</button></p>" +
	        "<p class='d-flex justify-content-end' id='date-created-comment'>" + json['date_created'] + "</p></div>");
		},

		error: function(xhr, errormsg, err) {
			$("#new-block-comment").html("<div class='container bt-3 border' id='block-comment'>" + errormsg + "</div>");
		}
	});
};
