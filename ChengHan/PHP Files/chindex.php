<!DOCTYPE html>
<?php 

setcookie("Logged_In", "", time()-60);
setcookie("User_Name", "", time()-60);
setcookie("User_Id", "", time()-60);
setcookie("Locker_Id","",time()-60);
x?>
<html>
 
<body>
 
    <?php
    header ('Location: index.php');
    ?>
 
</body>
 
</html>
