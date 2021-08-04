<?php

// Receiving POST DATA From Pin input page
$postedEnterCode =  ($_POST['enterCode']);

$servername = "localhost";
$username = "rebuxphpdbadmin";
$password = "rebuxphpdbadminpassword";
$dbname = "RebuxDB";


// Create Connection
$conn = new mysqli($servername, $username, $password, $dbname);


// Check Connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}


//Connection Success, Build Prepared Statements, and Execute Queries
$stmt = $conn->prepare("SELECT * FROM `Pin Session` WHERE status = 'Generated' AND pin_id = ? ");
$stmt->bind_param('i',$postedEnterCode); // 'i' specifies the variable type => 'integer'

//Executing Query, and Storing Results
$stmt->execute();
$stmt->store_result();


//Check if Pin Number is Valid and Exist in Database
if ($stmt->num_rows > 0) {
    
$stmt->bind_result($pinsesssion_id,$user_id,$pin_id,$generate_date_time,$use_date_time,$status);
$stmt->fetch();

//Check if Pin is Expired or Not, and if Pin  is considered Expired, ONLY PRINT EXPIRED MESSAGE if Pin is Expired RECENTLY.
date_default_timezone_set('Asia/Singapore');
$now = date("Y-m-d H:i:s");

$dateTimeGenerate = strtotime($generate_date_time);
$dateTimeGenerateFinalVal = date("Y-m-d H:i:s",$dateTimeGenerate);
$dateTimeExpireFinalVal = date("Y-m-d H:i:s",strtotime('+15 minutes', $dateTimeGenerate)); //EXPIRY TIME OF PIN = 15 mins
$dateTimeExpireWarningFinalVal = date("Y-m-d H:i:s",strtotime('+1440 minutes',$dateTimeGenerate)); //TIME WHEN EZPIRE MESSAGE WILL BE SHOWN = 1440 mins = 24 hrs (1 day,From Pin Being Generated) 
    
   //Success = PIN IS VALID + PIN NOT EXPIRED
    if($now <=  $dateTimeExpireFinalVal) {


        //Update Session Table with Status = In Progress
        $stmt = $conn->prepare("UPDATE Session SET status = 'In Progress' WHERE pinsession_id = (SELECT pinsession_id FROM `Pin Session` WHERE pin_id = ? AND status = 'Generated') ");
        $stmt->bind_param('i',$postedEnterCode);

        $stmt->execute();


        //Check Locker Avaliability
        if($pin_id >= "1000" && $pin_id <= "1999") {
            $lockerSize = "small"; 
        }

        elseif($pin_id >= "2000" && $pin_id <= "2999") {
            $lockerSize = "medium";
        }

        else{
            $lockerSize = "large";
        }
        $stmt = $conn->prepare("SELECT * FROM Locker WHERE status = 'vacant' AND size = ? LIMIT 1 ");
        $stmt->bind_param('s',$lockerSize); // 's' specifies the variable type => 'String'
        
        //Executing Query, and Storing Results
        $stmt->execute();
        $stmt->store_result();


        //Check if Locker as of Requested Size is Avaliable based on Database Records of Vacant Lockers
        if ($stmt->num_rows > 0) {
            $stmt->bind_result($locker_id,$item_id,$size,$status);
            $stmt->fetch();
            
            $postDataValue = openssl_digest($locker_id, "sha256");
            $redirectSuccessLinkWithLocker = "./pin_success.php?locker=";
            $redirectSuccessLinkWithLocker .= $postDataValue;
            echo $redirectSuccessLinkWithLocker; 
            
            //HASHED VALYE Cookie Declaration, however not used for locker unlock due to security concern, Security Unlock is still based on the hash value via query string
            setcookie("Locker_Id", $postDataValue, time()+60*10);
        }
        
        //All Locker, of Reuqested Size is CURRENTLY UNAVALIABLE
        else {

            //Update Session Table with Status = Lockers Unavailable (Previosuly Above Session was changed to = In Progress, hence a change needs to be done changing In Progress to Lockers Unavailable 
            $stmt = $conn->prepare("UPDATE Session SET status = 'Lockers Unavailable' WHERE pinsession_id = (SELECT pinsession_id FROM `Pin Session` WHERE pin_id = ? AND status = 'Generated') ");
            $stmt->bind_param('i',$postedEnterCode);

            $stmt->execute();


            $postDataValue = "unavailable";
            $postDataValue = openssl_digest($postDataValue, "sha256");
            $redirectUnavailableLinkWithLocker = "./pin_success.php?locker=";
            $redirectUnavailableLinkWithLocker .= $postDataValue;
            echo $redirectUnavailableLinkWithLocker;
        }
   
    //Update Pin Session Table with Used Date Time of Pin and Corresponding Status = Used
    $now_for_update = new DateTime();
    $string_now_for_update = $now_for_update->format('Y-m-d-H-i-s');
    $stmt = $conn->prepare("UPDATE `Pin Session` SET use_date_time = ? , status = 'Used' WHERE pin_id = ? AND status = 'Generated' ");
    $stmt->bind_param('si',$string_now_for_update,$postedEnterCode);

    $stmt->execute();


    }
 
    /*
    Expire and Invalid Pin Message, SEPERATED INTO TWO DUE TO SECURITY CONCERNS OF BRUTE FORCE ATTACK ETC. AS PIN SESSION TABLE GETS FILLED UP
    PIN IS LIKELY TO BE REPEATED IN PIN SESSION. HENCE SHOULD ONLY PRINT EXPIRE MESSAGE FOR USERS WHOM PIN RECENTLY HAS EXPIRE (RECENTLY = 1.5 HRS AFTER PIN GENERATION),
    AND ONCE USER IS NOTIFIED ONCE PIN WILL BE SET TO EXPIRE HENCE INVALID MESSAGE WILL NOW SHOW INSTEAD OF EXPIRE MESSAGE (PROTECTING FURTHER BRTUE FORCE ATTEMPTS FROM USERS
    */
    //EXPIRE MESSAGE = PIN IS VALID, PIN IS EXPIRED **RECENTLY**
    elseif($now <= $dateTimeExpireWarningFinalVal) {
        echo"./pin_input.php?status=e2";
    } 

    //INVALID MESSAGE = PIN IS EITHER INVALID OR, PIN IS EXPIRED **FOR A LONG TIME > 1440 mins (24hrs = 1 day) BEFORE TIME GENERATED**
    else {
        echo "./pin_input.php?status=e1";
    }

    //CATCH ALL UPDATE FOR EXPIRY OF PIN (DON'T CARE WETHER EXPIRE LONG TIME AGO OR RECENTLY, AS LONG AS EXPIRE, UPDATE DB WITH EXPIRE STATUS
    //Updating database records of Pin Session table for Pin inputted which are expired
    if ($now <=  $dateTimeExpireFinalVal == False) {

        $now_for_update = new DateTime();
        $string_now_for_update = $now_for_update->format('Y-m-d-H-i-s');

        $stmt = $conn->prepare("UPDATE `Pin Session` SET use_date_time = ?, status = 'Expired'  WHERE pin_id = ? AND status = 'Generated'");
        $stmt->bind_param('si',$string_now_for_update, $postedEnterCode);
        $stmt->execute();

    } 

}

//INVALID MESSAGE = PIN INPUTTED IS COMPLETELY INVALID AND DOESN'T EXIST IN DATABASE
else {

echo "./pin_input.php?status=e1";

}

//Closing Connection Clean Up
$conn->close();


exit;
 
?>
