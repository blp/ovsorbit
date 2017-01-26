var main = function() {
    $(".openbtn").click(function() {
        $("#sidenav").animate({left: "0"}, 250, function () { $(".sidenav-text").fadeIn() });
        $("#main").animate({paddingLeft: "250px"}, 250);
        $("#head-wrap").animate({paddingLeft: "250px"}, 250);
    });
    $(".closebtn").click(function() {
        $("#sidenav").animate({left: "-250px"}, 250,
                              function () { $(".sidenav-text").hide() });
        $("#main").animate({paddingLeft: "1%"}, 250);
        $("#head-wrap").animate({paddingLeft: "1%"}, 250);
    });
    $(".sidenav a").click(function() {
        $("#sidenav").css("left", "-250px");
        $("#main").css("paddingLeft", "1%");
        $("#head-wrap").css({"paddingLeft": "1%"});
    });
}
$(document).ready(main);
