<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" href="services.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/1.6.2/tailwind.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@700&display=swap" rel="stylesheet">
	
	

    <script>

     function getCookie(cname) {
	 let name = cname + "=";
	 let decodedCookie = decodeURIComponent(document.cookie);
	 let ca = decodedCookie.split(';');
	 for(let i = 0; i <ca.length; i++) {
	     let c = ca[i];
	     while (c.charAt(0) == ' ') {
	       c = c.substring(1);
	     }
	     if (c.indexOf(name) == 0) {
	      return c.substring(name.length, c.length);
	     }
      }
      return "";
    }

     $(document).ready(function() {
		    $('body.hero-anime').removeClass('hero-anime');


      var r_c_logged_in = getCookie("Logged_In");
		     var r_c_user_name_unformat = getCookie("User_Name");
		     var r_c_user_id = getCookie("User_Id");

		     var r_c_user_name = r_c_user_name_unformat.split("+").join(" ");

		     if (r_c_logged_in == "True") {
			 document.getElementById("services_dropdown").removeAttribute("hidden");
			 document.getElementById("button").innerHTML = r_c_user_name;
			 document.getElementById("button").removeAttribute('onclick');
		     }



    });
		
		
		
    (function($) { "use strict";

	$(function() {
		var header = $(".start-style");
		$(window).scroll(function() {    
			var scroll = $(window).scrollTop();
		
			if (scroll >= 10) {
				header.removeClass('start-style').addClass("scroll-on");
			} else {
				header.removeClass("scroll-on").addClass('start-style');
			}
		});
	});


		
	$('body').on('mouseenter mouseleave','.nav-item',function(e){
			if ($(window).width() > 750) {
				var _d=$(e.target).closest('.nav-item');_d.addClass('show');
				setTimeout(function(){
				_d[_d.is(':hover')?'addClass':'removeClass']('show');
				},1);
			}
	});	


	
	$("#switch").on('click', function () {
		if ($("body").hasClass("dark")) {
			$("body").removeClass("dark");
			$("#switch").removeClass("switched");
		}
		else {
			$("body").addClass("dark");
			$("#switch").addClass("switched");
		}
	});  
	
      })(jQuery); 


    </script>

	
    <title>Services</title>
</head>

<body class="hero-anime">
        <div class="navigation-wrap bg-light start-header start-style">
            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <nav class="navbar navbar-expand-md navbar-light">

                            <a class="navbar-brand" href="index.php" target="_blank">Rebux</a>

                            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                                <span class="navbar-toggler-icon"></span>
                            </button>

                            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                                <ul class="navbar-nav ml-auto py-4 py-md-0">
                                    <li class="nav-item pl-4 pl-md-0 ml-0 ml-md-4 active">
                                        <a class="nav-link" href="index.php" role="button">Home</a>
                                       
                                    </li>
                                    <li class="nav-item pl-4 pl-md-0 ml-0 ml-md-4">
                                        <a class="nav-link" href="about_us.php">About Us</a>
                                    </li>
                                    <li class="nav-item pl-4 pl-md-0 ml-0 ml-md-4">
                                        <a class="nav-link" href="contact_us.php">Contact</a>
                                    </li>
                                    <li class="nav-item pl-4 pl-md-0 ml-0 ml-md-4" id="services_dropdown" hidden>
                                        <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">Services</a>
                                        <div class="dropdown-menu">
                                            <a class="dropdown-item" href="services.php">Locker and Chute</a>                                
                                            <a class="dropdown-item" href="view_chute.php">View Chute Content Level</a>        
                                        </div>
                                    </li>
                                    <li class="nav-item pl-4 pl-md-0 ml-0 ml-md-4" id="button">
                                        <a class="square_btn" href="chindex.php">Login</a>
                                    </li>
                                </ul>
                            </div>

                        </nav>
                    </div>
                </div>
            </div>
        </div>
  
    <div class="space"></div>

    <!--Start of Services Content-->
       <div class="inline half-page-1">
       <div style="height:35vh"></div>
       <center class="type-title" style="color:#454545"><a href="pin_input.php">LOCKER</a></center>
        
       
       
     <center id="lockersection" class="child bounce"><a href="pin_input.php"> <img src="data:image/png;base64,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" width="300" height="300"/> </a></center>
     </div>


  
     <div class="inline half-page-2">
       <div style="height:35vh"></div>
       <center class="type-title" style="color:#454545"><a href="chute.php">CHUTE</a></center>
       
       <center id="chutesection" class="child bounce"><a href="chute.php"><img src="https://icons-for-free.com/iconfiles/png/512/arrow+box+down+essential+ui+icon-1320166478540091866.png" width="280" height="300"/></a></center>
     </div>
    
    <!--End of Services Content-->
 
    </body>

</html>
