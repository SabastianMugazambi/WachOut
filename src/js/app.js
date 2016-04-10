// var dictionary = {
//   //edit this with the right pecentages
//   '0': 'Crime Rate:100% Theft:200%, GTA: 100%, Rape: 30%',
//   '0': 'Fellonies: 100 Burglaries: 200, GTA: 100, Robberies: 30',
  
// };
/*var bool = true;
if(bool == true){}*/

var globalLatitude;
var globalLongitude;

function success(pos) {
  console.log('lat= ' + pos.coords.latitude + ' lon= ' + pos.coords.longitude);
  globalLatitude = pos.coords.latitude;
  globalLongitude = pos.coords.longitude;

  var req = new XMLHttpRequest();
  //this would get the current geolocation but we are hardcoding for the sake of demo
  //req.open('GET','http://137.22.185.215:5000/'+ pos.coords.latitude + "/" + pos.coords.longitude, false);
  req.open('GET','http://137.22.185.215:5000/40.587/-74.164', false);

  req.send(null);
  var headers = req.getAllResponseHeaders().toLowerCase();
  console.log(headers);
  console.log(req.responseText);

  var dictionary = {
    //edit this with the right pecentages
    '0': String(req.responseText)
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
  
//We are doing buttons now*********************////////

  
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
  
  console.log("I am listening");
  var xmlHttp = new XMLHttpRequest();
                
   switch(e.payload.message) {
      case 4: 
       console.log("trying to press button");
       xmlHttp.open( "GET", "http://137.22.185.215:5000/getHelp.html/coord1=" + globalLatitude + "&coord2=" + globalLongitude);
       console.log(xmlHttp.responseText);
          break;
      case 2:   
       console.log("pressing the top button");
       xmlHttp.open( "GET", "http://137.22.185.215:5000/getHelp.html/coord1=" + globalLatitude + "&coord2=" + globalLongitude);
       console.log(xmlHttp.responseText);   
       break;
      case 6:  
       console.log("pressing the bottom button for a longer time");
       xmlHttp.open( "GET", "http://137.22.185.215:5000/getHelp.html/coord1=" + globalLatitude + "&coord2=" + globalLongitude);
       console.log(xmlHttp.responseText);   
       break;
      default:
          console.log('Case Default / Error');        
        } 
   xmlHttp.send(null);
    
  }); 

setInterval(navigator.geolocation.getCurrentPosition(success, error, options), 10,000);


  
 /* void app_init(void) {
  ...
  window_set_click_config_provider(&window, (ClickConfigProvider) config_provider);
  ...
}
  void config_provider(Window *window) {
  ButtonId id = BUTTON_ID_SELECT;
  windows_single_click_subscribe(id, select_single_click_handler);
}
void select_single_click_handler(ClickRecognizerRef recognizer, void *context) {
  ... called on single click, and every 1000ms of being held ...
  var xmlHttp = new XMLHttpRequest();
  request.onload = function() {
  // The request was successfully completed!
  console.log('Got response: ' + this.responseText);
};
  xmlHttp.open( "GET", "http://localhost:8080/"+pos.coords.latitude+"?"+pos.coords.latitude);
  request.send();
}*/

/*
  void config_provider(Window *window) {
  ButtonId id_down = BUTTON_ID_DOWN;
  windows_single_click_subscribe(id_down, down_single_click_handler);
}
void up_single_click_handler(ClickRecognizerRef recognizer, void *context) {
  bool = true;
}

  void config_provider(Window *window) {
  ButtonId id_up = BUTTON_ID_UP;
  windows_single_click_subscribe(id_up, up_single_click_handler);
}`

});*/