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
    // dont net to update if is same play list
    if (!$(playlist).compare(data)) {
        playlist = data;
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

    var guid = store.get('guid');
    if (guid == undefined){
        // show config form if there is no guid saved
        $("#config").show();
    }

    var socket = io.connect(uri);
    socket.on('connect', function () {
        //message("System", "connected!");
        if (guid != undefined) {
            socket.emit("load", guid, function (data){
            if (data){
                set(data); // set play list
                $("#player").show();
                $("#status").hide();
            } else {
                $("#status").html("Waiting for a play list to " + guid);
                //message("Client", "no play list found!");
            }
        });    
        }        
    });

    socket.on('reconnect', function () {
        //message('System', 'Reconnected to the server');
    });

    socket.on('reconnecting', function () {
        //message('System', 'Attempting to re-connect to the server');
    });

    socket.on('error', function (e) {
        //message('System', e ? e : 'A unknown error occurred');
    });

    function message (from, msg) {
        console.log(from, msg);
    }

    $("#config").bind('submit', function (){
        $("#config").hide();

        // generate and save guid
        guid = guidGenerator();
        store.set('guid', guid);

        // emit signal to load a play list
        socket.emit("load", guid, function (data){
            if (data != false){
                set(data); // set play list
                $("#player").show();
                $("#status").hide();
            } else {
                $("#status").html("Waiting for a play list to " + guid);
                //message("Client", "no play list found!");
            }
        });
        return false;
    });
};