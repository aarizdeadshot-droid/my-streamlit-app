import streamlit as st

st.set_page_config(page_title="Geometry Dash Clone", page_icon="🔺", layout="centered")

st.markdown("""
    <style>
        .stApp {
            background-color: #001233 !important;
        }
        h1, p {
            color: #FFFFFF !important;
            font-family: 'Arial Black', Gadget, sans-serif;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔺 GEOMETRY DASH")

game_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background-color: #001233; text-align: center; overflow: hidden; user-select: none; }
        #canvas-container { position: relative; display: inline-block; margin-top: 10px; }
        canvas { 
            background: linear-gradient(180deg, #002447 0%, #00519e 70%, #002b54 100%); 
            border: 4px solid #00ffcc; 
            box-shadow: 0px 0px 20px #00ffcc;
            border-radius: 4px; 
        }
        #ui-layer { position: absolute; top: 15px; left: 0; right: 0; display: flex; justify-content: space-between; padding: 0 30px; font-family: 'Arial', sans-serif; pointer-events: none; }
        .hud-text { color: #ffffff; font-size: 20px; font-weight: bold; font-family: 'Impact', Charcoal, sans-serif; letter-spacing: 2px; text-shadow: 2px 2px 0px #000; }
        #win-msg, #crash-msg { display: none; position: absolute; width: 100%; top: 40%; text-align: center; font-family: 'Impact', sans-serif; font-size: 50px; letter-spacing: 3px; text-shadow: 3px 3px 0px #000; pointer-events: none; }
        #win-msg { color: #00ff00; }
        #crash-msg { color: #ff3333; }
    </style>
</head>
<body>

    <div id="canvas-container">
        <div id="ui-layer">
            <div id="progress-bar" class="hud-text">0%</div>
            <div id="attempt-counter" class="hud-text">ATTEMPT 1</div>
        </div>
        <div id="win-msg">LEVEL COMPLETE!</div>
        <div id="crash-msg">💥</div>
        <canvas id="gameCanvas" width="800" height="400"></canvas>
    </div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        const progressElement = document.getElementById("progress-bar");
        const attemptElement = document.getElementById("attempt-counter");
        const winMsg = document.getElementById("win-msg");
        const crashMsg = document.getElementById("crash-msg");

        const GROUND_Y = 320;
        let attempt = 1;
        let gameOver = false;
        let hasWon = false;
        let totalDistance = 12000; 
        let distanceTraveled = 0;
        let gameSpeed = 8.5; 

        let isHoldingJump = false;

        const player = {
            x: 180,
            y: GROUND_Y - 30,
            size: 32,
            vy: 0,
            gravity: 1.4, 
            jumpForce: -16.5,
            isGrounded: true,
            rotation: 0
        };

        let obstacles = [];
        
        function initLevel() {
            obstacles = [];
            distanceTraveled = 0;
            gameOver = false;
            hasWon = false;
            winMsg.style.display = "none";
            crashMsg.style.display = "none";
            player.y = GROUND_Y - player.size;
            player.vy = 0;
            player.rotation = 0;
            player.isGrounded = true;
            
            let nextSpawnX = 700;
            while (nextSpawnX < totalDistance - 800) {
                let randPattern = Math.random();
                if (randPattern < 0.4) {
                    obstacles.push({ x: nextSpawnX, type: 'single_spike', width: 30, height: 32 });
                    nextSpawnX += Math.floor(Math.random() * 250) + 380;
                } else if (randPattern < 0.7) {
                    obstacles.push({ x: nextSpawnX, type: 'double_spike', width: 58, height: 32 });
                    nextSpawnX += Math.floor(Math.random() * 300) + 450;
                } else {
                    obstacles.push({ x: nextSpawnX, type: 'block_jump', width: 40, height: 32 });
                    nextSpawnX += Math.floor(Math.random() * 200) + 400;
                }
            }
        }

        window.addEventListener("keydown", (e) => {
            if (e.key === " " || e.code === "Space" || e.key === "ArrowUp") {
                e.preventDefault(); 
                isHoldingJump = true;
                if (gameOver || hasWon) restartGame();
            }
        });

        window.addEventListener("keyup", (e) => {
            if (e.key === " " || e.code === "Space" || e.key === "ArrowUp") {
                isHoldingJump = false;
            }
        });

        canvas.addEventListener("mousedown", (e) => {
            isHoldingJump = true;
            if (gameOver || hasWon) restartGame();
        });

        window.addEventListener("mouseup", () => {
            isHoldingJump = false;
        });

        function restartGame() {
            attempt++;
            attemptElement.innerText = "ATTEMPT " + attempt;
            initLevel();
        }

        initLevel();

        function gameLoop() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            ctx.strokeStyle = "rgba(0, 255, 204, 0.08)";
            ctx.lineWidth = 2;
            let gridOffset = distanceTraveled % 45;
            for (let x = -gridOffset; x < canvas.width; x += 45) {
                ctx.beginPath();
                ctx.moveTo(x, 0);
                ctx.lineTo(x, GROUND_Y);
                ctx.stroke();
            }

            ctx.fillStyle = "#000814";
            ctx.fillRect(0, GROUND_Y, canvas.width, canvas.height - GROUND_Y);
            
            ctx.fillStyle = "#00ffcc";
            ctx.fillRect(0, GROUND_Y, canvas.width, 5); 
            ctx.shadowBlur = 15;
            ctx.shadowColor = "#00ffcc";
            ctx.fillRect(0, GROUND_Y, canvas.width, 2);
            ctx.shadowBlur = 0; 

            if (!gameOver && !hasWon) {
                distanceTraveled += gameSpeed;

                let progressPercent = Math.min(100, Math.floor((distanceTraveled / totalDistance) * 100));
                progressElement.innerText = progressPercent + "%";

                if (progressPercent >= 100) {
                    hasWon = true;
                    winMsg.style.display = "block";
                }

                if (isHoldingJump && player.isGrounded) {
                    player.vy = player.jumpForce;
                    player.isGrounded = false;
                }

                player.vy += player.gravity;
                player.y += player.vy;

                if (player.y >= GROUND_Y - player.size) {
                    player.y = GROUND_Y - player.size;
                    player.vy = 0;
                    player.isGrounded = true;
                    player.rotation = Math.round(player.rotation / (Math.PI / 2)) * (Math.PI / 2);
                } else {
                    player.rotation += 0.095;
                }

                obstacles.forEach(obs => {
                    let screenX = obs.x - distanceTraveled + player.x;

                    if (screenX > -150 && screenX < canvas.width + 150) {
                        ctx.lineWidth = 2;
                        
                        if (obs.type === 'single_spike') {
                            ctx.fillStyle = "#ff0055"; 
                            ctx.strokeStyle = "#ffffff";
                            ctx.beginPath();
                            ctx.moveTo(screenX, GROUND_Y);
                            ctx.lineTo(screenX + obs.width / 2, GROUND_Y - obs.height);
                            ctx.lineTo(screenX + obs.width, GROUND_Y);
                            ctx.closePath();
                            ctx.fill(); ctx.stroke();
                        } 
                        else if (obs.type === 'double_spike') {
                            ctx.fillStyle = "#ff0055"; 
                            ctx.strokeStyle = "#ffffff";
                            for(let s=0; s<2; s++) {
                                let sx = screenX + (s * 26);
                                ctx.beginPath();
                                ctx.moveTo(sx, GROUND_Y);
                                ctx.lineTo(sx + 15, GROUND_Y - obs.height);
                                ctx.lineTo(sx + 30, GROUND_Y);
                                ctx.closePath();
                                ctx.fill(); ctx.stroke();
                            }
                        } 
                        else if (obs.type === 'block_jump') {
                            ctx.fillStyle = "#2080ff";
                            ctx.strokeStyle = "#ffffff";
                            ctx.fillRect(screenX, GROUND_Y - obs.height, obs.width, obs.height);
                            ctx.strokeRect(screenX, GROUND_Y - obs.height, obs.width, obs.height);
                        }

                        let pLeft = player.x + 3;
                        let pRight = player.x + player.size - 3;
                        let pTop = player.y + 3;
                        let pBottom = player.y + player.size;

                        let oLeft = screenX + 4;
                        let oRight = screenX + obs.width - 4;
                        let oTop = GROUND_Y - obs.height;

                        if (pRight > oLeft && pLeft < oRight && pBottom > oTop) {
                            gameOver = true;
                            crashMsg.style.display = "block";
                        }
                    }
                });

                ctx.save();
                ctx.translate(player.x + player.size / 2, player.y + player.size / 2);
                ctx.rotate(player.rotation);

                ctx.fillStyle = "#ffcc00"; 
                ctx.fillRect(-player.size / 2, -player.size / 2, player.size, player.size);
                
                ctx.strokeStyle = "#000814";
                ctx.lineWidth = 3;
