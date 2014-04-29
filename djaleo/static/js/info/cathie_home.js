$(function(){
    $('#header-nav').data('size','big');
});

$(window).scroll(function(){
    var $navOne = $('#header-nav');
    var $navTwo = $('.cath-main-nav');
    if ($('body').scrollTop() > 50) {
        if ($navOne.data('size') == 'big') {
            $navOne.css("position","fixed");
            $navOne.data('size','small').stop().animate({
                height:'60px',
                top:'0'
            }, 600);
            $navTwo.data('size','small').stop().animate({
                "padding-top":"4px",
            }, 600);
        }
    } else {
        if ($navOne.data('size') == 'small') {
            $navOne.css("position","relative");
            $navOne.data('size','big').stop().animate({
                height:'112px',
            }, 600);
            $navTwo.data('size','big').stop().animate({
                "padding-top":"28px",
            }, 600);
        }  
    }
});