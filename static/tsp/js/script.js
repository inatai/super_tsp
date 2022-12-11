$(function(){
    $("#response").html("Response Values");

    $("#button").click( function(){
        var url = $("#url_post").val();

            var JSONdata = {
                value1: $("#value1").val(),
                value2: $("#value2").val()      
            };

        alert(JSON.stringify(JSONdata));

        $.ajax({
            type : 'post',
            url : url,
            data : JSON.stringify(JSONdata),
            contentType: 'application/JSON',
            dataType : 'JSON',
            scriptCharset: 'utf-8',
            success : function(data) {

                // Success
                alert("success");
                alert(JSON.stringify(data));
                $("#response").html(JSON.stringify(data));
            },
            error : function(data) {

                // Error
                alert("error");
                alert(JSON.stringify(data));
                $("#response").html(JSON.stringify(data));
            }
        });
    })
})