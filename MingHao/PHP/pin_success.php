<!DOCTYPE html>
<head>

<title>Rebux Deposit</title>

<link rel="stylesheet" href="pin_success.css" />

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js"></script>
<script type= "text/javascript">

jQuery(document).ready(function($) {
  $(document).ready(function() {

   const params = new URLSearchParams(window.location.search)
   
   //Retrival of Hashed Value from Query String
   var lockerRetrived = params.get('locker')
   
   //Hashing the various expected values 
   var hashVal101 = CryptoJS.SHA256("101")
   var hashVal102 = CryptoJS.SHA256("102")
   var hashVal103 = CryptoJS.SHA256("103")
   var hashVal104 = CryptoJS.SHA256("104")
   var hashVal105 = CryptoJS.SHA256("105")
   var hashVal106 = CryptoJS.SHA256("106")
   var hashVal107 = CryptoJS.SHA256("107")
   var hashVal108 = CryptoJS.SHA256("108")
   var hashVal109 = CryptoJS.SHA256("109")
 
   var unavailHashVal = CryptoJS.SHA256("unavailable")
   
   if (lockerRetrived == hashVal101) {
   document.getElementById("S-101").removeAttribute("hidden");
   }

   else if (lockerRetrived == hashVal102) {
   document.getElementById("S-102").removeAttribute("hidden");
   }

   else if (lockerRetrived == hashVal103) {
   document.getElementById("S-103").removeAttribute("hidden");
   }

   else if (lockerRetrived == hashVal104) {
   document.getElementById("M-104").removeAttribute("hidden");
   }

   else if (lockerRetrived == hashVal105) {
   document.getElementById("M-105").removeAttribute("hidden");
   }

   else if (lockerRetrived == hashVal106) {
   document.getElementById("M-106").removeAttribute("hidden");
   }

   else if (lockerRetrived == hashVal107) {
   document.getElementById("L-107").removeAttribute("hidden");
   }

   else if (lockerRetrived == hashVal108) {
   document.getElementById("L-108").removeAttribute("hidden");
   }

   else if (lockerRetrived == hashVal109) {
   document.getElementById("L-109").removeAttribute("hidden");
   }

   else if (lockerRetrived == unavailHashVal) {
   document.getElementById("LockersUnavailable").removeAttribute("hidden");
   document.getElementById("main_heading").innerHTML = "OUR APOLOGIES";
   document.getElementById("main_sub").innerHTML = "As all of our Lockers are currently in use. We apologise for not being able to serve you. Please come back again. Thank You.";
   document.getElementById("main_button").innerHTML = "Back to Home Menu";
   document.getElementById("main_button").setAttribute('onclick','window.location.href="./index.php";')
   }
   
   else {
   window.alert("ERROR! PLEASE DO NOT TAMPER WITH LINK OF KIOSK! THANK YOU.");
   window.location.replace("./pin_input.php");
   }

  });
});

</script>
</head>

<body>

<section class="section__img" id="S-101" hidden>
  <img src="https://i.pinimg.com/474x/57/c8/29/57c82965e04874d4c836715d661f65b8.jpg" alt="Head to Locker S-101." width="600" height="600">
</section>

<section class="section__img" id="S-102" hidden>
  <img src="https://i.pinimg.com/474x/12/90/c3/1290c353f5b0e660fe600d4c17d15787.jpg" alt="Head to Locker S-102." width="600" height="600">
</section>

<section class="section__img" id="S-103" hidden>
  <img src="https://i.pinimg.com/474x/b4/b7/1f/b4b71feb2b0c536140ed42379a784111.jpg" alt="Head to Locker S-103." width="600" height="600">
</section>

<section class="section__img" id="M-104" hidden>
  <img src="https://i.pinimg.com/474x/bf/0a/b2/bf0ab264d7348d347821f78168ba9e6c.jpg" alt="Head to Locker M-104." width="600" height="600">
</section>

<section class="section__img" id="M-105" hidden>
  <img src="https://i.pinimg.com/474x/da/e2/fd/dae2fdbd1cfe5db712b6759dddde8c8e.jpg" alt="Head to Locker M-105." width="600" height="600">
</section>

<section class="section__img" id="M-106" hidden>
  <img src="https://i.pinimg.com/474x/c1/23/0b/c1230b5bf8ad7a23f7fdea37899a0141.jpg" alt="Head to Locker M-106." width="600" height="600">
</section>

<section class="section__img" id="L-107" hidden>
  <img src="https://i.pinimg.com/474x/9a/fb/e5/9afbe575e6cec02c35f8049554aba68b.jpg" alt="Head to Locker L-107." width="600" height="600">
</section>

<section class="section__img" id="L-108" hidden>
  <img src="https://i.pinimg.com/474x/2c/6b/97/2c6b973a44566b53e6fdc14603beec5f.jpg" alt="Head to Locker L-108." width="600" height="600">
</section>

<section class="section__img" id="L-109" hidden>
  <img src="https://i.pinimg.com/474x/75/c4/ba/75c4ba6915f70cd68b270e44e1e31254.jpg" alt="Head to Locker L-109." width="600" height="600">
</section>

<section class="section__img" id="LockersUnavailable" hidden>
  <img src="https://i.pinimg.com/564x/15/65/f9/1565f9879b63609a65554eff0a925ae7.jpg" alt="Head to Locker L-109." width="600" height="600">
</section>

<main class="[ flow ] [ main ]">
  <h2 class="main__heading" id="main_heading">PROCEED TO LOCKER</h2>
  <p class="main__sub" id="main_sub">Please head to the Designated Locker that is reflected on the Image shown, for Item Deposit. Kindly close the Locker Door after use.</p>
  <button class="main__button" id="main_button" onclick="window.location.href='./await_locker_close.php'">Understood</button>
</main>

</body>

<?php

//Retrival of Hashed Value from Query String  
$retrivedLockerID = $_GET['locker'];


//Hashing the various expected values
$hashVal101 = openssl_digest("101", "sha256");
$hashVal102 = openssl_digest("102", "sha256");
$hashVal103 = openssl_digest("103", "sha256");
$hashVal104 = openssl_digest("104", "sha256");
$hashVal105 = openssl_digest("105", "sha256");
$hashVal106 = openssl_digest("106", "sha256");
$hashVal107 = openssl_digest("107", "sha256");
$hashVal108 = openssl_digest("108", "sha256");
$hashVal109 = openssl_digest("109", "sha256");

$hashValUnavail = openssl_digest("unavailable", "sha256");


// USED FOR SMALL LOCKERS //
//GPIO 19 --> S-103
//GPI0 26 --> S-102

// USED FOR MEDIUM LOCKERS //
//GPIO 6  --> M-105
//GPIO 13 --> M-106

//Declaration of GPIO Pins setting Pin to Output Pin (LED)
shell_exec("gpio -g mode 6 out");
shell_exec("gpio -g mode 13 out");
shell_exec("gpio -g mode 19 out");
shell_exec("gpio -g mode 26 out");

    if ($retrivedLockerID == $hashValUnavail) {
        shell_exec("gpio -g write 6 0");
        shell_exec("gpio -g write 13 0");
        shell_exec("gpio -g write 19 0");
        shell_exec("gpio -g write 26 0");
    }

    else if ($retrivedLockerID == $hashVal102) {
        shell_exec("gpio -g write 26 1");
        shell_exec("gpio -g write 6 0");
        shell_exec("gpio -g write 13 0");
        shell_exec("gpio -g write 19 0");
    }

    else if ($retrivedLockerID == $hashVal103) {
        shell_exec("gpio -g write 19 1");
        shell_exec("gpio -g write 6 0");
        shell_exec("gpio -g write 13 0");
        shell_exec("gpio -g write 26 0");
    }

    else if ($retrivedLockerID == $hashVal105) {
        shell_exec("gpio -g write 6 1");
        shell_exec("gpio -g write 13 0");
        shell_exec("gpio -g write 19 0");
        shell_exec("gpio -g write 26 0");
    }

    else if ($retrivedLockerID == $hashVal106) {
        shell_exec("gpio -g write 13 1");
        shell_exec("gpio -g write 6 0");
        shell_exec("gpio -g write 19 0");
        shell_exec("gpio -g write 26 0");
    }
    
    else {
        shell_exec("gpio -g write 6 0");
        shell_exec("gpio -g write 13 0");
        shell_exec("gpio -g write 19 0");
        shell_exec("gpio -g write 26 0");
    } 
  
?>


