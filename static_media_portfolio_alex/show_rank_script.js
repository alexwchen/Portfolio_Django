$('#portfolio_tabs_bar').tabs();

// Projects: hover color change
$('.div_portfolio_rank_frame').mouseenter(function(){
	
	if ( $('.img_arrow_display_size', this).attr('src') != 'media/Images/like_button_hover.jpg'){
		$('.img_arrow_display_size', this).attr('src', 'media/Images/like_button_ori.jpg');	
	}
	$(this).css('background-color','#CFECEC');
});
$('.div_portfolio_rank_frame').mouseleave(function(){
	$(this).css('background-color','white');
	$(this).css('border','0px solid #2F6AB3');
	$(this).css('border-bottom','1px solid #C0C0C0');

	$('.img_arrow_display_size', this).attr('src', 'media/Images/like_button.jpg');			
});




// Like: hover size change
$('.img_arrow_display_size').mouseenter(function(){
	$(this).attr('src', 'media/Images/like_button_hover.jpg')		
	$(this).css('width','35px');
	$(this).css('height','35px');	
});

$('.img_arrow_display_size').mouseleave(function(){
	$(this).attr('src', 'media/Images/like_button_ori.jpg')
	$(this).css('width','30px');
	$(this).css('height','30px');
});

// Like: click size change + trigger votes
$('.img_arrow_display_size').click(function(){
	var current_page = $(this).attr('data-click');
	$.get("/user_vote/voting_project", {current_page_url: current_page}, function(data){
		//alert(data)
		// should I provide user feedback
	});

	$(this).css('width','35px');
	$(this).css('height','35px');
	$(this).fadeOut()
	return false
});




// Filter Selection
$("#select_category").change(function () 
{
	var str = "";
	$("select option:selected").each(function () {

		if ($(this).text() == 'All Projects'){
			
			var filter_opt = $(this).text();
			$.get("/user_vote/rankfilter", {filter_option: filter_opt}, function(data){
				var organized = JSON.parse(data);
			
				for(var i=0; i<organized.total; i++){
					var id_name = '#portfolio_rank_frame' + (i+1)
					$(id_name).fadeOut();
				}
				
				for(var i=1; i<=organized.sortedlist.length; i++){
					var id_name = '#portfolio_rank_frame' + organized.sortedlist[i-1];
					$(id_name).fadeIn();
				}			
			});
			

			
		}
		
		if ($(this).text() == 'Machine Learning'){
						
			var filter_opt = $(this).text();
			$.get("/user_vote/rankfilter", {filter_option: filter_opt}, function(data){
				var organized = JSON.parse(data);
			
				for(var i=0; i<organized.total; i++){
					var id_name = '#portfolio_rank_frame' + (i+1)
					$(id_name).fadeOut();
				}
				
				for(var i=0; i<organized.sortedlist.length; i++){
					var id_name = '#portfolio_rank_frame' + (organized.sortedlist[i])
					$(id_name).fadeIn();
				}
				
			});
			
		}


		if ($(this).text() == 'Human Computer Interface'){
			
			var filter_opt = $(this).text();
			$.get("/user_vote/rankfilter", {filter_option: filter_opt}, function(data){
				var organized = JSON.parse(data);
			
				for(var i=0; i<organized.total; i++){
					var id_name = '#portfolio_rank_frame' + (i+1)
					$(id_name).fadeOut();
				}
				
				for(var i=0; i<organized.sortedlist.length; i++){
					var id_name = '#portfolio_rank_frame' + (organized.sortedlist[i])
					$(id_name).fadeIn();
				}
			});
			
		}


		if ($(this).text() == 'Publications'){
			
			var filter_opt = $(this).text();
			$.get("/user_vote/rankfilter", {filter_option: filter_opt}, function(data){
				var organized = JSON.parse(data);
			
				for(var i=0; i<organized.total; i++){
					var id_name = '#portfolio_rank_frame' + (i+1)
					$(id_name).fadeOut();
				}
				
				for(var i=0; i<organized.sortedlist.length; i++){
					var id_name = '#portfolio_rank_frame' + (organized.sortedlist[i])
					$(id_name).fadeIn();
				}
			});
			
		}

		
		if ($(this).text() == 'Web'){

			var filter_opt = $(this).text();
			$.get("/user_vote/rankfilter", {filter_option: filter_opt}, function(data){
				var organized = JSON.parse(data);
			
				for(var i=0; i<organized.total; i++){
					var id_name = '#portfolio_rank_frame' + (i+1)
					$(id_name).fadeOut();
				}
				
				for(var i=0; i<organized.sortedlist.length; i++){
					var id_name = '#portfolio_rank_frame' + (organized.sortedlist[i])
					$(id_name).fadeIn();
				}
			});

		}
		

	});
})
.change();


$("#select_ranking").change(function () 
{
	var str = "";
	/* Handy Code: We need to put this in documentation
				$("#portfolio_tabs_frame").empty();
				var content = $("#portfolio_rank_frame6").html();
				var content2 = $("#font_portfolio_rank_number3").html();
				$("#portfolio_rank_frame4").html(content);
				$("#font_portfolio_rank_number6").html(content2);
	*/
	
	$("select option:selected").each(function () {
		if ($(this).text() == 'Best'){

			// request calculate ranking
			var filter_opt = $(this).text();

			$.get("/user_vote/rankfilter", {filter_option: filter_opt}, function(data){
				var organized = JSON.parse(data);
				
				// sort the rank according to the new list
				for(var i=1; i<=organized.total; i++){
					$("#portfolio_rank_frame" + organized.sortedlist[i-1]).appendTo("#portfolio_tabs_frame");										
					$("#font_portfolio_rank_number"+organized.sortedlist[i-1]).html(i);
				}																		
			});	
								
		}


		if ($(this).text() == 'Recommend For You'){

			// request calculate ranking
			var filter_opt = $(this).text();

			$.get("/user_vote/rankfilter", {filter_option: filter_opt}, function(data){
				var organized = JSON.parse(data);
				
				// sort the rank according to the new list
				for(var i=1; i<=organized.total; i++){
					$("#portfolio_rank_frame" + organized.sortedlist[i-1]).appendTo("#portfolio_tabs_frame");										
					$("#font_portfolio_rank_number"+organized.sortedlist[i-1]).html(i);
				}																		
			});	
								
		}
		
		if ($(this).text() == 'Most Recent'){
			
			// request calculate ranking
			var filter_opt = $(this).text();
			$.get("/user_vote/rankfilter", {filter_option: filter_opt}, function(data){
				
				var organized = JSON.parse(data);
				for(var i=1; i<=organized.total; i++){
					$("#portfolio_rank_frame" + organized.sortedlist[i-1]).appendTo("#portfolio_tabs_frame");					
					//$("#font_portfolio_rank_number"+organized.sortedlist[i-1]).html(i);
				}
				
			});									
		}


		if ($(this).text() == 'Less Recent'){
			
			// request calculate ranking
			var filter_opt = $(this).text();
			$.get("/user_vote/rankfilter", {filter_option: filter_opt}, function(data){
				
				var organized = JSON.parse(data);
				// store all the proj in an array
				for(var i=1; i<=organized.total; i++){
					$("#portfolio_rank_frame" + organized.sortedlist[i-1]).appendTo("#portfolio_tabs_frame");					
					//$("#font_portfolio_rank_number"+organized.sortedlist[i-1]).html(i);
				}
				
			});									
		}
		
		
		
	});
})
.change();
