var io = require('socket.io').listen(9000);
var sqlite3 = require('sqlite3').verbose();

var db = new sqlite3.Database('hydra/hydra.db');

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

io.sockets.on('connection', function (socket) {
    socket.on('load', function (guid, fn) {
	var list = new Array();

	db.each("SELECT m.original_file, pl.sort FROM player_movie m, " +
	      "player_playlist p, " +
	      "player_playlistmovie pl, " +
	      "player_device d " +
	      "WHERE m.id=pl.movie_id and pl.playlist_id=p.id and " +
	      "d.playlist_id=p.id and d.guid=? ", guid,
	    function(err, row) {
	    if (err != null){
	        console.log(err);  
	        console.log(row);  
	    }
	    if (row){
	        console.log(row);
                list.push("media/player/" + row.original_file);
            }
	}, function (){
       	        console.log(list);
		fn(list);
	    }
	);
    });
    //socket.emit('set', {list: videoSourceList});
});

//db.close();
