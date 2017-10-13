<?php
/**
 * Created by:
 * User: Josh
 * @desc
 */
require_once(dirname(__FILE__) . '/../load.php');

//define passed and failed HTML objects
$passed = "<span class='glyphicon glyphicon-ok passed'></span>";
$failed = "<span class='glyphicon glyphicon-remove failed'></span>";
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Crime Data">
    <meta name="author" content="Joshua Standiford">

    <title>Testing Framework</title>

    <!-- Bootstrap Core CSS -->
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <!-- Distinct CSS -->
    <link rel="stylesheet" href="css/unit-test.css" type="text/css" media="screen">
</head>
<body>
<div id="pageTitle">Crime Data -- App Testing</div>
<div id="container">
    <!-- Test section -->
    <div class="test-section">
        <div class="title-section">Tests for --INSERT CLASS--</div>
        <div class="body-section">
            <table>
                <tr>
                    <th>Unit Test Description</th>
                    <th>Passed</th>
                </tr>
                <tr>
                    <td>BusinessCardParser constructor creates valid object</td>
                    <td>
                        <?php
                        /** Test Goes Here **/
                        if(true){ echo $passed;}
                        else {echo $failed;}
                        ?>
                    </td>
                </tr>
            </table>
        </div>
    </div>

    <br />
    Return home <a href="index.php"><span class="glyphicon glyphicon-home"></span></a>
</div>

<hr>
<footer style="text-align:center;font-size:.8em;">
    <p>Created By: Joshua Standiford</p>
</footer>

</body>
</html>
