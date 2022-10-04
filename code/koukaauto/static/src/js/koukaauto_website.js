odoo.define('koukaauto.koukaauto_website', function (require) {
    "use strict";

    $(".mark").change(function(){            
        $('.model').empty();       
        var selectedmark = $(this).children("option:selected").val();
        $.ajax({
            type: "POST",
            dataType: 'json',
            url: '/koukaauto/mark/',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({'jsonrpc': "2.0", 'method': "call", "params": {'selectedmark': selectedmark}}),
            success: function (data) {               
                if (data.result){
                    $('.model').append($("<option></option>"));
                    var model = data.result.map(function(model){
                            $('.model').append($("<option></option>").attr("value", model.id).text(model.name));
                    });
                }
            },
            error: function (data) {
                console.error("ERROR ", data);
            },
        });

    });
    
    $(".model").change(function(){            
        $('.finition').empty(); 
        var selectedmodel = $(this).children("option:selected").val();
        $.ajax({
            type: "POST",
            dataType: 'json',
            url: '/koukaauto/model/',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({'jsonrpc': "2.0", 'method': "call", "params": {'selectedmodel': selectedmodel}}),
            success: function (data) {  
                if (data.result){
                    $('.finition').append($("<option></option>"));
                    var model = data.result.map(function(finition){
                            $('.finition').append($("<option></option>").attr("value", finition.id).text(finition.name));
                    });
                }
            },
            error: function (data) {
                console.error("ERROR ", data);
            },
        });
    });
});