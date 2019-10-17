<?php
//
$form_data = array($_POST["req_date"],
	$_POST["req_time"],
	$_POST["req_client"],
	$_POST["req_department"],
	$_POST["req_address"],
	$_POST["req_phone"],
	$_POST["req_contact"],
	$_POST["req_systems"],
	$_POST["type"],
	$_POST["req_desc"]);
$service_person = $_POST["engineer"];
$bad_char = array ('\"','$');
$comm_txt = "";
for ($x =0; $x <count($form_data); $x++){
	$form_data[$x] = str_replace('"','',$form_data[$x]);
	$comm_txt = $comm_txt." \"".$form_data[$x]."\"";
}
$comm_txt."<br/>";
$command = escapeshellcmd("python serv_req.py{$comm_txt}");



$output = shell_exec($command." 2> error.log");
$output = trim($output);
echo ($output."<br/>");
?>

<?php
$name  ="CCEService";
$email  ="service@cce-service.ca";
$fetch_message  ="Service Request Incoming!<br/><br/>";
$fetch_message .= "<b>Date: </b>".$_POST["req_date"]." @ ".$_POST["req_time"]."<br/>";
$fetch_message .= "<b>Client: </b>".$_POST["req_client"]."<br/>";
$fetch_message .= "<b>Address: </b>".$_POST["req_address"]."<br/>";
$fetch_message .= "<b>Systems: </b>".$_POST["req_systems"]."<br/>";
$fetch_message .= "<b>Description: </b>".$_POST["req_desc"]."<br/>";



$fetch_subject ="Service Request";


$file_ext=explode(".",$output);
$file_type=strtolower($file_ext[1]);

$name_of_attachment = basename($output);
$tmp_path = $output;

if($file_type == "pdf" )
{
 $mime_type = "application/pdf";
}
else if($file_type == "doc" )
{
 $mime_type = "application/msword";
}
else if($file_type == "docx" )
{
 $mime_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document";
}
else {echo "None of the above my friend</br>";}

if ($file_type == 'pdf' || $file_type == 'doc' || $file_type == 'docx' )
  {
   $to = "sbrukson@gmail.com, alex@ccemedical.com";
   $subject =  $fetch_subject;
   $bound_text = "_____________________";
   $bound = "--".$bound_text."\r\n";
   $bound_last = "--".$bound_text."--\r\n";

  $headers .= "Reply-To: Service <service@cce-service.ca>\r\n";
  $headers .= "Return-Path: Service <service@cce-service.ca>\r\n";

   $headers = "From: \"".$name."\" <{$email}>\r\n";
   $headers .= "MIME-Version: 1.0\r\n"
   ."Content-Type: multipart/mixed; boundary=\"$bound_text\"";

   $message .= "".$bound;

   $message .= "Content-Type: text/html; charset=\"iso-8859-1\"\r\n"
   ."Content-Transfer-Encoding: 7bit\r\n\r\n"
   ."<b>Message: </b> ".$fetch_message." \r\n"
   .$bound;

   $file = file_get_contents($tmp_path);
   $file_encode = chunk_split(base64_encode($file));

   $message .= "Content-Type: ".$mime_type."; name=\"".$name_of_attachment."\"\r\n"
   ."Content-Transfer-Encoding: base64\r\n"
   ."Content-disposition: attachment; file=".$name_of_attachment."\r\n"
   ."\r\n"
   .$file_encode
   .$bound_last;

   if(mail($to, $subject, $message, $headers))
   {
    echo '<script language="javascript">alert("Message sent.");</script>';
    echo "<script>  location.replace(\"https://cce-service.ca\")</script>";
}
   else
   {
	echo '<script language="javascript">alert("Error in sending message. Please try again later.");</script>';
   }

  }
  else
  {
   echo 'Invalid uploaded file type!';
  }

?>
