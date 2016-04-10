$(function () {
	var locate = window.location;
	document.coordinate.information.value = locate;
	var text = document.coordinate.information.value;
	console.log(text);
	alert(text);

	function coordinate1Retrieval(str) {
		theleft = str.indexOf("=") + 1;
		theright = str.lastIndexOf("&");
		return(str.substring(theleft, theright));
	}

	function coordinate2Retrieval(str) {
		point = str.lastIndexOf("=");
		return(str.substring(point+1,str.length));
	}

	var GPScoordinate1 = coordinate1Retrieval(text);
	var GPScoordinate2 = coordinate2Retrieval(text);

	$("#coordinateStatement").html("Your friend is in danger! They last transmitted at these coordinates: " + GPScoordinate1 + ", " + GPScoordinate2);


	setTimeout(function() {
		window.reload()
	}, 10);
	
	

});
