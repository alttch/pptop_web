window.addEventListener('resize', function() {
    if ($('#mob_menu').hasClass('open')) {
      if (window.innerWidth > 991) {
        $('.mobile-menu').hide();
      } else {
        $('.mobile-menu').show();
      }
    } 
    if($('#mob_menu').hasClass('open')){
        $('#mob_menu').css({left: (window.innerWidth - $('#mob_menu').outerWidth())}, 150);
    }
});
function openMenu() {
    $('body').css("overflow","hidden");
    $('#mob_menu').css("overflow","auto");
    $('.mobile-menu').toggle();
    $('#mob_menu').animate({left: (window.innerWidth - $('#mob_menu').outerWidth())}, 150);
    $('#mob_menu').addClass('open');
}
function closeMenu() {
    $('body').css("overflow","auto");
    $('#mob_menu').animate({left: "100%"}, 150);
    setTimeout( function() { $('.mobile-menu').toggle()}, 150);
    $('#mob_menu').removeClass('open');
}
/*Function for closing menu on tapping on left side of screen*/
function closeM(e) {
    if (e.target != $('.mobile-menu')[0]) {
        return;
    }
    closeMenu();
}
document.addEventListener('swiped-left', function(e) {
	if($('.slider').is(':visible')) {
		document.location = $('.slider:visible .slide:target .next')[0].href
	} else {
		if($(window).width() < 992 && e.detail.indexOf('edge')!=-1) {
			var elementExists = document.getElementsByClassName("smoothbox");
			if(elementExists.length == 0 && !$('#mob_menu').hasClass('open')) {
				openMenu();
			}
		}
	}
});
document.addEventListener('swiped-right', function(e) {
	if($('.slider').is(':visible')) {
		document.location = $('.slider:visible .slide:target .prev')[0].href
	}
});