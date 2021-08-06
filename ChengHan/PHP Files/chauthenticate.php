<?php
session_start();
// Change this to your connection info.
$DATABASE_HOST = 'localhost';
$DATABASE_USER = 'rebuxphpdbadmin';
$DATABASE_PASS = 'rebuxphpdbadminpassword';
$DATABASE_NAME = 'RebuxDB';
// Try and connect using the info above.
$con = mysqli_connect($DATABASE_HOST, $DATABASE_USER, $DATABASE_PASS, $DATABASE_NAME);
if ( mysqli_connect_errno() ) {
	// If there is an error with the connection, stop the script and display the error.
	exit('Failed to connect to MySQL: ' . mysqli_connect_error());
}


if ( !isset($_POST['username'], $_POST['password']) ) {
	// Could not get the data that should have been sent.
	exit('Please fill both the username and password fields !');
}

 
if ($stmt = $con->prepare('SELECT user_id, password, name FROM Users WHERE user_id = ?')) {
	// Bind parameters (s = string, i = int, b = blob, etc), in our case the username is a string so we use "s"
	$stmt->bind_param('i', $_POST['username']);
	$stmt->execute();
	// Store the result so we can check if the account exists in the database.
	$stmt->store_result();
	





if ($stmt->num_rows > 0) {
	$stmt->bind_result($user_id, $password, $name);
	$stmt->fetch();
	// Account exists, now we verify the password.
	// Note: remember to use password_hash in your registration file to store the hashed passwords.
	
	// convert user input password into hash digit
	$userinput = hash("sha256", $_POST['password']);
	
	 if ($userinput === $password) {
		// Verification success! User has logged-in!
		// Create sessions, so we know the user is logged in, they basically act like cookies but remember the data on the server.
		session_regenerate_id();
		//$_SESSION['loggedin'] = TRUE;
                //$_SESSION['user_name'] = $_POST['username'];
		//$_SESSION['user_id'] = $user_id;
		
                setcookie("Logged_In", "True", time()+60*10);
                setcookie("User_Name", $name, time()+60*10);
                setcookie("User_Id", $user_id, time()+60*10); 

		header('Location: index.php');
		
} else {
		// Incorrect password
		header('Location: chindex.php?error=Incorrect password');
	}
} else {
	// Incorrect username
	header('Location: chindex.php?error=Incorrect username ');
}

	$stmt->close();


}
?>
