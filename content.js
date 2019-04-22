//runs at the end of every page laod

//Extracts the protocl, domain and port from the url
var domain = location.protocol+'//'+location.hostname+(location.port ? ':'+location.port: '');

//chrome runtime function to send a message to the background script
chrome.runtime.sendMessage( {action: "capture", url: domain }, function(response) {

});
      