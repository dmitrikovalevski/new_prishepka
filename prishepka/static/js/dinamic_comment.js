'use strict'


$("#comment-form").on('submit', function(event) {
	event.preventDefault();
	console.log('form submitted')
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
			$("#id_body").val('');
			console.log(json);
			console.log('success');
		},

		error: function(xhr, errormsg, err) {
			$("#new-block-comment").html("<div class='container bt-3 border' id='block-comment'>" + errormsg + "</div>");
			console.log(xhr.status);
		}
	});
};
