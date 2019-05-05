window.onload = function(){
  
  //Extracts the protocol, domain and port from the url  
  var domain = location.protocol+'//'+location.hostname+(location.port ? ':'+location.port: '');
  

  //chrome runtime function to send a message to the background script
  chrome.runtime.sendMessage( {action: "capture", url: domain }, function(response) {
  
   var  visited_link=domain;
   console.log("link visited is: " + visited_link);
  });

  

  


}
      