<?php
$servername = "localhost";
$username = "rebuxphpdbadmin";
$password = "rebuxphpdbadminpassword";
$dbname = "RebuxDB";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT description, weight FROM Item
INNER JOIN Locker WHERE Item.item_id = Locker.item_id AND status = 'occupied' ";
$result = $conn->query($sql);

#Another way to append to data into the array in the while loop below 
#$dataPoints[] = array("y" => $row["weight"], "label" => $row["description"]);

$dataPoints = array();
if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
     array_push($dataPoints, array("y" => $row["weight"], "label" => $row["description"])); 
 
  } 
}else {
  echo "0 results";
}


$conn->close(); 
?>

<!DOCTYPE HTML>
<html>
    <head>
    <script>
        window.onload = function() {
         
        var chart = new CanvasJS.Chart("chartContainer", {
            animationEnabled: true,
            theme: "light2",
            title:{
                text: "View Locker Cotent Level"
            },
            axisY: {
                title: "Weight of Item (in grams)"
            },
            data: [{
                type: "column",
                yValueFormatString: "#,##0.##g",
                dataPoints: <?php echo json_encode($dataPoints, JSON_NUMERIC_CHECK); ?> 
                }]
        });
        chart.render();
         
        }
        </script>   
    </head>
    <body>
    <div id="chartContainer" style="height: 500px; width: 100%;"></div>
    <script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
    </body>
    
</html>


