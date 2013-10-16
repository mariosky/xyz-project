$ = jQuery.noConflict();
jQuery(document).ready(function($){
	
	//Place holder for input, textarea
	$('input, textarea').placeholder();
	
	// Start audio, video player
	$('audio,video').mediaelementplayer({
		audioWidth: '100%',
		features: ['playpause','progress','current','volume']
	});
	
	//Autoresize Video
	if(jQuery().fitVids) {
		$(".fit").fitVids();
	}
	
	// Scroll to top
	$(function () {
		var scrolling_top = 0;
		var scrolling_bottom = 0;
		$(window).scroll(function () {
			if ($(this).scrollTop() < 100) {
				if(scrolling_top == 0){
					scrolling_top = 1;
					
					$('#toTop').animate({"bottom": '0' }, 200,function(){
						scrolling_top = 0;
					});
					
				}
			} else if($(this).scrollTop() > 100) {
				if(scrolling_bottom == 0){
					scrolling_bottom = 1;
					$('#toTop').animate({"bottom": '50px' }, 200,function(){
						scrolling_bottom = 0;
					});
				}
			}
		});

		// scroll body to 0px on click
		$('#toTop a').click(function () {
			$('body,html').animate({scrollTop: 0}, 800);
			return false;
		});
	});
	
	// Menu
	$('ul.sf-menu').superfish({
		animation: {opacity:'show'},
		speed: 200,
		delay: 10,
		animation:   {opacity:'show',height:'show'}
	
	});
	$('#top_menu ul.sf-menu').mobileMenu({
		defaultText: 'Navigation ...',
		className: 'select_menu',
		subMenuDash: '&ndash;'
	});
	
	// Navigation style in Mobile
	$('select.select_menu').each(function(){
		var title = $(this).attr('title');
		if( $('option:selected', this).val() != ''  ) title = jQuery('option:selected',this).text();
		$(this)
			.css({'z-index':10,'opacity':0,'-khtml-appearance':'none'})
			.after('<span class="nav_select">' + title + '<span class="menu_icon"></span></span>')
			.change(function(){
				val = $j('option:selected',this).text();
				$(this).next().text(val);
			});
	});
	
	
	// Search
 	$('.search_btn').click(function () {
     $(this).toggleClass("close");
	  $('.search_box').toggleClass('show');	
    });
	
	
	// Thumb hover
	if ( $( '.thumb_hover' ).length && jQuery() ) {
		thumb_hover('.thumb_hover');
	}
	

	/** POSTS ELEMENTS
	-------------------------------------------- **/
	
	/** Tabs **/
	if($('.tabs-container').length) {	
		$('.tabs-container').each(function() {
			
			var tabs=$(this);
		
			//show first pane
			tabs.find('.tab_pane').hide();
			tabs.find('.tab_panes .tab_pane:eq(0)').show();			
			tabs.find('ul.tabs li:first-child').addClass('active');
			
			tabs.find('ul.tabs li').click(function() {
				//set active state to tab
				tabs.find('ul.tabs li').removeClass('active');
				$(this).addClass('active');
				
				//show current tab
				tabs.find('.tab_pane').hide();
				tabs.find('.tab_pane:eq('+$(this).index()+')').fadeIn();			
			});
		});	
	}
	
	/** Accordion **/
	if($('.accordion').length) {
		$("ul.accordion li").each(function(){
			$(this).children(".accordion_content").css('height', function(){ 
				return $(this).height(); 
			});
			
			if($(this).index() > 0){
				$(this).children(".accordion_content").css('display','none');
			}else{
				$(this).find(".accordion_head").addClass('active');
			}
			
			$(this).children(".accordion_head").bind("click", function(){
				$(this).addClass(function(){
					if($(this).hasClass("active")) return "";
					return "active";
				});
				$(this).siblings(".accordion_content").slideDown();
				$(this).parent().siblings("li").children(".accordion_content").slideUp();
				$(this).parent().siblings("li").find(".active").removeClass("active");
			});
		});
	}
	
	/** END POST ELEMENTS **/

});


// Thumb hover
function thumb_hover($wrapp) {
	if ( $( $wrapp ).length && jQuery() ) {
		//$($wrapp).find('div.hover').css("opacity",0);
		$($wrapp).hover(function() {
		$(this).find('.img_wrapper img').animate({opacity: 0.4}, 300);			 
		$(this).find('.for_link').stop(0,0).removeAttr('style');
		$(this).find('.for_view').stop(0,0).removeAttr('style');
		$(this).find('.for_link').animate({"top": "50%" }, 500);
		$(this).find('.for_view').animate({"top": "50%" }, 500);
		}, function() {
			$(this).find('.for_link').stop(0,0).animate({"top": "120%"}, 500);
			$(this).find('.for_view').stop(0,0).animate({"top": "-30%"}, 500);
			$(this).find('.img_wrapper img').animate({opacity: 1}, 300);	
			//$(this).find('div.hover').stop(0,0).animate({opacity: 0}, 500);
		});
	}
}

