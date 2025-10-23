<?php
include "database.php";
$conn = new mysqli("localhost",$db_user, $db_password, $db_name);

if($conn->connect_error){
	die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT value, time FROM data WHERE time > DATE_SUB(CURRENT_DATE, INTERVAL 1 WEEK) ORDER BY time DESC";
$result = $conn->query($sql);

if($result->num_rows > 0){
	while($row = $result->fetch_assoc()){
		echo "V&auml;rde(mm): " . $row["value"] . " -- Tid(GMT): " . $row["time"] . "<br>";
	}
}

$conn->close();
echo "<br><br><br>Done";
echo "<br>Measurment done every 3 min since 2025-10-23 (on previous machine from 2016-03-01)";
?>
