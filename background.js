//list of websites to be captured
var websites = [ "https://www.google.com", "https://www.youtube.com", "https://www.cnn.com"];


//function to check if the domain is listed in the websites array and to take a screenshot
function capture( url ){
  if( websites.includes(url) )
  {

    //chrome tabs functions to take a screenshot of the visible content. By default it takes the screenshot of
    // the current tab. The image format is jpeg by default. it convets the image into Base64 encoded string
    // and passes it to the callback functions which then converts the base64string into a non inline-able resource
    // and so the window.open() function forces a dialogue box.
    chrome.tabs.captureVisibleTab(null, function(img) {
      var url = img.replace(/^data:image\/[^;]+/, 'data:application/octet-stream');
	  var img = new Image;
		img.src = url;
		console.log(img);
      window.open(url);
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