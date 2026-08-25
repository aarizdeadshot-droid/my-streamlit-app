import streamlit as st

# Configure wide layout 
st.set_page_config(page_title="Python Geometry Dash", page_icon="🔺", layout="centered")

st.title("🔺 Geometry Dash Sandbox")
st.write("Click anywhere inside the game area or press **SPACEBAR / UP ARROW** to jump over spikes!")

# Embedded HTML5/Javascript High-Speed Platformer Engine
game_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background-color: #ffffff; font-family: sans-serif; text-align: center; overflow: hidden; }
        #canvas-container { position: relative; display: inline-block; margin-top: 10px; }
        canvas { background: linear-gradient(180deg, #001f3f, #0074D9); border: 4px solid #333; border-radius: 8px; }
        #ui-layer { position: absolute; top: 15px; left: 0; right: 0; display: flex; justify-content: space-between; padding: 0 20px; font-family: 'Courier New', Courier, monospace; pointer-events: none; }
        .hud-text { color: #ffffff; font-size: 18px; font-weight: bold; background: rgba(0,0,0,0.5); padding: 5px 12px; border-radius: 4px; text-shadow: 1px 1px 2px #000; }
    </style>
</head>
<body>

    <div id="canvas-container">
        <div id="ui-layer">
            <div id="progress-bar" class="hud-text">PROGRESS: 0%</div>
            <div id="attempt-counter" class="hud-text">ATTEMPT: 1</div>
        </div>
        <canvas id="gameCanvas" width="800" height="400"></canvas>
    </div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        const progressElement = document.getElementById("progress-bar");
        const attemptElement = document.getElementById("attempt-counter");

        // --- GAME PARAMETERS ---
        const GROUND_Y = 320;
        let attempt = 1;
        let gameOver = false;
        let totalDistance = 10000; // Total length of the level track
        let distanceTraveled = 0;

        // Player properties (The Cube)
        const player = {
            x: 150,
            y: GROUND_Y - 30,
            size: 30,
            vy: 0,
            gravity: 1.2,
            jumpForce: -16,
            isGrounded: true,
            rotation: 0
        };

        // Obstacles data array (Spikes)
        let obstacles = [];
        
        // Populate level with procedural spike distribution mapping
        function initLevel() {
            obstacles = [];
            distanceTraveled = 0;
            gameOver = false;
            
            // Spawn spikes progressively across the custom horizontal matrix
            let nextSpawnX = 600;
            while (nextSpawnX < totalDistance) {
                // Randomize spacing intervals between obstacles
                nextSpawnX += Math.floor(Math.random() * 300) + 350;
                
                // Randomly decide if it's a single spike (1) or double spike (2)
                let type = Math.random() > 0.7 ? 2 : 1;
                obstacles.push({ x: nextSpawnX, type: type, width: 30, height: 30 });
            }
        }

        // --- HANDLE INPUT EVENTS ---
        function triggerJump() {
            if (player.isGrounded && !gameOver) {
                player.vy = player.jumpForce;
                player.isGrounded = false;
            }
            if (gameOver) {
                attempt++;
                attemptElement.innerText = "ATTEMPT: " + attempt;
                initLevel();
                player.y = GROUND_Y - player.size;
                player.vy = 0;
                player.rotation = 0;
                player.isGrounded = true;
            }
        }

        // Listeners for keyboard controls
        window.addEventListener("keydown", (e) => {
            if (e.key === " " || e.key === "ArrowUp") {
                e.preventDefault(); // Stop webpage from shifting down
                triggerJump();
            }
        });

        // Click or tap directly inside the map area
        canvas.addEventListener("mousedown", (e) => {
            triggerJump();
        });

        // Initialize Level Sequence
        initLevel();

        // --- MAIN GEOMETRY ENGINE TIMESTEP LOOP ---
        function gameLoop() {
            // 1. Clear Screen Canvas Frame
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // 2. Draw Scrolling Background Matrix Grid Pattern
            ctx.strokeStyle = "rgba(255,255,255,0.07)";
            ctx.lineWidth = 2;
            let gridOffset = distanceTraveled % 40;
            for (let x = -gridOffset; x < canvas.width; x += 40) {
                ctx.beginPath();
                ctx.moveTo(x, 0);
                ctx.lineTo(x, GROUND_Y);
                ctx.stroke();
            }

            // 3. Draw Ground Line As Asphault Layout Barrier
            ctx.fillStyle = "#000000";
            ctx.fillRect(0, GROUND_Y, canvas.width, canvas.height - GROUND_Y);
            ctx.fillStyle = "#00ffcc";
            ctx.fillRect(0, GROUND_Y, canvas.width, 4); // Glowing green neon baseline border

            if (!gameOver) {
                // 4. Update Game Speeds and Track Advancements
                let gameSpeed = 7.5; 
                distanceTraveled += gameSpeed;

                // Update Level Progression Readout HUD percentage updates
                let progressPercent = Math.min(100, Math.floor((distanceTraveled / totalDistance) * 100));
                progressElement.innerText = "PROGRESS: " + progressPercent + "%";

                if (progressPercent >= 100) {
                    gameOver = true; // Win condition parameters matching track layout endpoints
                }

                // 5. Update Player Vertical Velocity Physics Mechanics 
                player.vy += player.gravity;
                player.y += player.vy;

                // Ground Collision bounds checking
                if (player.y >= GROUND_Y - player.size) {
                    player.y = GROUND_Y - player.size;
                    player.vy = 0;
                    player.isGrounded = true;
                    
                    // Snap rotation alignment flush onto ground when landed safely
                    player.rotation = Math.round(player.rotation / (Math.PI / 2)) * (Math.PI / 2);
                } else {
                    // Continuously spin character cube asset clockwise mid-air during jump frames
                    player.rotation += 0.08;
                }

                // 6. Move & Draw Spikes + Handle Precise Collision Checks
                ctx.fillStyle = "#FF4136"; // Neon Red sharp spike hazards color
                ctx.strokeStyle = "#FFFFFF";
                ctx.lineWidth = 1.5;

                obstacles.forEach(spike => {
                    // Update relative canvas positions based on horizontal scrolling offsets
                    let screenX = spike.x - distanceTraveled + player.x;

                    // Only draw visible objects sitting inside standard resolution screens bounds
                    if (screenX > -100 && screenX < canvas.width + 100) {
                        for (let count = 0; count < spike.type; count++) {
                            let currentSpikeX = screenX + (count * 28);
                            
                            // Vector geometry drawing commands for drawing sharp triangles
                            ctx.beginPath();
                            ctx.moveTo(currentSpikeX, GROUND_Y);
                            ctx.lineTo(currentSpikeX + spike.width / 2, GROUND_Y - spike.height);
                            ctx.lineTo(currentSpikeX + spike.width, GROUND_Y);
                            ctx.closePath();
                            ctx.fill();
                            ctx.stroke();

                            // Triangle-to-Box bounding overlap checks
                            let boxLeft = player.x;
                            let boxRight = player.x + player.size;
                            let boxTop = player.y;
                            let boxBottom = player.y + player.size;

                            let spikeLeft = currentSpikeX + 4; // Padding cushion to ensure fair hitboxes
                            let spikeRight = currentSpikeX + spike.width - 4;
                            let spikeTop = GROUND_Y - spike.height + 4;

                            if (boxRight > spikeLeft && boxLeft < spikeRight && boxBottom > spikeTop) {
                                gameOver = true; // Crash detected!
                            }
                        }
                    }
                });

                // 7. Render Character Icon (The Cube Matrix Object Canvas Transformations)
                ctx.save();
                ctx.translate(player.x + player.size / 2, player.y + player.size / 2);
                ctx.rotate(player.rotation);

                // Draw Neon Outer Box face mapping profile shell
                ctx.fillStyle = "#FFDC00"; // Signature bright yellow look
                ctx.fillRect(-player.size / 2, -player.size / 2, player.size, player.size);
                
                // Draw inner detailing structural squares inside the cube face
                ctx.strokeStyle = "#001f3f";
                ctx.lineWidth = 3;
                ctx.strokeRect(-player.size / 2 + 4, -player.size / 2 + 4, player.size - 8, player.size - 8);
                
                // Tiny decorative square eyes inside face vectors
                ctx.fillStyle = "#001f3f";
                ctx.fillRect(-8, -8, 5, 5);
                ctx.fillRect(3, -8, 5, 5);
                
                ctx.restore();

            } else {
                // --- GAME OVER OR WIN DISPLAY SCREENS OVERLAYS ---
                ctx.fillStyle = "rgba(0,0,0,0.75)";
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.font = "bold 36px sans-serif";
                ctx.textAlign = "center";

