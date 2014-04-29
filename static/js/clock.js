function time() {

  var now = new Date();
//  var hour = now.getHours();
//  var ampm = "AM";
//  hour -= 4;
  var today = now.getDay();
/*  if (hour < 0) {
    hour += 24;
    today--;
    if (today < -1) {
      today = 6;
    }
  }
  if (hour >= 12) {
    ampm = "PM";
  }
  hour %= 12;
  if (hour == 0) {
    hour = 12;
  }
  
  var min = now.getMinutes();
  if (min < 10) {
    min = "0" + min;
  }
  
  var sec = now.getSeconds();
  if (sec < 10) {
    sec = "0" + sec;
  }
  */
  var weekday = new Array(7);
  weekday[0]="Sunday";
  weekday[1]="Monday";
  weekday[2]="Tuesday";
  weekday[3]="Wednesday";
  weekday[4]="Thursday";
  weekday[5]="Friday";
  weekday[6]="Saturday";

  var day = weekday[today];

  //clock.innerHTML = hour + ":" +  min + ":" + sec + " " + ampm;
  document.getElementById("clock").innerHTML = now.toLocaleTimeString();
  document.getElementById("date").innerHTML = day + ", " + now.toLocaleDateString();
}

time();
