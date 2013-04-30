$('#portfolio_tabs_bar').tabs();

// Projects: hover color change
$('.div_portfolio_color_rank_frame').mouseenter(function(){
	$(this).css('background-color','#CFECEC');
});
$('.div_portfolio_color_rank_frame').mouseleave(function(){
	$(this).css('background-color','white');
});

// Publications: hover color change
$('.div_portfolio_pub_color_rank_frame').mouseenter(function(){
	$(this).css('background-color','#CFECEC');
});
$('.div_portfolio_pub_color_rank_frame').mouseleave(function(){
	$(this).css('background-color','white');
});
