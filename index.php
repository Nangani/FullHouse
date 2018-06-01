<!DOCTYPE html>
<html>

	<head>
	    <meta charset="utf-8">
	    <link rel="stylesheet" type="text/css" href="main.css">
	</head>

	<body>
		<img class="main_image" src="image/main.png">

	    <form enctype="multipart/form-data" action="ShowWall.php" id ="plan" name="plana" method="POST">
	    	<button class="replace">Load Image</button>
	    	<input type="file" name="img" class="upload" onchange=aa(); />
	    </form>
	    
	    <button class="button_make" onclick="makepage()">Make Plan</button>
<script>
	function aa() {
		if(document.plana.img.value != "") {
			document.plana.action = "workpage2.php";
			document.plana.submit();
		}
	}
	function makepage() {
		location.replace("makepage.html");
	}
</script>
</html>

