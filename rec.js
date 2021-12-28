var arDrone = require('ar-drone');
var http    = require('http');


// Create client
var client = arDrone.createClient();


//// Get PNG stream
//var pngStream = client.getPngStream();


var lastPng;

const fs = require('fs')
const request = require('request')

//pngStream
//    .on('error', function(error){
//        console.log("Error occurred: " + error);
//    })
//    .on('data', function(pngBuffer) {
//        lastPng = pngBuffer;
//    });

eval(fs.readFileSync('commands.js')+'', function(err, data){
 if (err) throw err;
});
filename = 'commands.js';

fs.readFile(filename, 'utf8', function(err, data) {
if (err) throw err;
    console.log('OK: ' + filename);
    console.log(data)
});


