var main = function() {
    $(".openbtn").click(function() {
        $("#sidenav").animate({left: "0"}, 250, function () { $(".sidenav-text").fadeIn() });
        $("#main").animate({marginLeft: "250px"}, 250);
    });
    $(".closebtn").click(function() {
        $("#sidenav").animate({left: "-250px"}, 250, function () { $(".sidenav-text").hide() });
        $("#main").animate({marginLeft: "1%"}, 250);
    });
}
$(document).ready(main);
