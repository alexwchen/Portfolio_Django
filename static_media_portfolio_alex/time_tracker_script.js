$(window).load(function(){
	var current_page = window.location.href;
	$.get("/user_vote/window_load_time_stemp", {current_page_url: current_page}, function(data){
	//	alert(data)
	});
});

$(window).unload(function(){
	var current_page = window.location.href;	
	$.ajax({
		type: 'GET',
		async: false,
	    url: '/user_vote/window_unload_time_stemp',
		data: 'current_page_url='+current_page,
		success: function(data){
	       //alert("It is working: " + data)
		}
	});	
});
