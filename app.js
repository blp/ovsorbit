var main = function() {
    $(".openbtn").click(function() {
        $("#sidenav").animate({left: "0"}, 250, function () { $(".sidenav-text").fadeIn() });
        $("#main").animate({paddingLeft: "250px"}, 250);
        $("#head").animate({paddingLeft: "250px"}, 250);
    });
    $(".closebtn").click(function() {
        $("#sidenav").animate({left: "-250px"}, 250,
                              function () { $(".sidenav-text").hide() });
        $("#main").animate({paddingLeft: "1%"}, 250);
        $("#head").animate({paddingLeft: "1%"}, 250);
    });
    $(".sidenav a").click(function() {
        if ($(document).width() < 800) {
            $("#sidenav").css("left", "-250px");
            $("#main").css("paddingLeft", "1%");
            $("#head").css({"paddingLeft": "1%"});
        }
    });
    function search(target) {
        target = target.toLowerCase();
        for (var i = 1; ; i++) {
            var ptr = $("#pe" + i);
            if (!ptr.length) {
                break;
            }
            if ($("#e" + i).text().toLowerCase().indexOf(target) >= 0) {
                ptr.show();
            } else {
                ptr.hide();
            }
        }
        if (target == '') {
            $("#episodes").text("Episodes");
        } else {
            $("#episodes").text("Search results:");
        }
    }
    $("#search").on('input', function() { search($("#search").val()); });
}
$(document).ready(main);
