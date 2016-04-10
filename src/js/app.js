// var dictionary = {
//   //edit this with the right pecentages
//   '0': 'Crime Rate:100% Theft:200%, GTA: 100%, Rape: 30%',
//   '0': 'Fellonies: 100 Burglaries: 200, GTA: 100, Robberies: 30',
  
// };


function success(pos) {
  console.log('lat= ' + pos.coords.latitude + ' lon= ' + pos.coords.longitude);
  
   var req = new XMLHttpRequest();
  req.open('GET','http://137.22.185.215:5000/', false);
    req.send(null);
    var headers = req.getAllResponseHeaders().toLowerCase();
    console.log(headers);
    console.log(req.responseText);
  
  var finalForPebble = '';
   var original = req.responseText;
   var splitOriginal = original.split(",");
  //finalForPebble = splitOriginal[0]+' '+splitOriginal[2]+', 'splitOriginal[3]+', '+ splitOriginal[7];
  finalForPebble = splitOriginal[0]+' ' + splitOriginal[2];
  //finalForPebble += splitOriginal[2] + '\n';
  //finalForPebble += splitOriginal[3] + '\n';
  //finalForPebble += splitOriginal[4] + '\n';
  //finalForPebble += ' '+splitOriginal[3]+',';
  //finalForPebble += ' '+splitOriginal[7];
  console.log(finalForPebble)
   var dictionary = {
  //edit this with the right pecentages
     '0': 'Fellonies: 100 Burglaries: 200, GTA: 100, Robberies: 30',
     '1': 'second word'
    };
  Pebble.sendAppMessage(dictionary);
        
}





function error(err) {
  console.log('location error (' + err.code + '): ' + err.message);
}

// Choose options about the data returned
var options = {
  enableHighAccuracy: true,
  maximumAge: 10000,
  timeout: 10000
};



// Request current position

// getWeather is called when my watchface is opened and when an AppMessage is received
// Listen for when the watchface is opened
Pebble.addEventListener('ready', 
  function(e) {
    //console.log("PebbleKit JS ready!");
    // Get the initial weather
    //getWeather();
    navigator.geolocation.getCurrentPosition(success, error, options); 
  }
);

Pebble.addEventListener("appmessage", function(e) {

/*
Case:
1-up
2-long up
3-select
4-long select
5-down
6-long down
*/
  
  
 var xmlHttp = new XMLHttpRequest();
                
 switch(e.payload.message) {
   
    case 1:        
     xmlHttp.open( "GET", "http://localhost:8080/");
        break;
    case 2:        
        xmlHttp.open( "GET", "http://192.168.178.31/?run=lichtaus");
        break;
    case 3:          
        xmlHttp.open( "GET", "http://192.168.178.31:8080/jsonrpc?request=%7B%22jsonrpc%22%3A+%222.0%22%2C+%22method%22%3A+%22Player.PlayPause%22%2C+%22params%22%3A+%7B+%22playerid%22%3A+1+%7D%2C+%22id%22%3A+1%7D");
        break;
    case 4:        
        break;
    case 5:        
        xmlHttp.open( "GET", "http://192.168.178.31/?run=tvan");
        break;
    case 6:        
        xmlHttp.open( "GET", "http://192.168.178.31/?run=tvaus");
        break;
    default:
        console.log('Case Default / Error');        
      } 
  
 xmlHttp.send(null);
  
});
