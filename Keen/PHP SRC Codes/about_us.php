<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" href="RebuxStyleSheet.css">
    <link rel="stylesheet" href="about_us.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.3/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/1.6.2/tailwind.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
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
    <title>About Us</title>
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

                            <div class="collapse navbar-collapse" id="navbarlSupportedContent">
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
	<!--Start of About Us Portion-->
              
       <div class="sm:flex items-center max-w-screen-xl">
	<div class="sm:w-1/2 p-10">
            <div class="image object-center text-center">
              
		<!--SVG Image of Woman Wearing Pink-->
		<img src="https://opendoodles.s3-us-west-1.amazonaws.com/unboxing.svg" alt="About Us Images" width=100% height=100%/>
		<!--SVG Image of Woman Wearing Pink-->

            </div>
	</div>
	<div class="sm:w-1/2 p-5">
	    <div class="text">
		
		<h2 class="my-4 font-bold text-3xl  sm:text-4xl ">About <span style="color: #4DC0B2">Rebux</span></h2>
		<p class="text-gray-900" style="text-align: left; display:flex; flex-direction: column; align-items: left">
		Rebux is developed by Republic Polytechnic's students and it's a  Lost and Found System that allows students and staff to 
		deposit lost items found within the school premises and to make the process of deposting lost items seamless through the usage of a Locker and Chute. 
		Scroll down to find out more about our services.</p>

        </div>
    </div>
</div>



  <!-- End of About Us Portion-->            
						</div>	
					</div>		
				</div>		
			</div>
		</div>
   </div
  
<!-- Start of Our Services Portion-->       
<div class="container my-0">
  <div class="text-center mb-5">
    
    <h1 class="text-capitalize font-weight-bold">Our <span style="color: #4DC0B2">Services</span></h1>
  </div>

  <div class="row">
    
    <div class="col-md-6 p-6">
      <div class="d-flex align-items-start">
        <div class="mr-4">
          <div class="p-4 rounded-circle text-white font-weight-bold d-flex align-items-center justify-content-center" style="height: 60px; width: 60px; background-color: #4DC0B2">
            1
          </div>
        </div>
        <div class="">
          <h5 class="mb-2" style="font-weight: 600;">Pin</h5>
          <p class="text-secondary" style="text-align: left; display:flex; flex-direction: column; align-items: left">The purpose of the 4 digit generated pin is to allow you to deposit the lost item to a specific locker terminal.
	  Navigate to Locker under Services to enter your pin which and you will be directed to a locker to deposit the lost item.</p>
        </div>
      </div>
    </div>

    <div class="col-md-6 p-6">
      <div class="d-flex align-items-start">
        <div class="mr-4">
          <div class="p-4 rounded-circle text-white font-weight-bold d-flex align-items-center justify-content-center" style="height: 60px; width: 60px; background-color: #4DC0B2">
            2
          </div>
        </div>
        <div class="">
          <h5 class="mb-2" style="font-weight: 600;">Locker Terminal Deposit</h5>
          <p class="text-secondary" style="text-align: left; display:flex; flex-direction: column; align-items: left">Locker terminals have 3 sizes which includes small, medium and large. The locker you deposit the lost item in depends on it's size.</p>
        </div>
      </div>
    </div>

    <div class="col-md-6 p-6">
      <div class="d-flex align-items-start">
        <div class="mr-4">
          <div class="p-4 rounded-circle text-white font-weight-bold d-flex align-items-center justify-content-center" style="height: 60px; width: 60px; background-color: #4DC0B2">
            3
          </div>
        </div>
        <div class="">
          <h5 class="mb-2" style="font-weight: 600;">Chute Deposit</h5>
          <p class="text-secondary" style="text-align: left; display:flex; flex-direction: column; align-items: left">Lost items that exceed the regular sizes of locker terminals are deposited in the Chute.</p>
        </div>
      </div>
    </div>

 
     <div class="col-md-6 p-6">
      <div class="d-flex align-items-start">
        <div class="mr-4">
          <div class="p-4 rounded-circle text-white font-weight-bold d-flex align-items-center justify-content-center" style="height: 60px; width: 60px; background-color: #4DC0B2">
            4
          </div>
        </div>
        <div class="">
          <h5 class="mb-2" style="font-weight: 600;">View Chute Content Level</h5>
          <p class="text-secondary" style="text-align: left; display:flex; flex-direction: column; align-items: left">As an administrator of Rebux, you can view the Chute's Content Level which shows the total weight of items deposited in the Chute and 
	  acts an indicator that the Chute is full and should be emptied.
	  </p>
        </div>
      </div>
    </div>   

  </div>
</div>
  
<!-- End of Our Services Portion-->   
    </body>

</html>
