function main(uri){
    playlist = null;
    current = null;

    $("#player").bind('ended', function(){
        // play next vido
        next();
    });

    var guid = getCookie("guid");
    if (guid == undefined || guid == null){
        // show config form if there is no guid saved
        $("#device").show();
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
        alert('load');
        if (data != false && data.length != 0){
           set(data); // set play list
           $("#player").show();
           $("#status").hide();
        } else {
           $("#status").show();
        }
    });

    $("#device-assign").bind('submit', function (){
        if ($("#device-assign").validate()){
    		$("#device").hide();

            // generate and save guid
            guid = guidGenerator();
            setCookie("guid", guid, 365);
            $("#id_guid").val(guid);

    		// emit signal to load a play list
    		socket.emit("guid", guid);
            return true;
        } else {
            return false;
        }
    });
};
