$(document).ready(function(){
    $('#logout').click(function(){
        $.ajax({
            type: 'GET',
            url: 'http://localhost:5000/logout',
            success: function(data){
                var rdata = jQuery.parseJSON(data)
                if (rdata.data.status == 'success'){
                    window.location.replace("http://localhost:5000/login");
                }
            }
        })
    });
    $("#sidebar-menu ul li").click(function(){
        if($(this).children(".box-drawer").is(":hidden")){
            if(!$(this).children(".box-drawer").is(":animated")){
                $(this).children(".box-drawer").animate({
                    height: 'show'
                }, 1000)
            .end().siblings().find(".box-drawer").hide(1000);
            }
        } else{
            if(!$(this).children(".box-drawer").is(":animated")){
                $(this).children(".box-drawer").animate({
                    height: 'hide'
                }, 1000)
                end().siblings().find(".box-drawer").hide(1000);
            }
        }
    });
    $('.box-drawer').click(function(e){
        e.stopPropagation();
    });

});