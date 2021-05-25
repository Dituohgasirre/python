$(document).ready(function(){
    $("#rtop").hide();
    // console.log($("#prev_tool").height());
    // console.log($("body").height() / 10);
    var top = ($("body").height() / 10 + 300) / 2;
    // console.log(top);
    $("#prev_tool").css("top", top +"px");
    $("#next_tool").css("top", top +"px");

    $(".right_tool_list").click(function(){
        if ($("#right_list").hasClass("hide"))
            $("#right_list").addClass("show");
        if ($("#header").hasClass("slideUp"))
            $("#right_list").css("top", "0");
        else
            $("#right_list").css("top", "50px");
        $("#right_list").toggleClass("slideRight");
        $("#right_list").toggleClass("slideLeft");
    });

    $("#rtop").click(function(){
        $("html body").animate({scrollTop: 0}, 280);
        // window.scrollTo(0, 0);
        $(this).hide();
    });

    $(document).popover({
      'content': '<img src="brcode.png" style="width:120px; height:120px;">',
      'html': true,
      'selector': '.barcode',
      'trigger': 'hover',
      'placement': 'left',
    });
});

$(document).scroll(function() {
    // console.log($(this), $(this).scrollTop(), $(window).height() / 2)
    if ($(this).scrollTop() > $(window).height() / 2) {
        $("#rtop").show();
    } else {
        $("#rtop").hide();
    }

});

$(document).on('click', '.blog-link', function() {
    var link = $(this).attr("data-link");
    if (link) {
    // console.log($(this).attr("data-link"))
        location.href = $(this).attr("data-link");
    }
});

var elem = document.getElementById("header");
var headroom = new Headroom(elem, {
  "tolerance": 5,
  "offset": 205,
  "classes": {
    "initial": "animated",
    "pinned": "slideDown",
    "unpinned": "slideUp"
  }
});
headroom.init();

