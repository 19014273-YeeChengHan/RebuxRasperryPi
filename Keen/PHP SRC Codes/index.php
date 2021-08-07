<!DOCTYPE html>
<html lang="en">
<head>
    <title>Rebux Homepage</title>
    <link rel="stylesheet" href="index.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>



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
		
	
	$(document).ready(function() {

                 var r_c_logged_in = getCookie("Logged_In");
                 var r_c_user_name_unformat = getCookie("User_Name");
                 var r_c_user_id = getCookie("User_Id");

                 var r_c_user_name = r_c_user_name_unformat.split("+").join(" ");
  
                 if (r_c_logged_in == "True") {
                     document.getElementById("services_dropdown").removeAttribute("hidden");
                     document.getElementById("button").innerHTML = r_c_user_name;
                     document.getElementById("button").removeAttribute('onclick');
                 }

		 $('body.hero-anime').removeClass('hero-anime');
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
	
	<title>Rebux Homepage</title>

</head>


<body class="hero-anime">
    
	
        <div class="ocean">
            <div class="wave"></div>
            <div class="wave"></div>
        </div>

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
					<a class="nav-link dropdown-toggle" data-toggle="dropdown" href="services.php" role="button" aria-haspopup="true" aria-expanded="false" id="services">Services</a>
					<div class="dropdown-menu">
                                            <a class="dropdown-item" href="services.php">Locker and Chute</a>
					    <a class="dropdown-item" href="view_chute.php">Chute Content Level</a>        
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
        <div class="section full-height">
            <div class="absolute-center">
                <div class="section">
                    <div class="container">
                        <div class="row">
                            <div class="col-12">
                                <h1>
                                    <span>W</span><span>e</span><span>l</span><span>c</span><span>o</span><span>m</span><span>e</span><br><span>to</span>
                                    <br><span>R</span><span>e</span><span>b</span><span>u</span><span>x</span>
                                </h1>
                                <p>Republic Polytechnic's Lost and Found</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="section mt-5">
                    <div class="container">
                        <div class="row">
                            <div class="col-12">

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="my-5 py-5">
        </div>

    </body>



  
</html>

 

