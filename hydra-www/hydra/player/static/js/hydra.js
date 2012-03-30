function main(uri){
    /*$("#player").bind('ended', function(){
        // play next vido
        next();
    });*/
    var current = null;
    var interval_id;
    var guid = getCookie("guid");
    if (guid == undefined || guid == null){
        // show config form if there is no guid saved
        $("#device").show();
    } else {
        $("#status").show();
    }

    var socket = io.connect(uri);
    socket.on('reconnect', function () {
        console.log('System', 'Reconnected to the server');
    });

    socket.on('reconnecting', function () {
        console.log('System', 'Attempting to re-connect to the server');
    });

    socket.on('error', function (e) {
        console.log('System', e ? e : 'A unknown error occurred');
    });

    socket.on('connect', function () {
        console.log('System', 'Connected to the server');
        if (guid != undefined) {
            socket.emit("guid", guid);    
        }
    });

    socket.on('load', function(data){
        if (data != false && data.length != 0){
            if (data[0]['movie'] != current){
                play(data[0]['movie']); // set play list
                current = data[0]['movie'];    
            }
            $("#player").show();
            $("#status").hide();
            window.clearInterval(interval_id);
        }
    });

    $("#id_save").bind('click', function (){
        if ($("#device-assign").validate()){
            $("#device").hide();

            // generate and save guid
            guid = guidGenerator();
            setCookie("guid", guid, 365);
            $("#id_guid").val(guid);

            $.post('device', {'guid': guid, 'title': $("#id_title").val()}, 
                function(data) {
                    // emit signal to load a play list
                    socket.emit("guid", guid);
                }
            );

            $("#status").show();
            function check (guid, socket){
                if (guid){
                    socket.emit('guid', guid);
                }
            }

            interval_id = window.setInterval(function() {
                check(guid, socket);
            }, 10000);
            return true;
        }
    });
};
