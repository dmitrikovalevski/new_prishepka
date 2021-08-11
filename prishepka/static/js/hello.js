'use strict'


let request = null;

try {
		request = new XMLHttpRequest();

	} catch (failed) {

		request = null;

	}
	if (request == null)
	alert('Error creating request');


function getSomeone() {
	let url = $("#test-button").attr("data-ajax-target");
	request.open('get', url, true);
	request.send(null);
}

function updatePage() {
	if (request.readyState == 4) {
	let newComment = request.responseText;
	let comment = document.getElementById("#comment");
	replaceText(comment, newComment);
	}
}

function getCustomerInfo() {
	let phone = document.getElementById("#phone").value;
	let url = $("#submit-button").attr("data-ajax-target");
	request.open("GET", url, true);
	request.onreadystatechange = updatePage;
	request.send(null);
}







/*
$(document).ready(function() {
	getComment();
	$("#submit-form").click(function() {

		let comment_body = $("#id_body").val();

		$.ajax({
			type: "post",
			url: "{% url 'detail' %}",
			data: {
				'comment': comment_body,
			},
		});
	});
});

function getComment() {

	$.ajax({
		type: 'get',
		url: "{{ url 'detail' }}",

		success: function(call) {
			let datas = $.parseJSON(call);
			$("#").html(datas.answer)
		}
	});
}


/*
function ajax_post() {

	let body = $(this).serialize();

	$.ajax({
		url: "{% url 'detail' %}",
		type: "POST",
		data: {
			'body': body,
			//'csrfmiddlewaretoken': "{{ csrf_token }}"
		},
		datatype: 'json',
		success: function(response) {
			console.log(response);
		},
		error: function(rs, e) {
			console.log(e);
		} 
	})
}


$(document).ready(function() {
	$('#submit-form').click(function(e) {

		ajax_post();
	});
});

/*
$("#comment-form").submit(function(e) {
	e.preventDefault();

	let alldata = $(this).serialize();

	$.ajax({
		type: "POST",
		url: "{% url 'detail' %}",
		data: alldata,
		success: function(respose) {
			$("#comment-form").trigger("reset");
			$("#id_body").focus();
		}
	});
});



/*
$.ajax({
	url: 'http://127.0.0.1:8000/',
	type: 'get',
	success: function(data) {
		alert(data);
	},
	failure: function(data) {
		alert('ERROR');
	}
});



/*
$('#id_body').change(function() {
	let comment_body = $(this).val();

	$.ajax({
		url: "{% url 'validate_comment' %}",
		data: comment_body.serialize(),
		success: function(response) {
			if (response.body == 'comment_body') {
				alert('ok')
			}
		}
	});
});

/*
$("#id_body").change(function() {
	$(this).attr("body");
	
});
	/*
	let comment_body = $(this).val();

	$.ajax({
		url: "{% url 'validate_comment' %}",
		data: {
			'body': comment_body
		},
		dataType: 'json',
		success: function (data) {
			if (data.is_taken) {
				console.log(data);
			}
		}
	});
});



/*
let xhr = new XMLHttpRequest();
xhr.open(
	'get',
	'http://192.168.1.89/detail/2/',
	true,
	)

xhr.send()

xhr.onreadystatechange = function() {
	if (xhr.readyState != 4) {
		return
	}
	if (xhr.status === 200) {
		console.log('result\n', xhr.getResponseHeader("server"));
	} else {
		console.log('err', xhr.responseText);
	}
};



/*
$(document).ready(function() {
	$("#submit-form").click(function() {
		let value = 'text';
		$("#new-user-comment").html(`<div class="container bt-3 border" id="comment-view"><br><br><br></div>`);
	});
});

function loadDoc() {
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    document.getElementById("new-user-comment").innerHTML = this.responseText;
    console.log(this.responseText);
    }
  xhttp.open("GET", "http://192.168.1.89/detail/2/", true);
  xhttp.send();
}

//var ajaxreq = new XMLHttpRequest();
//ajaxreq.open('GET', 'http://s13.ru/');
//ajaxreq.onload = function() {
//	var myData = JSON.parse(ajaxreq.responseText);
//	console.log(ajaxreq[0]);
//};
//ajaxreq.send();

/*
function getRequest() {
	let xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			alert(this.status);
		}
	};
	xhr.open('GET', "{% url 'home' %}", true);
	xhr.send();
}
*/


//$(document).ready(function() {
//	$('#comment').on('submit', function() {
//		$.ajax({
//			url: "{% url 'detail' %}",
//			method: 'post',
//			dataType: 'html',
//			data: $(this).serialaze(),
//			success: function(data){
//				console.log(JSON.stringify());
//			}
//		});
//	});
//});



//$(document).ready(function() {
//	$('.btn').click(function() {
//		let comment = '{{ last_comment.body }}'
//		alert(comment);
//	});
//});

//$(document).ready(function() {
//	$('#111').click(function() {
//		$('p').hide();
//	});
//	$('#222').click(function() {
//		$('p').show();
//	});
//});

//alert('message');

//$(document).ready(function() {
//	$('.but').click(function() {
//		alert('push me');
//	});
//});

//$(document).ready(function() {
//	$('.container').click(function() {
//		$(this).hide();
//	});
//});

//$(document),ready(function() {
//	$("button").click(function() {
//		$(".container").fadeToggle("slow");
//	});
//});