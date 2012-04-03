function play(path){
    // detemine supported extension
    var extension = Modernizr.video.h264 ? 'mp4': 
                    Modernizr.video.webm ? 'webm': 'mp4';

    // remove extension
    var name = path.substr(0, path.lastIndexOf('.')) || path;
    
    $('video').remove();

    var t = $('<video id="player" class="player" width="100%" height="100%" loop></video>');
    $("body").append(t);

    $("video")[0].type = "video/" + extension;
    $("video")[0].src = name + "." + extension;
    $("video")[0].load();
    $("video")[0].play();    
}