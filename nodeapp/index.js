var webshot = require("webshot");
var websites=["www.cnn.com","www.facebook.com","www.twiter.com"]

var options = {
    streamType: "jpeg",
    windowSize:{
        width:2024,
        height: 786
    },
    shotSize:{
        width:"all",
        height: "all" 
    }
};

webshot(websites[1], "ourcodeworld-file.jpeg", options, (err) => {
    if(err){
        return console.log(err);
    }

    console.log("Image succesfully created");
});