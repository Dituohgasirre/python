$(".btn-add-student").click(function(){
    $.get('/student/add', function(data, state) {
        layer.open({
            type: 1,
            title: "<strong>添加学生</strong>",
            area: ['600px', '450px'],
            content: data
        });
    });
});

$(".link-modify-student").click(function(){
    $.get($(this).attr('href'), function(data, state) {
        layer.open({
            type: 1,
            title: "<strong>编辑学生信息</strong>",
            area: ['600px', '450px'],
            content: data
        });
    });
    return false;
});

$(document).on('change', '#student-sid', function(){
    var sid=$(this).val()
    $.get('/student/getclass/sid/' + sid, function(data, state) {
        $("#student-cid").html(data)
    });
});

$(".btn-search").click(function() {
    var url = location.href;
    var i =  url.indexOf('search');
    if (i != -1) {
        url = url.substring(0, i);
    }
    if (url[url.length - 1] != '/') {
        url += "/"
    }
    url += "search/" + $("#search").val();
    location.href = encodeURI(url);
});
