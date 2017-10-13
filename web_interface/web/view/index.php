<?php
/**
 * Created by:
 * @author: Josh
 * @date: 9/29/2017
 * @desc
 * 
 */
require_once(dirname(__FILE__) . '/../load.php');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Crime Data Analytics">
    <meta name="author" content="Joshua Standiford">

    <title>Crime Data Analytics</title>

    <!-- Bootstrap Core CSS -->
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Distinct CSS -->
    <!--<link href="css/styles.css" type="text/css" rel="stylesheet">-->
    <link rel="stylesheet" href="css/style.css" type="text/css" media="screen">
    <link rel="stylesheet" href="css/map-styles.css" type="text/css" media="screen">

    <!-- Custom Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
    <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">

    <!-- AJAX Prototype Import -->
    <script src="https://ajax.googleapis.com/ajax/libs/prototype/1.7.3.0/prototype.js"></script>

</head>
<body>

<!-- Title of page -->
<div id="pageTitle">Crime Data</div>

<br />
<div id="info-box"></div>

<!-- Display Content -->
<div id="container">
   <!-- Content Goes Here -->
   <div id="floating-panel">
      <button onclick="toggleHeatmap()">Toggle Heatmap</button>
      <button onclick="changeGradient()">Change gradient</button>
      <button onclick="changeRadius()">Change radius</button>
      <button onclick="changeOpacity()">Change opacity</button>
    </div>
    <div id="map"></div>
</div>

<hr>
<footer>
    <!-- Footer Content Here -->
</footer>


<!-- Load scripts at the end -->
<script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDCCcUY9AP8u3ZWiOBWjbKCxA6qXX2wWSg&libraries=visualization&callback=initMap"></script>
<script src="js/Maps.js"></script>
<!-- End Loading Scripts-->
</body>
</html>