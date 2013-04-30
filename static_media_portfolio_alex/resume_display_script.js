$(document).ready(function(){

});

// Education: show hidden div
$('#middle_content_container').click(function(){
	$('#education_detail').fadeToggle('fast');
});

// Education: hover color change
$('#middle_content_container').mouseenter(function(){
	$(this).css('background-color','#CFECEC');	
});
$('#middle_content_container').mouseleave(function(){
	$(this).css('background-color','white');
});


// Tech: show hidden div
$('.div_tech_title_internal').click(function(){
	  var count=$(this).attr('value');
		$('#tech_job_'+count).fadeToggle('fast');
});

// Tech: hover color change
$('.div_tech_title_internal').mouseenter(function(){
	$(this).css('background-color','#CFECEC');
});
$('.div_tech_title_internal').mouseleave(function(){
	$(this).css('background-color','white');
});
$('#portfolio_tabs_bar').tabs();


// Comm: show hidden div
$('.div_tech_title_internal_comm').click(function(){
	  var count=$(this).attr('value');
		$('#comm_display_box_id_'+count).fadeToggle('fast');
});

// Comm: hover color change
$('.div_tech_title_internal_comm').mouseenter(function(){
	$(this).css('background-color','#CFECEC');
});
$('.div_tech_title_internal_comm').mouseleave(function(){
	$(this).css('background-color','white');
});


// Tech Expand All
$('#tech_middle_tech_job_trigger').toggle(function(){
	$(this).text('Hide All');
	$(this).css('color','#2F6AB3');
	$('.div_tech_left_detail').fadeIn('fast');
},
function(){
	$(this).text('Expand All');
	$('.div_tech_left_detail').fadeOut('fast');
	
});

// Comm Expand All
$('#comm_middle_comm_job_trigger').toggle(function(){
	$(this).text('Hide All');
	$(this).css('color','#2F6AB3');
	$('.div_comm_left_detail').fadeIn('fast');
},
function(){
	$(this).text('Expand All');
	$('.div_comm_left_detail').fadeOut('fast');
	
});