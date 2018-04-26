<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>


    <script src="three.js"></script>
    <script src="PointerLockControls.js"></script>
    <script src="jquery-3.3.1.min.js"></script>
    <script src="OrbitControls.js"></script>
    <!--script scr="js/main.js"></script-->

    <!--<script type="text/javascript" src="main.js"></script-->

</head>

<body>
    <div id='container'></div>
    <?php
        $_FILES['img']['name']="plan.png";
        $uploadAddr = '/var/www/html/';
        $uploadFile = $uploadAddr.basename($_FILES['img']['name']);
        move_uploaded_file($_FILES['img']['tmp_name'], 'plan.png');
        exec('C:\Python36-32\python.exe C:/xampp/htdocs/FindWall.py');
        $python = exec ('C:\Python36-32\python.exe PrintWall.py');
       
      
    ?>
        <input type="hidden" id="walls" value=<?php echo "\"".$python."\"";?> >
        <script type="text/javascript">
            var $ = function(id) {return document.getElementById(id)};
            
            var map = document.getElementById("walls");
            
            var UNITWIDTH = 1;
            var UNITHEIGHT = 25;

            var camera, scene, renderer, controls;
            var mapSize;
            var totalCubesWide;

            var collidableObjects = [];

            function init() {

                scene = new THREE.Scene();
                scene.background = new THREE.Color(0xffffff);

                renderer = new THREE.WebGLRenderer();
                renderer.setPixelRatio(window.devicePixelRatio);
                renderer.setSize(window.innerWidth, window.innerHeight);

                var container = document.getElementById('container');
                container.appendChild(renderer.domElement);

                camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 2000);
                camera.position.y = 500;
                camera.position.x = 0;
                camera.position.z = 0;
                camera.lookAt(new THREE.Vector3(0, 0, 0));

                scene.add(camera);
                
                controls = new THREE.OrbitControls(camera, renderer.domElement);
                
                controls.enableDamping = true;
                controls.dampingFactor = 0.25;
                controls.panningMode = THREE.HorizontalPanning;
                controls.keys = {
                    LEFT:37,
                    UP:38,
                    RIGHT:39,
                    BOTTOM:40
                }
                
                controls.minDistance = 48;
                controls.maxDistance = 2000;
                controls.maxPolarAngle = Math.PI / 2;

                createMazeCubes();
                createGround();
                addLights();

                window.addEventListener('resize', onWindowResize, false);

            }

            function addLights() {
                var lightOne = new THREE.DirectionalLight(0xffffff);
                lightOne.position.set(1, 1, 1);
                scene.add(lightOne);

                var lightTwo = new THREE.DirectionalLight(0xffffff, .5);
                lightTwo.position.set(1, -1, -1);
                scene.add(lightTwo);
            }
            
            var data = map.value;
            map = JSON.parse(data);

            function createMazeCubes() {
                console.log(map);
              
                //var texture = new THREE.TextureLoader().load("stone.jpg");
                var cubeGeo = new THREE.BoxGeometry(UNITWIDTH, UNITHEIGHT, UNITWIDTH);
                var cubeMat = [
                    new THREE.MeshBasicMaterial({color: 0x8f8f8f}), //right side
                    new THREE.MeshBasicMaterial({color: 0x8f8f8f}), //left side
                    new THREE.MeshBasicMaterial({color: 0x000000}), //top side
                    new THREE.MeshBasicMaterial({color: 0x8f8f8f}), //bottom side
                    new THREE.MeshBasicMaterial({color: 0x8f8f8f}), //front side
                    new THREE.MeshBasicMaterial({color: 0x8f8f8f}) //back side
                ];

                var widthOffset = UNITWIDTH / 2;
                var heightOffset = UNITHEIGHT / 2;

                totalCubesWide = map.length;
                totalCubesHeight = map[0].length;
                console.log(map[0].length);
                for (var i = 0; i < totalCubesWide; i++) {
                    for (var j = 0; j < map[i].length; j++) {
                        
                        if (map[i][j]) {
                            var cube = new THREE.Mesh(cubeGeo, cubeMat);
                            cube.position.z = (i - totalCubesWide / 2) * UNITWIDTH + widthOffset;
                            cube.position.y = heightOffset;
                            cube.position.x = (j - totalCubesWide / 2) * UNITWIDTH + widthOffset;
                            scene.add(cube);
                            collidableObjects.push(cube);
                        }
                    }
                }
                mapSize = totalCubesWide * UNITWIDTH;
                mapHeight = totalCubesHeight * UNITWIDTH;
            }

            function createPerimWalls() {
                var halfMap = mapSize / 2;
                var sign = 1;

                for (var i = 0; i < 2; i++) {
                    var perimGeo = new THREE.PlaneGeometry(mapSize, UNITHEIGHT);
                    var perimMat = new THREE.MeshPhongMaterial({
                        color: 0x464646,
                        side: THREE.DoubleSide
                    });
                    var perimWallLR = new THREE.Mesh(perimGeo, perimMat);
                    var perimWallFB = new THREE.Mesh(perimGeo, perimMat);

                    perimWallLR.position.set(halfMap * sign, UNITHEIGHT / 2, 0);
                    perimWallLR.rotation.y = degreesToRadians(90);
                    scene.add(perimWallLR);

                    collidableObjects.push(perimWallLR);

                    perimWallFB.position.set(0, UNITHEIGHT / 2, halfMap * sign);
                    scene.add(perimWallFB);


                    collidableObjects.push(perimWallFB);

                    sign = -1;
                }
            }

            function createGround() {
                var texture = new THREE.TextureLoader().load("/image/floor.png");
                texture.wrapS = THREE.RepeatWrapping;
                texture.wrapT = THREE.RepeatWrapping;
                texture.repeat.set(4, 4);
                var groundGeo = new THREE.PlaneGeometry(mapHeight+100, mapSize);
                var groundMat = new THREE.MeshPhongMaterial({
                    map: texture,
                    side: THREE.DoubleSide
                });

                var ground = new THREE.Mesh(groundGeo, groundMat);
                ground.position.set(0, 1, 0);

                ground.rotation.x = degreesToRadians(90);
                scene.add(ground);
            }


            function onWindowResize() {

                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();

                renderer.setSize(window.innerWidth, window.innerHeight);

            }

            function animate() {
                requestAnimationFrame(animate);
                controls.update();
                render();
            }


            function render() {
                renderer.render(scene, camera);
            }

            function degreesToRadians(degrees) {
                return degrees * Math.PI / 180;
            }

            function radiansToDegrees(radians) {
                return radians * 180 / Math.PI;
            }


            init();
            animate();

        </script>
</body>

</html>
