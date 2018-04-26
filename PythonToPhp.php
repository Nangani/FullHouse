<?php
    $_FILES['img']['name']="plan.png";
    $uploadAddr = '/var/www/html/'
    $uploadFile = $uploadFile = $uploadAddr.basename($_FILES['img']['name']);
    move_uploaded_file($_FILES['userfile']['tmp_name'], $uploadfile))
    exec('FindWall.py');
    $python = exec ('PrintWall.py');
?>