// https://node-irc.readthedocs.io/en/latest/API.html
// node-irc api documentation

npm install irc
// Library provides basic IRC client functionality

// See https://github.com/martynsmith/node-irc for examples



// Connect to an IRC server:
var irc = require('irc');
var client = new irc.Client('irc.yourserver.com', 'myNick', {
    channels: ['#channel'],
});

//note format of irc.Client(server, nick[, options])
//irc.Client represents a single nick connected to a single IRC server.
// Other options include:
{
    userName: 'nodebot',
    realName: 'nodeJS IRC client',
    port: 6667,
    localAddress: null,
    debug: false,
    showErrors: false,
    autoRejoin: false,
    autoConnect: true,
    channels: [],
    secure: false,
    selfSigned: false,
    certExpired: false,
    floodProtection: false,
    floodProtectionDelay: 1000,
    sasl: false,
    retryCount: 0,
    retryDelay: 2000,
    stripColors: false,
    channelPrefixes: "&#",
    messageSplit: 512,
    encoding: ''
}

//Commands:
//See documentation https://node-irc.readthedocs.io/en/latest/API.html for more commands

//join channel:
client.join('#yourchannel yourpass');

//leave channel:
client.part('#yourchannel');

// message channel:
client.say('#yourchannel', "I'm a bot!");

// Log all messages:
client.addListener('message', function (from, to, message) {
    console.log(from + ' => ' + to + ': ' + message);
});

//Log direct messages to bot itself
client.addListener('pm', function (from, message) {
    console.log(from + ' => ME: ' + message);
});

//Log messages from particular channel:
client.addListener('message#yourchannel', function (from, message) {
    console.log(from + ' => #yourchannel: ' + message);
});

// Flood Protection so that the bot can not be spammed e.g. with malicious requests:
Client.activateFloodProtection([interval])

//Log "error" event:
client.addListener('error', function(message) {
    console.log('error: ', message);
});

//EventEmitters also an option
