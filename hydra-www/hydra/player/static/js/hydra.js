function set_current(path){
    var extension = Modernizr.video.h264 ? 'mp4': 
                    Modernizr.video.webm ? 'webm': 
                                           'mp4';    
    current = path;
    $("video")[0].src = path + "." + extension;
    $("video")[0].type = "video/" + extension;
    $("video")[0].load();
}

function first(){
    set_current(playlist[0])
    $("video")[0].play();
}

function next(){
    var index = playlist.indexOf(current);
    if (index == playlist.length-1){ // end of play list?
        path = playlist[0];
    } else {
        // next video
        path = playlist[index+1];
    }

    set_current(path);
    $("video")[0].play();    
}

function set(data){
    var list = Array();
    for (var i=0; i < data.length; i++){
      var input = data[i];
      list.push(input.substr(0, input.lastIndexOf('.')) || input);
    }

    // dont net to update if is same play list
    if (!$(playlist).compare(list)) {
        playlist = list;
        first();
    }
}

function main(uri){
    playlist = null;
    current = null;

    $("#player").bind('ended', function(){
        // play next vido
        next();
    });

    //var guid = window.localStorage.getItem('guid');
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
        //message("System", "connected!");
        if (guid != undefined) {
            socket.emit("load", guid, function (data){
            if (data && data.length != 0){
                set(data); // set play list
                $("#player").show();
                $("#status").hide();
            } else {
                //$("#status").html("Waiting for a play list to " + guid);
                console.log(guid);
                $("#status").show();
                //message("Client", "no play list found!");
            }
        });    
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
    		socket.emit("load", guid, function (data){
    		    if (data != false && data.length != 0){
    	           set(data); // set play list
    	           $("#player").show();
    	           $("#status").hide();
    		    } else {
    	           //$("#status").html("Waiting for a play list to " + guid);
    	           $("#status").show();
    	           //message("Client", "no play list found!");
    		    }
    		});
            return true;
        } else {
            return false;
        }
    });
};
