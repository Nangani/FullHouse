MyMain = function () {

    var my = this;

    var UNITWIDTH = 90;
    var UNITHEIGHT = 45;

    var camera, scene, renderer;
    var mapSize;
    var totalCubesWide;
    
    var collidableObjects = [];

    my.init = function () {

        scene = new THREE.Scene();
        scene.background = new THREE.Color(0xffffff);

        renderer = new THREE.WebGLRenderer();
        renderer.setPixelRatio(window.devicePixelRatio);
        renderer.setSize(window.innerWidth, window.innerHeight);

        var container = document.getElementById('container');
        container.appendChild(renderer.domElement);

        camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 2000);
        camera.position.y = 2000;
        camera.position.x = 0;
        camera.position.z = 0;
        camera.lookAt(new THREE.Vector3(0,0,0));

        scene.add(camera);

        my.createMazeCubes();

        my.addLights();

        window.addEventListener('resize', onWindowResize, false);

    }

    my.addLights = function () {
        var lightOne = new THREE.DirectionalLight(0xffffff);
        lightOne.position.set(1, 1, 1);
        scene.add(lightOne);

        var lightTwo = new THREE.DirectionalLight(0xffffff, .5);
        lightTwo.position.set(1, -1, -1);
        scene.add(lightTwo);
    }

    my.createMazeCubes = function () {
    var map = [
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, ],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, ],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, ],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, ],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, ],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, ]
  ];

        var cubeGeo = new THREE.BoxGeometry(UNITWIDTH, UNITHEIGHT, UNITWIDTH);
        var cubeMat = new THREE.MeshPhongMaterial({
            color: 0x81cfe0,
        });

        var widthOffset = UNITWIDTH / 2;
        var heightOffset = UNITHEIGHT / 2;

        totalCubesWide = map[0].length;

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
    }

    my.createPerimWalls = function () {
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
    
     my.createGround = function () {
        var groundGeo = new THREE.PlaneGeometry(mapSize, mapSize);
        var groundMat = new THREE.MeshPhongMaterial({
            color: 0xA0522D,
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

    my.animate = function () {
        my.render();
        requestAnimationFrame(my.animate);
    }


    my.render = function () {
        renderer.render(scene, camera);
    }

    function degreesToRadians(degrees) {
        return degrees * Math.PI / 180;
    }

    function radiansToDegrees(radians) {
        return radians * 180 / Math.PI;
    }


    my.init();
    my.animate();

}
