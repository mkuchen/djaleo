$(function(){
    $('#sliding-nav').data('size','big');
    $('.cath-main-nav').data('size','big');
    $('.top-nav').data('size','big');
});

$(window).scroll(function(){
    var $navOne = $('#sliding-nav');
    var $navTwo = $('.cath-main-nav');
    var $navThree = $('.top-nav');
    if ($('body').scrollTop() > 0) {
        if ($navOne.data('size') == 'big') {
            $navOne.css("position","fixed").addClass("sliding").data('size','small').stop().animate({
                height:'60px',
                top:'0'
            }, 600);
            $navTwo.data('size','small').stop().animate({
                "padding-top":"4px",
            }, 600);
            
            $navThree.data('size','small').stop().animate({
                height:'50px',
            }, 600);
        }
    } else {
        if ($navOne.data('size') == 'small') {
            $navOne.css("position","relative").removeClass("sliding").data('size','big').stop().animate({
                height:'112px',
            }, 600);
            $navTwo.data('size','big').stop().animate({
                "padding-top":"22px",
            }, 600);
            
            $navThree.data('size','big').stop().animate({
                height:'112px',
            }, 600);
        }  
    }
});