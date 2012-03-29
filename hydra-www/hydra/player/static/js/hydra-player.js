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