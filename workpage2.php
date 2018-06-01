<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-s=1.0">
    <link rel="stylesheet" href="workpagestylesheet.css">
    <link rel="stylesheet" href="sidebar.css">
    <script src=jquery-3.3.1.min.js></script>
    <script src="jquery-ui.min.js"></script>
    <script type="text/javascript" src="buttonaction.js"></script>
    <script type="text/javascript" src="sidebar.js"></script>
    <script src="three.js"></script>
    <script src="OrbitControls.js"></script>
    <script src="dat.gui.min.js"></script>
    <title>Load Your House</title>
</head>
<body>
    <div>
        <img style="margin-left: 2%" src="images/workpagelogo.png">
    </div>
    <div id="leftdiv">
        <aside class="sidebar">
            <div class="sidebar-content">
                <strong>&nbsp;&nbsp;MENU</strong><br><br>
                <div class="panels">
                    <input type="image" class="top" src="images/Door-icon.png" onclick="firstButtonClicked()" />
                    <input type="image" class="top" src="images/hammer.png" onclick="secondButtonClicked()" />
                    <input type="image" class="top" src="images/Household-Sofa-icon.png" onclick="thirdButtonClicked()" />
                </div><br><br><br>
                <div class="midbuttons1">
                    <input type="image" id="door" value="models/door/door" class="mid" src="images/door.JPG" onclick="passValue(this.id)"/>
                </div>
                <div class="midbuttons2" style="display:none">
                    <input type="image" id="wall" value="wall" class="colors" src="images/brick-wall.png" onclick="passValue(this.id)"/>
                    <input type="image" id="wallpaint1" value="images/wallpainting1" class="colors" src="images/wallpainting1.PNG" onclick="passValue(this.id)"/>
                    <input type="image" id="wallpaint2" value="images/wallpainting2" class="colors" src="images/wallpainting2.PNG" onclick="passValue(this.id)"/>
                    <input type="image" id="wallpaint3" value="images/wallpainting3" class="colors" src="images/wallpainting3.PNG" onclick="passValue(this.id)"/>
                    <input type="image" id="wallpaint4" value="images/wallpainting4" class="colors" src="images/wallpainting4.PNG" onclick="passValue(this.id)"/>
                    <input type="image" id="wallpaint5" value="images/wallpainting5" class="colors" src="images/wallpainting5.PNG" onclick="passValue(this.id)"/>
                </div>
                <div class="midbuttons3" style="display:none">
                    <input type="button" class="type" value="Kitchen" id="kitchen" onclick="kitchenButtonClicked()" />
                    <input type="button" class="type" value="Bedroom" id="bedroom" onclick="bedroomButtonClicked()" />
                    <input type="button" class="type" value="Livingroom" id="livingroom" onclick="livingroomButtonClicked()" />
                    <input type="button" class="type" value="Bathroom" id="bathroom" onclick="bathroomButtonClicked()" />
                    <input type="button" class="type" value="Etc" id="etc" onclick="etcButtonClicked()" />
                    <br>
                </div>
                <div class="wrapper" style="display:none">
                    <div class="bottombuttons1" style="display: none">
                        <input type="image" id="chair" class="bottom" src="Furniture/chair/chair.PNG" value="Furniture/chair/chair" onclick="passValue(this.id)" />
                        <input type="image" id="microwave" class="bottom" src="Furniture/microwave/microwave.PNG" value="Furniture/microwave/microwave" onclick="passValue(this.id)" />
                        <input type="image" id="refrigerator" class="bottom" src="Furniture/refrigerator/refrigerator.PNG" value="Furniture/refrigerator/refrigerator" onclick="passValue(this.id)"/>
                        <input type="image" id="sink" class="bottom" src="Furniture/sink/sink.PNG" value="Furniture/sink/sink" onclick="passValue(this.id)"/>
                        <input type="image" id="sink1" class="bottom" src="Furniture/sink1/sink1.PNG" value="Furniture/sink1/sink1" onclick="passValue(this.id)"/>
                        <input type="image" id="sink2" class="bottom" src="Furniture/sink2/sink2.PNG" value="Furniture/sink2/sink2" onclick="passValue(this.id)"/>
                    </div>
                    <div class="bottombuttons2" style="display: none">
                        <input type="image" id="bed" class="bottom" src="Furniture/bed/bed.PNG" value="Furniture/bed/bed" onclick="passValue(this.id)"/>
                    </div>
                    <div class="bottombuttons3" style="display: none">
                        <input type="image" id="drawer" class="bottom" src="Furniture/drawer/drawer.PNG" value="Furniture/drawer/drawer" onclick="passValue(this.id)"/>
                        <input type="image" id="bigdrawer" class="bottom" src="Furniture/bigdrawer/bigdrawer.PNG" value="Furniture/bigdrawer/bigdrawer" onclick="passValue(this.id)"/>
                        <input type="image" id="bookshelf" class="bottom" src="Furniture/bookshelf/bookshelf.PNG" value="Furniture/bookshelf/bookshelf" onclick="passValue(this.id)"/>
                        <input type="image" id="smalltable" class="bottom" src="Furniture/smalltable/smalltable.PNG" value="Furniture/smalltable/smalltable" onclick="passValue(this.id)"/>
                        <input type="image" id="table" class="bottom" src="Furniture/table/table.PNG" value="Furniture/table/table" onclick="passValue(this.id)"/>
                        <input type="image" id="sofa" class="bottom" src="Furniture/sofa/sofa.PNG" value="Furniture/sofa/sofa" onclick="passValue(this.id)"/>
                        <input type="image" id="sofa1" class="bottom" src="Furniture/sofa1/sofa1.PNG" value="Furniture/sofa1/sofa1" onclick="passValue(this.id)"/>
                        <input type="image" id="tv" class="bottom" src="Furniture/tv/tv.PNG" value="Furniture/tv/tv" onclick="passValue(this.id)"/>
                        <input type="image" id="tvtable" class="bottom" src="Furniture/tvtable/tvtable.PNG" value="Furniture/tvtable/tvtable" onclick="passValue(this.id)"/>
                    </div>
                    <div class="bottombuttons4" style="display: none">
                        <input type="image" id="bathsink" class="bottom" src="Furniture/bathsink/bathsink.PNG" value="Furniture/bathsink/bathsink" onclick="passValue(this.id)"/>
                        <input type="image" id="bathtub" class="bottom" src="Furniture/bathtub/bathtub.PNG" value="Furniture/bathtub/bathtub" onclick="passValue(this.id)"/>
                        <input type="image" id="toilet" class="bottom" src="Furniture/toilet/toilet.PNG" value="Furniture/toilet/toilet" onclick="passValue(this.id)"/>
                    </div>
                    <div class="bottombuttons5" style="display: none">
                        <input type="image" id="lamp" class="bottom" src="Furniture/lamp/lamp.PNG" value="Furniture/lamp/lamp" onclick="passValue(this.id)"/>
                        <input type="image" id="mirror" class="bottom" src="Furniture/mirror/mirror.PNG" value="Furniture/mirror/mirror" onclick="passValue(this.id)"/>
                        <input type="image" id="mirror1" class="bottom" src="Furniture/mirror1/mirror1.PNG" value="Furniture/mirror1/mirror1" onclick="passValue(this.id)"/>
                        <input type="image" id="boxshelf" class="bottom" src="Furniture/boxshelf/boxshelf.PNG" value="Furniture/boxshelf/boxshelf" onclick="passValue(this.id)"/>
                        <input type="image" id="talllamp" class="bottom" src="Furniture/talllamp/talllamp.PNG" value="Furniture/talllamp/talllamp" onclick="passValue(this.id)"/>
                        <input type="image" id="trashcan" class="bottom" src="Furniture/trashcan/trashcan.PNG" value="Furniture/trashcan/trashcan" onclick="passValue(this.id)"/>
                    </div>
                </div>
            </div>
            <button><span class="sidebar-btn">OPEN</span></button>
        </aside>

    </div>
    <div id="rightdiv" style="width: 1200px; height: 800px ;">
    <?php
        $_FILES['img']['name']="plan.png";
        $uploadAddr = 'C:/xampp/htdocs/';
        $uploadFile = $uploadAddr.basename($_FILES['img']['name']);
        move_uploaded_file($_FILES['img']['tmp_name'], 'plan.png');

        $error =  exec('C:/Python36/python.exe FindWall.py');
        exec('C:/Python36/python.exe PrintWall.py');
        $python = file("ww.txt");

    ?>
    <input type="hidden" id="walls" value=<?php echo "\"".$python[0]."\"";?> >    
        <script type="text/javascript" >

            var map = document.getElementById("walls");
            var rightdiv = document.getElementById("rightdiv");
            var CANVAS_WIDTH = rightdiv.offsetWidth;
            var CANVAS_HEIGHT = rightdiv.offsetHeight;
            var UNITWIDTH = 1;
            var UNITHEIGHT = 75;
            var ground;
            var camera, scene, renderer, controls;
            var mapSize;
            var totalCubesWide;
            var isDeleteDown = false;
            var isChangeDown = false;
            var isAttributeDown = false;
            var collidableObjects = [];
            var rollOverMesh, rollOverMaterial, rollOverGeo;
            var clickMesh;
            var rotations = 0;
            var objects = [];
            var container;
            var plane, cube;
            var basicX, basicY, basicZ, basicColor,basicRotation;
            var raycaster, mouse;
            var params = {
                rotation: 0,
                scaleX: 1,
                scaleY: 1,
                scaleZ: 1,
                color: 0xFF6b6b,
                EDIT: true
            };
            var gui;
            var wall;
            var groundPlane;
            var currentObject, currentColor;
            var collidableObjects = [];
            var path= "";
            var numDoor=0;
            function passValue(id) {
                var furni = document.getElementById(id);
                rotations = 0;
                path = furni.value;
                rollOverGeo = new THREE.ObjectLoader();

                    scene.remove(rollOverMesh);

                    if(path == "wall") {
                    var wallGeo = new THREE.BoxGeometry(UNITWIDTH * 2, UNITHEIGHT, UNITWIDTH * 2);
                    var wallMat = new THREE.MeshPhongMaterial({
                        color: 0xff0000, opacity: 0.5, transparent:true
                    });
                    var tempMesh = new THREE.Mesh(wallGeo, wallMat);
                    rollOverMesh = tempMesh;

                    tempMesh.position.y = 38;
                    scene.add(tempMesh);
                    }
                    else if(path=="images/wallpainting1" ||path=="images/wallpainting3" ||path=="images/wallpainting2" ||path=="images/wallpainting4" ||path=="images/wallpainting5" ){
                        var texture = new THREE.TextureLoader().load(path+".PNG");
                        var paintGeo = new THREE.BoxGeometry(50, UNITHEIGHT, UNITWIDTH);
                        var paintMat = new THREE.MeshPhongMaterial({
                                    map: texture
                        });
                        var paintMesh = new THREE.Mesh(paintGeo, paintMat);
                        paintMesh.position.y = 38;
                        paintMesh.rotation.y += rotations*2;
                        rollOverMesh = paintMesh;
                        scene.add(paintMesh);
                    }
                    else if(path == "models/door/door") {
                        rollOverGeo.load(path + ".json", function(object) {
                            object.scale.z = 40;
                            object.scale.x = 150;
                            object.scale.y = 30;
                            
                            rollOverMesh = object;
                            scene.add(object);
                        });
                    }

                    else {
                        rollOverGeo.load(path + ".json", function(object) {
                            object.scale.x = 15;
                            object.scale.y = 15;
                            object.scale.z = 15;
                            rollOverMesh = object;
                            scene.add(object);
                        });
                    }
                }
            function init() {

                renderer = new THREE.WebGLRenderer();
                renderer.setPixelRatio(window.devicePixelRatio);
                renderer.setSize(rightdiv.offsetWidth-6, rightdiv.offsetHeight-6);

                rightdiv.appendChild(renderer.domElement);

                scene = new THREE.Scene();
                scene.background = new THREE.Color(0xffffff);

                camera = new THREE.PerspectiveCamera(60, CANVAS_WIDTH / CANVAS_HEIGHT, 1, 10000);
                camera.position.y = 800;
                camera.position.x = 0;
                camera.position.z = 0;
                camera.lookAt(new THREE.Vector3(0, 0, 0));

                scene.add(camera);

                controls = new THREE.OrbitControls(camera, renderer.domElement);

                controls.enableDamping = true;
                controls.dampingFactor = 0.25;
                controls.panningMode = THREE.HorizontalPanning;
                controls.keys = {
                    LEFT: 37,
                    UP: 38,
                    RIGHT: 39,
                    BOTTOM: 40
                }
                controls.enabled = false;

                raycaster = new THREE.Raycaster();
                mouse = new THREE.Vector2();
                var geometry = new THREE.PlaneBufferGeometry(1000, 1000);
                geometry.rotateX(-Math.PI / 2);

                controls.minDistance = 48;
                controls.maxDistance = 2000;
                controls.maxPolarAngle = Math.PI / 2;

                createColorCubes();
                addLights();

                gui = new dat.GUI();
                gui.add(params, 'rotation', 0, 360 );
                gui.add(params, 'scaleX', 0.1, 5);
                gui.add(params, 'scaleY', 0.1, 5);
                gui.add(params, 'scaleZ', 0.1, 5);
                gui.addColor(params, 'color');
                gui.add(params,'EDIT');
                gui.open();

                document.addEventListener('mousemove', onDocumentMouseMove, false);
                document.addEventListener('mousedown', onDocumentMouseDown, false);
                document.addEventListener('keydown', onDocumentKeyDown, false);
                document.addEventListener('keyup', onDocumentKeyUp, false);
                window.addEventListener('resize', onWindowResize, false);
            }


            function addLights() {
                var ambientLight = new THREE.AmbientLight(0x606060);
                scene.add(ambientLight);
                var directionalLight = new THREE.DirectionalLight(0xffffff);
                directionalLight.position.set(1, 0.75, 0.5).normalize();
                scene.add(directionalLight);
            }

            function createColorCubes(rgbColor) {
                var data = map.value;
                
                map = JSON.parse(data);
                
                var cubeGeo = new THREE.BoxGeometry(UNITWIDTH, UNITHEIGHT, UNITWIDTH);
                var cubeMat = new THREE.MeshPhongMaterial({
                    color: 0x8f8f8f
                });

                var merged = new THREE.Geometry();
                var widthOffset = UNITWIDTH / 2;
                var heightOffset = UNITHEIGHT / 2;

                totalCubesWide = map[0].length;
                totalCubesHeight = map.length;
               
                var door=[];
                var k=0,l=0;
                var k2=0,l2=0;
                
                for (var i = 0; i < totalCubesHeight; i++) {
                   
                    for (var j = 0; j < map[i].length; j++) {
                     
                        if (map[i][j]) {
                            var cube = new THREE.Mesh(cubeGeo, cubeMat);
                            cube.position.x = (j - totalCubesWide / 2) * UNITWIDTH + widthOffset;
                            cube.position.y = heightOffset;
                            cube.position.z = (i - totalCubesHeight / 2) * UNITWIDTH + widthOffset;
                            cube.matrixAutoUpdate = false;
                            cube.updateMatrix();
                            merged.merge(cube.geometry, cube.matrix);
                            
                        }
                        if(map[i][j] ==2 && alreadyDoor(i,j,door)){
                            
                            var loader = new THREE.ObjectLoader();
                            door.push([i,j]);
                            var x=i;
                            var y=j;
                            while( map[x][y]==2){
                                    y++;      
                            }
                            y--;
                            while( map[x][y]==2){
                                    x++;   
                            }   
                            x--;
                            door.push([x,y]);
                            
                           
                            loader.load("/models/door/door.json", function(object) {
                                numDoor+=1;
                                object.scale.z = 40;
                                object.scale.y = 30;
                                object.position.y=1;
                                if(door[numDoor*2-1][1]-door[numDoor*2-2][1] > door[numDoor*2-1][0]-door[numDoor*2-2][0]){
                                    object.rotation.y += Math.PI/2;
                                    object.scale.x = (door[numDoor*2-1][0]-door[numDoor*2-2][0])*50;
                                }
                                else{
                                    object.scale.x = (door[numDoor*2-1][1]-door[numDoor*2-2][1])*50;
                                }
                                object.position.x=((door[numDoor*2-1][1]-door[numDoor*2-2][1])/2+door[numDoor*2-2][1] - (totalCubesWide/2)) * UNITWIDTH ;
                                object.position.z=((door[numDoor*2-1][0]-door[numDoor*2-2][0])/2+door[numDoor*2-2][0] - (totalCubesHeight/2)) * UNITWIDTH ;
                                
                                scene.add(object);
                                objects.push(object);
                                });
                        }
                    }
                }   
                var mergeMesh = new THREE.Mesh(merged, cubeMat);
                
                merged.computeBoundingBox();
                wall = mergeMesh;
                wall.name = "wall";
                objects.push(wall);
                scene.add(mergeMesh);
                
                mapSize = totalCubesWide * UNITWIDTH;
                mapHeight = totalCubesHeight * UNITWIDTH;

                var mergedGround = new THREE.Geometry();
                var texture = new THREE.TextureLoader().load("/images/floor.png");
                
                var groundGeo = new THREE.PlaneGeometry(1,1,1);
                var groundMat = new THREE.MeshPhongMaterial({
                    map: texture,

                    side: THREE.DoubleSide
                });

                for(var x = merged.boundingBox.min.x; x < merged.boundingBox.max.x; x++) {
                    for(var z = merged.boundingBox.min.z; z < merged.boundingBox.max.z; z++) {
                        
                        ground = new THREE.Mesh(groundGeo, groundMat);
                        ground.position.set(x, 1, z);
                        ground.rotation.x = degreesToRadians(90);
                        ground.matrixAutoUpdate = false;
                        ground.updateMatrix();
                        mergedGround.merge(ground.geometry, ground.matrix);
                        
                    }
                }
                var mergeGround = new THREE.Mesh(mergedGround, groundMat);
                ground = mergeGround;
               
                objects.push(ground);
                scene.add(mergeGround);
            }

            
            function createGround() {
                var texture = new THREE.TextureLoader().load("/images/floor.png");
                texture.wrapS = THREE.RepeatWrapping;
                texture.wrapT = THREE.RepeatWrapping;
                texture.repeat.set(4, 4);
                var groundGeo = new THREE.PlaneGeometry(1,1,1);
                var groundMat = new THREE.MeshPhongMaterial({
                    map: texture,

                    side: THREE.DoubleSide
                });

                ground = new THREE.Mesh(groundGeo, groundMat);
                ground.position.set(0, 1, 0);
                ground.name="ground"
                ground.rotation.x = degreesToRadians(90);
                scene.add(ground);
                objects.push(ground);
            }


            function onWindowResize() {

                camera.aspect = CANVAS_WIDTH / CANVAS_HEIGHT;
                camera.updateProjectionMatrix();
                

            }
 
            function animate() {
                requestAnimationFrame(animate);
                
                render();

            }

            function render() {
                if(params.EDIT == true) {
                    controls.enabled = false;
                    if(rollOverMesh != null && isAttributeDown == false && isDeleteDown == false)
                        rollOverMesh.visible = true;
                }
                else{
                    controls.enabled = true;
                    if(rollOverMesh != null)
                        rollOverMesh.visible = false;
                }
                if (currentObject != null) {
                    if(path!="models/door/door"){
                        currentObject.rotation.y = basicRotation +degreesToRadians(params.rotation);
                    }
                    currentObject.scale.x = basicX * params.scaleX;
                    currentObject.scale.y = basicY * params.scaleY;
                    currentObject.scale.z = basicZ * params.scaleZ;
                    basicColor = params.color;
                    currentObject.material.color.setHex(params.color);
                }
                renderer.render(scene, camera);
            }

            function degreesToRadians(degrees) {
                return degrees * Math.PI / 180;
            }

            function radiansToDegrees(radians) {
                return radians * 180 / Math.PI;
            }

            function onDocumentMouseMove(event) {
                event.preventDefault();
                mouse.set(((event.clientX-rightdiv.offsetLeft) / rightdiv.offsetWidth) * 2 - 1, -((event.clientY-rightdiv.offsetTop) / rightdiv.offsetHeight) * 2 + 1);
                raycaster.setFromCamera(mouse, camera);
                var intersects = raycaster.intersectObjects(objects, true);
                if (intersects.length > 0) {
                    var intersect = intersects[0];
                    
                    if(path == "wall")
                        intersect.point.y = UNITHEIGHT / 2;
                    if(intersect.object == wall)
                            intersect.point.y=1;
                    if(path=="images/wallpainting1" ||path=="images/wallpainting3" ||path=="images/wallpainting2" ||path=="images/wallpainting4" ||path=="images/wallpainting5" )
                        intersect.point.y=38;
                    if(rollOverMesh != null)
                        rollOverMesh.position.copy(intersect.point).add(intersect.face.normal);

                  
                }
                render();
            }

            function onDocumentMouseDown(event) {
                event.preventDefault();
                mouse.set(((event.clientX-rightdiv.offsetLeft) / rightdiv.offsetWidth) * 2 - 1, -((event.clientY-rightdiv.offsetTop) / rightdiv.offsetHeight) * 2 + 1);
                raycaster.setFromCamera(mouse, camera);
                var intersects = raycaster.intersectObjects(objects, true);
                if (intersects.length > 0) {
                    var intersect = intersects[0];
                    
                    if (isDeleteDown && controls.enabled == false) {
                        if (intersect.object != ground && intersect.object != wall) {
                            
                            if(intersect.object.parent.parent == null){
                                scene.remove( intersect.object );
                                objects.splice( objects.indexOf( intersect.object ), 1 );
                            }
                            else{

                                scene.remove( intersect.object.parent.parent );
                            
                                objects.splice( objects.indexOf( intersect.object.parent.parent ), 1 );
                            }
                            
                        }
                    } else if (isAttributeDown && controls.enabled == false) {
                        if (intersect.object != ground && intersect.object != wall) {
                           
                            basicX = intersect.object.scale.x;
                            basicY = intersect.object.scale.y;
                            basicZ = intersect.object.scale.z;
                            basicRotation = intersect.object.rotation.y;

                            if (currentObject != null) {
                                if (basicColor == 0XFF6b6b)
                                    currentObject.material.color.setHex(currentColor);
                                else
                                    currentObject.material.color.setHex(params.color);
                                basicColor = 0XFF6b6b;
                            }
                            gui.__controllers[0].setValue(0);
                            gui.__controllers[1].setValue(1);
                            gui.__controllers[2].setValue(1);
                            gui.__controllers[3].setValue(1);
                            gui.__controllers[4].setValue(0xff6b6b);
                            currentObject = intersect.object;
                            currentColor = currentObject.material.color.getHex();
                            currentObject.material.color.setHex(params.color);
                            
                        }
                    } else if (controls.enabled == false && rollOverMesh != null) {
                        if(path == "wall") {
                            var wallGeo = new THREE.BoxGeometry(UNITWIDTH * 2, UNITHEIGHT, UNITWIDTH * 2);
                            var wallMat = new THREE.MeshPhongMaterial({
                                color: 0x8f8f8f
                            });
                            var tempMesh = new THREE.Mesh(wallGeo, wallMat);

                            
                                intersect.point.y = 38.5;
                            tempMesh.position.copy(intersect.point).add(intersect.face.normal);
                           
                            
                            clickMesh = tempMesh;
                            scene.add(tempMesh);
                            objects.push(clickMesh);
                        }
                        else if(path=="images/wallpainting1" ||path=="images/wallpainting3" ||path=="images/wallpainting2" ||path=="images/wallpainting4" ||path=="images/wallpainting5" ){
                        
                            if(intersect.object == wall){
                                var texture = new THREE.TextureLoader().load(path+".PNG");
                                var paintGeo = new THREE.BoxGeometry(50, UNITHEIGHT, UNITWIDTH);
                                var paintMat = new THREE.MeshPhongMaterial({
                                    map: texture
                                });
                                var paintMesh = new THREE.Mesh(paintGeo, paintMat);
                                intersect.point.y = 38;
                                paintMesh.rotation.y += rotations;
                                paintMesh.position.copy(intersect.point).add(intersect.face.normal);
                                clickMesh = paintMesh;
                                scene.add(paintMesh);
                                objects.push(clickMesh);
                            }

                        }
                        else if(path == "models/door/door") {
                            if(intersect.object == wall) {
                                var loader = new THREE.ObjectLoader();
                                loader.load(path + ".json", function(object) {
                                    object.scale.z = 40;
                                    object.scale.x = 150;
                                    object.scale.y = 30;
                                    object.position.y=1;
                                    intersect.point.y=1;
                                    object.rotation.y += rotations;
                                    object.position.copy(intersect.point).add(intersect.face.normal);
                                    clickMesh = object;
                                    scene.add(object);
                                    objects.push(object);
                                });
                            }
                        }
                        else{
                            var collisionDetect=false;
                            var loader = new THREE.ObjectLoader();
                            loader.load(path + ".json", function(object) {
                                
                                object.scale.x = 15;
                                object.scale.y = 15;
                                object.scale.z = 15;
                                
                                if(intersect.object == wall)
                                    intersect.point.y=1;
                                object.position.copy(intersect.point).add(intersect.face.normal);
                                clickMesh = object.children[0].children[0];
                                
                                var helper  = new THREE.Box3().setFromObject(object);
                                
                                var rotationMatrix = new THREE.Matrix3();
                                rotationMatrix.set(Math.cos(rotations),0,Math.sin(rotations),0,0,0,-Math.sin(rotations),0,Math.cos(rotations));
                                object.rotation.y += rotations;
                                    
                                    var globalVertex1 = new THREE.Vector3(helper.min.x,0,0);
                                    var globalVertex2 = new THREE.Vector3(helper.max.x,0,0);
                                    var globalVertex3 = new THREE.Vector3(0,0,helper.min.z);
                                    var globalVertex4 = new THREE.Vector3(0,0,helper.max.z);
                                    var globalVertex5 = new THREE.Vector3(helper.min.x,0,helper.min.z);
                                    var globalVertex6 = new THREE.Vector3(helper.max.x,0,helper.min.z);
                                    var globalVertex7 = new THREE.Vector3(helper.max.x,0,helper.max.z);
                                    var globalVertex8 = new THREE.Vector3(helper.min.x,0,helper.max.z);

                                    
                                    var radius1 = object.position.x-helper.min.x;
                                    var radius2 = helper.max.x-object.position.x;
                                    var radius3 = object.position.z-helper.min.z;
                                    var radius4 = helper.max.z-object.position.z;
                                    var radius5 = Math.sqrt(radius1*radius1+radius3*radius3);
                                    var radius6 = Math.sqrt(radius2*radius2+radius3*radius3);
                                    var radius7 = Math.sqrt(radius2*radius2+radius4*radius4);
                                    var radius8 = Math.sqrt(radius1*radius1+radius4*radius4);

                                    var nodeVertex1 = new THREE.Vector3(-1,0,0);
                                    var nodeVertex2 = new THREE.Vector3(1,0,0);
                                    var nodeVertex3 = new THREE.Vector3(0,0,-1);
                                    var nodeVertex4 = new THREE.Vector3(0,0,1);
                                    var nodeVertex5 = new THREE.Vector3(-radius1,0,-radius3);
                                    var nodeVertex6 = new THREE.Vector3(radius2,0,-radius3);
                                    var nodeVertex7 = new THREE.Vector3(radius2,0,radius4);
                                    var nodeVertex8 = new THREE.Vector3(-radius1,0,radius4);

                                    var objectD = [radius1,radius2,radius3,radius4,radius5,radius6,radius7,radius8];
                                    var globalVertex = [globalVertex1,globalVertex2,globalVertex3,globalVertex4,globalVertex5,globalVertex6,globalVertex7,globalVertex8];
                                    var nodeVertex = [nodeVertex1.applyMatrix3(rotationMatrix),nodeVertex2.applyMatrix3(rotationMatrix),nodeVertex3.applyMatrix3(rotationMatrix),nodeVertex4.applyMatrix3(rotationMatrix),nodeVertex5.applyMatrix3(rotationMatrix),nodeVertex6.applyMatrix3(rotationMatrix),nodeVertex7.applyMatrix3(rotationMatrix),nodeVertex8.applyMatrix3(rotationMatrix)];       
                                    var position = object.position.clone();
                                    position.y = object.position.y+(helper.max.y-helper.min.y)/2;
                                    
                                    for(var i = 0;i<8;i++){
                                        var ray = new THREE.Raycaster( position, nodeVertex[i].clone().normalize() );
                                        var collisionResults = ray.intersectObjects( objects,true );
                                        if ( collisionResults.length > 0  ) 
                                        {
                                            if(collisionResults[0].object == ground )
                                                continue; 
                                            
                                            if(collisionResults[0].distance < objectD[i] ){
                                                collisionDetect = true;
                                                
                                            }
                                        }
                                    }                         
                                if(collisionDetect == false){
                                    scene.add(object);
                                    objects.push(object);
                                }
                            });
                        }
                    }
                    render();
                }
            }
            function onDocumentKeyDown(event) {
                switch (event.keyCode) {
                    
                    case 65:
                        isAttributeDown = true;
                        if(rollOverMesh != null) rollOverMesh.visible = false;
                        break;
                    case 68:
                        isDeleteDown = true;
                        if(rollOverMesh != null) rollOverMesh.visible = false;
                        break;
                    
                }
            }
            function findDoor(x,y,door,map){
                var i=x;
                var j=y;
                while( map[i][j]==2){
                    if(map[i][j+1]==2){
                        j++;
                    }
                }
                while( map[i][j]==2){
                    if(map[i+1][j]==2){
                        i++;
                    }
                }   
                door.push([i,j]);
            }   
            function alreadyDoor(x,y,door){
                for(var i = 0; i<door.length; i+=2 ){
                    if(door[i][0]<=x && x<=door[i+1][0]){
                        if(door[i][1]<=y && y<=door[i+1][1]){
                            return false;
                        }
                    }
                }
                return true;
            }      
            function onDocumentKeyUp(event) {
                switch (event.keyCode) {
                    case 65:
                        isAttributeDown = false;
                        if(rollOverMesh != null) rollOverMesh.visible = true;
                        break;
                    case 68:
                        isDeleteDown = false;
                        if(rollOverMesh != null) rollOverMesh.visible = true;
                        break;
                    case 82:
                        if(rollOverMesh != null){
                            rollOverMesh.rotation.y += Math.PI / 2;
                            rotations += Math.PI / 2;
                        }
                        break;
                }
            }
            function findCoordinate(x,y,arr){
                for(var i = 0;i<arr.length;i++){
                    if(arr[i][0]==x && arr[i][1]==y)
                        return false;
                }
                return true;
            }
            init();
            animate();
        </script>
    </div>
</body>
</html>
