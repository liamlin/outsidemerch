$(document).ready(function() {

var date = new Date(); // current date-time


/*

NEEDS TO BE SET TO ROUND TO 5 MINUTE STRING 
EX: 12:10 = '1210'

*/
function roundMinutes(date) {

    date.setHours(date.getHours() + Math.round(date.getMinutes()/60));
    date.setMinutes(0);

    return date;
}




var moveWindow = function() {
	window.location.hash=roundMinutes(date);
	};



/* roundMinutes(date); // 5:00 */


});