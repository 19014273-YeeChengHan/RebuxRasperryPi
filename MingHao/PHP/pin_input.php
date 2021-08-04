<!DOCTYPE html>
<head>

<title>Rebux Deposit</title>

<link rel="stylesheet" href="pin_input.css" />

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>

<script type= "text/javascript">

jQuery(document).ready(function($) {
  $(document).ready(function() {
    
    //Retrive Query String Values in URL, if any is found.
    const params = new URLSearchParams(window.location.search)
 
    var enterCode = '';
    
    var statusRetrived = params.get('status')
    if (statusRetrived == 'e1') { 
    document.getElementById("alertmessage").innerHTML = "ERROR! INVALID PIN, PLEASE TRY AGAIN";
    document.getElementById("alertxbutton").removeAttribute("hidden");
    document.getElementById("alert").removeAttribute("hidden");
    }

    if (statusRetrived == 'e2') {
    document.getElementById("alertmessage").innerHTML = "ERROR! PIN HAS EXPIRED, PLEASE RE-GENERATE A NEW PIN, ON OUR WEBSITE AND TRY AGAIN";
    document.getElementById("alertxbutton").removeAttribute("hidden");
    document.getElementById("alert").removeAttribute("hidden");
    }

    $("#numbers button").click(function() {

      var clickedNumber = $(this).text().toString();
      enterCode = enterCode + clickedNumber;
      var lengthCode = parseInt(enterCode.length);
      lengthCode--;
      $("#fields .numberfield:eq(" + lengthCode + ")").addClass("active");

      if (lengthCode == 3) {
      
      $.ajax({
      type: "POST",
      url: 'pin_authenticate.php',
      data: {enterCode: enterCode},
      success: function(data){ 
      window.location.href = data
      },
      error: function(xhr, status, error){
      console.error(xhr);
      }
      });
      }

    });
    
    $("#restartbtn").click(function(){
      enterCode = "";
      $("#fields .numberfield").removeClass("active");
      $("#fields .numberfield").removeClass("right");
      $("#numbers").removeClass("hide");
      $("#anleitung p").html("<strong>Please enter the correct PIN-Code.</strong><br> It is: 1234 / Also try a wrong code");
    });

  });
});

</script>

</head>

<body>
  <div id="pincode">
    <div class="table">
      <div class="cell">

        <div id="userprompt">
          <h2>
            <strong>Please Enter Pin Code</strong>
          <h2>
        </div>
        
        <div class="alert" id="alert" hidden>
          <span id="alertxbutton"class="closebtn" onclick="this.parentElement.style.display='none';" hidden>&times;</span> 
          <strong id="alertmessage"></strong>
        </div>

        <div id="fields">
          <div class="grid">
            <div class="grid__col grid__col--1-of-4 numberfield"><span></span></div>
            <div class="grid__col grid__col--1-of-4 numberfield"><span></span></div>
            <div class="grid__col grid__col--1-of-4 numberfield"><span></span></div>
            <div class="grid__col grid__col--1-of-4 numberfield"><span></span></div>
	   
          </div>
        </div>

        <div id="numbers">
          <div class="grid">
            <div class="grid__col grid__col--1-of-3"><button>1</button></div>
            <div class="grid__col grid__col--1-of-3"><button>2</button></div>
            <div class="grid__col grid__col--1-of-3"><button>3</button></div>

            <div class="grid__col grid__col--1-of-3"><button>4</button></div>
            <div class="grid__col grid__col--1-of-3"><button>5</button></div>
            <div class="grid__col grid__col--1-of-3"><button>6</button></div>

            <div class="grid__col grid__col--1-of-3"><button>7</button></div>
            <div class="grid__col grid__col--1-of-3"><button>8</button></div>
            <div class="grid__col grid__col--1-of-3"><button>9</button></div>

            <div class="grid__col grid__col--1-of-3"></div>
            <div class="grid__col grid__col--1-of-3"><button>0</button></div>
            <div class="grid__col grid__col--1-of-3"></div>

          </div>
        </div>

      </div>
    </div>
  </div>

</body>
