import streamlit as st

st.set_page_config(page_title="Python 3D City Driver", page_icon="🚗", layout="wide")

st.title("🚗 3D Open-World City Driver")
st.write("Drive around a 3D procedurally generated block city using WASD or Arrow Keys!")

# Embedded HTML5/WebGL Three.js Game Engine
game_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body { margin: 0; overflow: hidden; background-color: #050510; font-family: sans-serif; }
        #canvas-container { width: 100vw; height: 75vh; position: relative; }
        #ui { position: absolute; top: 15px; left: 15px; color: #fff; background: rgba(0,0,0,0.7); padding: 15px; border-radius: 8px; pointer-events: none; border: 1px solid #333; }
        h3 { margin: 0 0 8px 0; color: #00ffcc; font-size: 16px; }
        p { margin: 4px 0; font-size: 13px; color: #bbb; }
    </style>
    <!-- Include Three.js via Cloudflare CDN -->
    <script src="https://cloudflare.com"></script>
</head>
<body>
    <div id="canvas-container">
        <div id="ui">
            <h3>🎮 CITY SANDBOX CONTROLS</h3>
            <p><b>W / Up Arrow:</b> Accelerate Forward</p>
            <p><b>S / Down Arrow:</b> Reverse / Brake</p>
            <p><b>A / Left Arrow:</b> Steer Left</p>
            <p><b>D / Right Arrow:</b> Steer Right</p>
            <p id="speedometer" style="color: #ffff00; font-weight: bold; margin-top: 10px; font-size: 15px;">Speed: 0 km/h</p>
        </div>
    </div>

    <script>
        // --- 1. SETUP 3D WORLD RENDERING CONTEXT ---
        const container = document.getElementById('canvas-container');
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0x0a0a1a);
        scene.fog = new THREE.FogExp2(0x0a0a1a, 0.015);

        const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(container.clientWidth, container.clientHeight);
        renderer.shadowMap.enabled = true;
        container.appendChild(renderer.domElement);

        // --- 2. LIGHTING SYSTEM ---
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.3);
        scene.add(ambientLight);

        const sunLight = new THREE.DirectionalLight(0xffffff, 0.8);
        sunLight.position.set(50, 200, 50);
        sunLight.castShadow = true;
        scene.add(sunLight);

        // --- 3. GENERATE OPEN WORLD MAP (GROUND & ROADS) ---
        const worldSize = 400;
        const groundGeo = new THREE.PlaneGeometry(worldSize, worldSize);
        const groundMat = new THREE.MeshStandardMaterial({ color: 0x222225, roughness: 0.8 });
        const ground = new THREE.Mesh(groundGeo, groundMat);
        ground.rotation.x = -Math.PI / 2;
        ground.receiveShadow = true;
        scene.add(ground);

        // Grid lines simulating city streets
        const grid = new THREE.GridHelper(worldSize, 40, 0x00ffcc, 0x444444);
        grid.position.y = 0.01;
        scene.add(grid);

        // --- 4. PROCEDURAL BUILDING GENERATION (SKYSCRAPERS) ---
        const buildings = [];
        const buildingCount = 70;
        
        for (let i = 0; i < buildingCount; i++) {
            const bWidth = Math.random() * 15 + 10;
            const bHeight = Math.random() * 60 + 20;
            const bDepth = Math.random() * 15 + 10;
            
            const bGeo = new THREE.BoxGeometry(bWidth, bHeight, bDepth);
            // Neon matrix colors simulating a sci-fi GTA city landscape
            const bColor = new THREE.Color().setHSL(Math.random() * 0.1 + 0.5, 0.8, 0.3);
            const bMat = new THREE.MeshStandardMaterial({ color: bColor, roughness: 0.5 });
            const building = new THREE.Mesh(bGeo, bMat);
            
            // Randomly scatter around grid blocks avoiding spawn center point (0,0)
            let bx = (Math.random() - 0.5) * (worldSize - 60);
            let bz = (Math.random() - 0.5) * (worldSize - 60);
            if (Math.abs(bx) < 25) bx += 30;
            if (Math.abs(bz) < 25) bz += 30;
            
            building.position.set(bx, bHeight / 2, bz);
            building.castShadow = true;
            building.receiveShadow = true;
            scene.add(building);
            buildings.push(building);
        }

        // Add a giant stunt ramp structure inside the sandbox layout
        const rampGeo = new THREE.BoxGeometry(15, 8, 30);
        const rampMat = new THREE.MeshStandardMaterial({ color: 0xff3300 });
        const ramp = new THREE.Mesh(rampGeo, rampMat);
        ramp.position.set(0, 1, -40);
        ramp.rotation.x = 0.25; // Incline slant
        scene.add(ramp);

        // --- 5. VEHICLE CHARACTER OBJECT CONFIGURATION ---
        const carGroup = new THREE.Group();
        
        // Chassis Body Box
        const bodyGeo = new THREE.BoxGeometry(3, 1, 5);
        const bodyMat = new THREE.MeshStandardMaterial({ color: 0x00ffcc, metalness: 0.8, roughness: 0.2 });
        const carBody = new THREE.Mesh(bodyGeo, bodyMat);
        carBody.position.y = 0.6;
        carBody.castShadow = true;
        carGroup.add(carBody);

        // Cabin Box
        const cabinGeo = new THREE.BoxGeometry(2.4, 0.8, 2.5);
        const cabinMat = new THREE.MeshStandardMaterial({ color: 0x111111, roughness: 0.1 });
        const carCabin = new THREE.Mesh(cabinGeo, cabinMat);
        carCabin.position.set(0, 1.4, -0.4);
        carGroup.add(carCabin);

        // Headlights markers
        const lightGeo = new THREE.BoxGeometry(0.5, 0.2, 0.2);
        const lightMat = new THREE.MeshBasicMaterial({ color: 0xffffaa });
        const leftLight = new THREE.Mesh(lightGeo, lightMat);
        leftLight.position.set(-1, 0.6, -2.5);
        const rightLight = leftLight.clone();
        rightLight.position.x = 1;
        carGroup.add(leftLight, rightLight);

        carGroup.position.set(0, 0, 0);
        scene.add(carGroup);

        // --- 6. PHYSICS PHYSICS AND VEHICLE TELEMETRY VARIABLES ---
        let speed = 0;
        let maxSpeed = 1.8;
        let acceleration = 0.04;
        let friction = 0.015;
        let turnSpeed = 0.04;
        let carAngle = 0;

        // Input Listener Vectors
        const keys = { w: false, s: false, a: false, d: false, ArrowUp: false, ArrowDown: false, ArrowLeft: false, ArrowRight: false };

        window.addEventListener('keydown', (e) => { if (e.key in keys || ['W','A','S','D','w','a','s','d'].includes(e.key)) keys[e.key.toLowerCase()] = true; });
        window.addEventListener('keyup', (e) => { if (e.key in keys || ['W','A','S','D','w','a','s','d'].includes(e.key)) keys[e.key.toLowerCase()] = false; });

        // --- 7. MAIN ENGINE ANIMATION LOOP ---
        const clock = new THREE.Clock();
        const speedoElement = document.getElementById('speedometer');

        function animate() {
            requestAnimationFrame(animate);

            // Handle Throttle Inputs
            if (keys['w'] || keys['arrowup']) {
                if (speed < maxSpeed) speed += acceleration;
            } else if (keys['s'] || keys['arrowdown']) {
                if (speed > -maxSpeed/2) speed -= acceleration;
            } else {
                // Apply drag deceleration physics friction
                if (speed > 0) speed = Math.max(0, speed - friction);
                if (speed < 0) speed = Math.min(0, speed + friction);
            }

            // Handle Steer Angles
            if (keys['a'] || keys['arrowleft']) {
                if (Math.abs(speed) > 0.05) carAngle += turnSpeed * (speed > 0 ? 1 : -1);
            }
            if (keys['d'] || keys['arrowright']) {
                if (Math.abs(speed) > 0.05) carAngle -= turnSpeed * (speed > 0 ? 1 : -1);
            }

            // Update 3D positional matrix coordinates
            carGroup.rotation.y = carAngle;
            carGroup.position.x -= Math.sin(carAngle) * speed;
            carGroup.position.z -= Math.cos(carAngle) * speed;

            // Simple map boundary bounding loops
            if (Math.abs(carGroup.position.x) > worldSize/2) carGroup.position.x *= -0.98;
            if (Math.abs(carGroup.position.z) > worldSize/2) carGroup.position.z *= -0.98;

            // Simple Ramp Trigger Elevation Logic
            if (Math.abs(carGroup.position.x) < 7 && carGroup.position.z < -25 && carGroup.position.z > -55) {
                // Calculate height profile based on ramp position slope
                const t = (carGroup.position.z + 55) / 30; // 0 to 1 scaling factor
                carGroup.position.y = (1 - t) * 7.5;
            } else {
                // Return safely back onto asphalt terrain layer floor
                carGroup.position.y = 0;
            }

            // --- 8. THIRD PERSON CAMERA FOLLOW ALGORITHM ---
            const relativeCameraOffset = new THREE.Vector3(0, 7, 18);
            const cameraOffset = relativeCameraOffset.applyMatrix4(carGroup.matrixWorld);
            
            camera.position.x = THREE.MathUtils.lerp(camera.position.x, cameraOffset.x, 0.1);
            camera.position.y = THREE.MathUtils.lerp(camera.position.y, cameraOffset.y, 0.1);
            camera.position.z = THREE.MathUtils.lerp(camera.position.z, cameraOffset.z, 0.1);
            camera.lookAt(new THREE.Vector3(carGroup.position.x, carGroup.position.y + 2, carGroup.position.z));

            // Dynamic Dashboard UI Speed conversion readouts
            speedoElement.innerText = "Speed: " + Math.round(Math.abs(speed) * 90) + " km/h";

            renderer.render(scene, camera);
        }

        // Handle Responsive scaling dynamically on windows resizing loops
        window.addEventListener('resize', () => {
            camera.aspect = container.clientWidth / container.clientHeight;
            camera.updateProjectionMatrix();
