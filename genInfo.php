<!DOCTYPE html>
<html lang="en">
    
    <link href="includes/css/style.css" rel="stylesheet">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
        <script language="javascript" type="text/javascript" src="includes/js/time.js">time</script>
        <script language="javascript" type="text/javascript" src="includes/js/genInfo.js">time</script>
        
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />


    <title>Team Orange Bull Racing</title>
  </head>
  <body>

  <?php
  $filename = "data/batteryData.json";
  $jso = file_get_contents($filename);
  $jarray = json_decode($jso, true);

  $array_bat = $jarray["result"]["data"];
  $array_keys = $jarray["result"]["columns"];
  $key_charge = array_search("stofch", $array_keys);
  $key_voltage = array_search("v_value", $array_keys);
  $key_current = array_search("bat_c", $array_keys);

  $range = end($array_bat)[$key_charge];
  $inspection = "11.11.2018";
  $user = "Alex";
  $friends = 12;
  $model = "Model123";

  $hp = 30;
  $bat_capacity = 2.6;
  $manufacturing_year = 2017;

  ?>


    <head>
        <img  id="logo" class="col-12 " src="includes/img/2000px-Continental_AG_logo.svg.png" alt="CESpa_E-Scooter">
      </head>
    
    

    <ul id="nav_ul">
        <li><a  href="index.html">Home</a></li>
        <li><a href="genInfo.php">General Information </a></li>
        <li><a href="ECCCha.html">Eco Monitor</a></li>
        <li><a href="safety.html">Safety and Security</a></li>
        <li><a href="navigation.html">Navigation</a></li>

        <li class="loginPos"><a id="uhr"></a></li>
        <li class="loginPos"><a  href="login.html">Login</a></li>	
        
    </ul>
    
        <table class="distance table">
            <tbody>
            <tr>
              <td><b>General Information</b></td> <td></td>
            </tr>
            <tr>
              <td>Range</td>
              <td>
              <?php echo $range ?> km
              </td>
            </tr>
            <tr>
              <td>Battery charge</td><td>
              <?php echo end($array_bat)[$key_charge] ?> %
              </td>
            </tr>
            <tr>
              <td>Last inspection</td>
              <td>
              <?php echo $inspection ?>
              </td>
            </tr>
          <!-- </table>
          <table width="400"> -->
            <tr>
                <td><b>User Dates</b></td> <td></td>
            </tr>
            <tr>
              <td>User Name</td>
              <td>
              <?php echo $user ?>
              </td>
            </tr>
            <tr>
              <td>Friends</td>
              <td>
              <?php echo $friends ?>
              </td>
            </tr>
          <!-- </table>
          <table width="400"> -->
            <tr>
              <td><b>Scooter Information</b></td> <td></td>
            </tr>
            <tr>
              <td>Model</td>              
               <td>
              <?php echo $model ?>
              </td>
            </tr>
            <tr>
              <td>Horse Powers</td>
              <td>
              <?php echo $hp ?> hp
              </td>
            </tr>
            <tr>
              <td>Battery capacity</td>
              <td>
              <?php echo $bat_capacity ?> kWh
              </td>
            </tr>
            <tr>
              <td>Battery voltage</td>
              <td>
              <?php echo end($array_bat)[$key_voltage] ?> V
              </td>
              </tr>
              <tr>
              <td>Battery current</td>
              <td>
              <?php echo end($array_bat)[$key_current] ?> A
              </td>
              </tr>
              <tr>
                <td>Manufacturing year</td>
                <td>
              <?php echo $manufacturing_year ?>
              </td>
              </tr>
              </tbody>
          </table>

        <!-- <form>
            <div class="col-2" id="distance_Login">
                <table class="table price-table" >
                  <tr>
                    <td>Username:</td>
                    <td><input type="text"/> </td>
                  </tr>
                  <tr>
                      <td>Password:</td>
                      <td><input type="password"/> </td>
                  </tr>
                  <tr>
                    <td><input id="Login_btn" class ="btn"type="submit"value="Login"/></td>
                    <td><input id="Login_btn" class ="btn" type="reset" value="Reset"></td>
                  </tr>
                </table>
            </div>  
          </form> -->

        
        
	
  </body>
  <footer id="footer_padding-top">
      <div class="row">
            
          <div class="column">
              <a href="#">Imprint</a></br>
              <a href="#">Data protection</a></br>
              <a href="#">Contact</a></br>
          </div>
        </div>
  
  
  
  
  </footer>
</html>