<!DOCTYPE html>
<head>

<title>Rebux Deposit</title>

<link rel="stylesheet" href="await_locker_close.css" />

</head>

<body>

<h1>AWAITING DEPOSIT TERMINAL CLOSURE</h1>

<div class="container">
  <div class="dot dot-1"></div>
  <div class="dot dot-2"></div>
  <div class="dot dot-3"></div>
</div>

<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
  <defs>
    <filter id="goo">
      <feGaussianBlur in="SourceGraphic" stdDeviation="10" result="blur" />
      <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 21 -7"/>
    </filter>
  </defs>
</svg>

<a href="./chlogout.php" class="next round">&#8250;</a>

</body>

<?php

//Hashing Expected Values of Locker ID, for Cookie Comparison
$hashVal101 = openssl_digest("101", "sha256");
$hashVal102 = openssl_digest("102", "sha256");
$hashVal103 = openssl_digest("103", "sha256");
$hashVal104 = openssl_digest("104", "sha256");
$hashVal105 = openssl_digest("105", "sha256");
$hashVal106 = openssl_digest("106", "sha256");
$hashVal107 = openssl_digest("107", "sha256");
$hashVal108 = openssl_digest("108", "sha256");
$hashVal109 = openssl_digest("109", "sha256");

$hashValArray = array(101 => $hashVal101, 102 => $hashVal102, 103 => $hashVal103, 104 => $hashVal104, 105 => $hashVal105, 106 => $hashVal106, 107 => $hashVal107, 108 => $hashVal108, 109 => $hashVal109);

//Read Cookies
$phpVarUserID = $_COOKIE['User_Id'];
$phpVarLockerID = $_COOKIE['Locker_Id'];

//Comparing hash cookie retriced and hash expected value stored in array
$finalPhpVarLockerID = array_search($phpVarLockerID,$hashValArray,true);

$output = shell_exec("python3 /home/pi/RebuxRepo/BingXian/Locking Mechanism/DetectClosure.py "  .$phpVarUserID  .$finalPhpVarLockerID);

echo $output

?>
