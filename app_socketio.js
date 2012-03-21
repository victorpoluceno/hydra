var io = require('socket.io').listen(9000);
var sqlite3 = require('sqlite3').verbose();

var db = new sqlite3.Database('hydra/hydra.db');

db.each("SELECT m.* FROM player_device d, player_playlist p, " +
      "player_playlistmovie pl, player_movie m " +
      "where d.guid=8898 and d.playlist_id=p.id and "+
      "pl.playlist_id=p.id and m.id=pl.movie_id and "+
      "d.playlist_id!=null", function(err, row) {
    if (err != null){
      console.log(err);  
    }
    console.log(row);
});

db.close();

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
