//global map variable
var map;

function init() {
	  //setup the search button
    document.getElementById("searchBtn").addEventListener("click", search);

    //setup leaflet map
    map = L.map ("map1");

    //credit OpenStreetMap
    var attrib="Map data copyright OpenStreetMap contributors, Open Database Licence";

    L.tileLayer
    ("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
        { attribution: attrib } ).addTo(map);

    //on initial setup of the map, check if the user has location on
    if(navigator.geolocation)
    {
    	//only set the map to look at their position on setup
        navigator.geolocation.getCurrentPosition (
            gpspos=> {
				        //set map view to their position
                map.setView([gpspos.coords.latitude, gpspos.coords.longitude], 14);
            },
            err=> {
            	//display error message
                alert(`You must enable location in order to fully utilise the map.`);
                //default map location if the user denies location
                map.setView([50.908,-1.4], 14);
            }
        );
    }
    else
    {
        //default map location if the user turns off GPS
        map.setView([50.908,-1.4], 14);
    }
}


//define search function
function search() {
    // Read in the input from the form
    var location = document.getElementById('location').value;

    // Set up the AJAX connection variable
    var ajaxConnection = new XMLHttpRequest();

    // Set up the callback function. Here, the callback is an arrow function.
    ajaxConnection.addEventListener("load", e => {
        var output = ""; // initialise output to blank text

        //checks for confirmation
        if (e.target.status == 200){
          var response = JSON.parse(e.target.responseText);
          //fetch default JSON responses
          var locationResponse = response.location;
          var current = response.current;

          //retrieve search term coordinates
          var latitude = locationResponse.lat;
          var longitude = locationResponse.lon;
          //centre map on search
          map.setView([latitude, longitude], 14);

          //fetch "condition" JSON object
          var condition = current.condition;
          var is_day = condition.is_day;
          var weather_code = condition.code;
          var loc = document.location.pathname;
          var icon_path = loc.substring(0, loc.lastIndexOf('/')) + "/weather/64x64/";
          // add the details to the output variable
          output = `Location: ${locationResponse.name} <br/>
                Last updated: ${current.last_updated} <br/>
                Temperature: ${current.temp_c}&deg;C <br/>
                Feels like: ${current.feelslike_c}&deg;C <br/>
                Precipitation: ${current.precip_mm}mm <br/>
                Humidity: ${current.humidity}% <br/>
                Current weather: ${condition.text}`;

          //icon logic
          if (is_day == 1){
            icon_path += `day/${weather_code}.png`;
          }
          else {
            icon_path += `night/${weather_code}.png`;
          }
          //add icon to output variable
          output += `<img src=${icon_path}>`;

          // Put the HTML output into the response div
          document.getElementById("response").innerHTML = output;
        }
        else if (e.target.status == 404){
          //if it errors display error message
          alert(`WeatherAPI call unsuccessful.`);
        }
    });

    // Open the connection to weather API
    ajaxConnection.open("GET", `http://api.weatherapi.com/v1/current.json?key=39f72f12b939426793c63540201011&q=${location}`);
    // Send the request.
    ajaxConnection.send();
}
