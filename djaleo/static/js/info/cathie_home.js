$(function(){
    $('#header-nav').data('size','big');
});

$(window).scroll(function(){
    var $nav = $('#header-nav');
    if ($('body').scrollTop() > 50) {
        if ($nav.data('size') == 'big') {
            $nav.css("position","fixed");
            $nav.data('size','small').stop().animate({
                height:'40px',
                top:'0'
            }, 600);
        }
    } else {
        if ($nav.data('size') == 'small') {
            $nav.css("position","relative");
            $nav.data('size','big').stop().animate({
                height:'100px',
            }, 600);
        }  
    }
});