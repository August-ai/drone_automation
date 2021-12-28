var arDrone = require('ar-drone');
var http    = require('http');


console.log('Connecting to drone video stream ...');

// Create client
var client = arDrone.createClient();
client.takeoff();


// Get PNG stream
var pngStream = client.getPngStream();


var lastPng;
var num = 0
var rep = 0
const fs = require('fs')
const request = require('request')

// const download = (url, path, callback) => {
// 		request.head(url, (err, res, body) => {
//    			request(url)
//      			.pipe(fs.createWriteStream(path))
//      			.on('close', callback)
//	  	})
//	}




pngStream
    .on('error', function(error){
        console.log("Error occurred: " + error);
    })
    .on('data', function(pngBuffer) {
        lastPng = pngBuffer;
    });


var server = http.createServer(function(req, res) {
    if (lastPng) {
        // Declare content type, in this case we want image/png

	res.writeHead(200, {'Content-Type': 'image/png'});


		var path = './images/image';
		var end = '.png';
		const url = 'http://localhost:8000/';
		num = num +1;
		Snum = num.toString();

		var path = path.concat(Snum);
		var path = path.concat(end);

//		console.log("New orders given to drone");

		eval(fs.readFileSync('commands.js')+'', function(err, data){
         if (err) throw err;
        });
        filename = 'commands.js';

        fs.readFile(filename, 'utf8', function(err, data) {
        if (err) throw err;
            console.log('OK: ' + filename);
            console.log(data)
        });
//	download(url, path, () => {
//  			console.log('image grabbed')
//	})

	res.end(lastPng);

    }else{
        res.writeHead(503);
        res.end('No stream data recieved.');
    }
});

server.listen(8000, function() {
    console.log('Serving latest png on port 8000 ...');
});


