var io = require('socket.io').listen(8080);
io.enable('browser client minification'); // send minified client
io.enable('browser client etag'); // apply etag caching logic based on version number
io.enable('browser client gzip'); // gzip the file
//io.set('log level', 1); // reduce logging
io.set('transports', [ // enable all transports (optional if you want flashsocket)
    'websocket'
  , 'flashsocket'
  , 'htmlfile'
  , 'xhr-polling'
  , 'jsonp-polling'
]);

var playlists = {
  'bb8c1ed8-cc24-332f-ace8-ed45b612d500': [
    "/static/media/big_buck_bunny_640x360_2.28", 
    "/static/media/sintel_640x360_2.28",
    "/static/media/elephants_dream_640x360_2.30"
  ],
  '420c6daa-ce2b-afd8-64eb-378d8684b9b7': [
    "/static/media/sintel_640x360_2.28",
    "/static/media/elephants_dream_640x360_2.30"
  ],
  '27831633-0bed-1a37-720a-8bda42305990': [
    "/static/media/sintel_640x360_2.28",
  ]
};

io.sockets.on('connection', function (socket) {
    socket.on('load', function (guid, fn) {
        var list = playlists[guid];
        if (list != undefined){
          fn(list);
        } else {
          fn(false);
        }
    });
    //socket.emit('set', {list: videoSourceList});
});
