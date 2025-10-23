<html>
	<head>
		<style>
		#chart_div {
		width: 1800px;
		height: 900px;
		}
		</style>		
		<script type="text/javascript" src="https://gstatic.com/charts/loader.js"></script>
		<script type="text/javascript">
			google.charts.load('current',{'packages':['corechart']});
			google.charts.setOnLoadCallback(drawChart);
			
			function drawChart(){
				var data = google.visualization.arrayToDataTable([
				['Tid', 'Höjd']<?php

include "database.php";
$conn = new mysqli("localhost",$db_user, $db_password, $db_name);

if($conn->connect_error){
	die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT value, time FROM data WHERE time > DATE_SUB(CURRENT_DATE, INTERVAL 1 MONTH)";

$result = $conn->query($sql);
$counter = 0;
$test = FALSE;
if($result->num_rows > 0){
	while($row = $result->fetch_assoc()){
		$value = intval($row["value"]);		
		if($value > 200){
			$test = TRUE;
		} elseif($value < 100 && $test){
			$counter = $counter + 1;
			$test = FALSE;
		}
		echo ",\n\t\t\t\t[new Date('" . $row["time"] . "')," . $value . "]";
	}
}

$conn->close();

?>

				]);

				var options = {
					title: 'Vattennivå',
					hAxis: {title: "Datum"},
					vAxis: {maxValue: 330}
				};
				
				var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
				chart.draw(data,options);
				}
		</script>
	</head>
	<body>
		<div id="chart_div"></div>
		<font size="12"><center>Antal t&ouml;mningar: 
<?php
echo $counter; 
?>
</center>
		
	</body></font>
</html>
			
