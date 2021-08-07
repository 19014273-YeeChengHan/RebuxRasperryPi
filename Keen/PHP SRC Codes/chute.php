<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" href="chute.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/1.6.2/tailwind.min.css">
    <script `src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>

	
    <script>
	
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
	
	
		
	</script>
	
	<title>Chute</title>
</head>

<body class="hero-anime">

<!--Start of NavBar-->
        <div class="navigation-wrap bg-light start-header start-style">
            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <nav class="navbar navbar-expand-md navbar-light">

                            <a class="navbar-brand" href="#" target="_blank">Rebux</a>

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
                                    <li class="nav-item pl-4 pl-md-0 ml-0 ml-md-4">
                                        <a class="square_btn" href="chindex.php">Login</a>
                                    </li>
                                </ul>
                            </div>

                        </nav>
                    </div>
                </div>
            </div>
        </div>
  
<!--End of NavBar-->  

<!--Start of Chute Portion-->
<div class="sm:flex items-center max-w-screen-xl">
    <div class="sm:w-1/2 p-10">
      
            <div class="header"></div>

            <div class="image object-center text-center">

      <img src="https://opendoodles.s3-us-west-1.amazonaws.com/sitting.svg" alt="Snow" width=100% height=100%>
            </div>
    </div>
    <div class="sm:w-1/2 p-5">
        <div class="text">

            <h2 class="my-4 font-bold text-3xl  sm:text-4xl " align="middle">Rebux<span style="color:#73D0C2"> Chute</span></h2>

     <div>&nbsp</div>
     <div class="text-md">
        <h1 class="text-gray-900 font-semibold mb-2 left-column">The purpose of the Chute</h1>
        <p class="text-gray-500 text-sm">The chute is used for depositing lost items that do not fit in the regular sizes of the Locker Terminal. 
	Items that are bukly in size such as, a bag, should be deposited in the Chute. </p>
      </div>
          
     <div>
	     
        &nbsp;
      </div>
	<div class="text-md">
		
		<h1 class="text-gray-900 font-semibold mb-2">How to use?</h1>
		<p class="text-gray-500 text-sm">
		 If you have found a lost item that are bulky in size, simply deposit the item through the chute. 
		 Once you hear a buzzer sound, it means that the item has been deposited properly. 
		 These lost items will be collected by the employees at One Stop Centre and will store the items.
		</p>
	</div>
	</div>
    
    </div>
</div>
<!--End of Chute Portion-->
    </body>

</html>

