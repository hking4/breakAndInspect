//list of websites to be captured
var websites = [ "https://www.google.com", "https://www.facebook.com","https://stackoverflow.com" ];

//function to download a UrlData and also accepts a name for the file
function downloadURI(uri, name) {
  var link = document.createElement("a");
  link.download = name;
  link.href = uri;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  delete link;
}

//function to check if the domain is listed in the websites array and to take a screenshot
function capture( url ){
  if( websites.includes(url) )
  {
    //Injecting files into the browser one after the other. The second file is in the callback of first file injection as it uses the functions in the first file
    chrome.tabs.executeScript({
      file: 'js/html2canvas.min.js'
     
    }, function(){
      chrome.tabs.executeScript({
        file: 'js/takess.js'
      })
      console.log(url);
    });
  }

}


//function that listens for incoming message and acts as per the request
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    
    if (request.action == "capture")
    {
      capture( request.url );
    }
  
  }
);