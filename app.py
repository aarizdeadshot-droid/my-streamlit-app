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
        body { margin: 0; background-color: #001233; text-align: center; overflow: hidden; user-select: none; font-family: 'Arial', sans-serif; }
        #canvas-container { position: relative; display: inline-block; margin-top: 10px; }
        canvas { 
            background: linear-gradient(180deg, #002447 0%, #00519e 70%, #002b54 100%); 
            border: 4px solid #00ffcc; 
            box-shadow: 0px 0px 20px #00ffcc;
            border-radius: 4px; 
        }
        #ui-layer { position: absolute; top: 15px; left: 0; right: 0; display: flex; justify-content: space-between; padding: 0 30px; pointer-events: none; }
        .hud-text { color: #ffffff; font-size: 20px; font-weight: bold; font-family: 'Impact', Charcoal, sans-serif; letter-spacing: 2px; text-shadow: 2px 2px 0px #000; }
        
        .overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 10, 30, 0.85); display: flex; flex-direction: column; align-items: center; justify-content: center; z-index: 10; }
        .menu-title { font-family: 'Impact', sans-serif; font-size: 48px; color: #00ffcc; letter-spacing: 3px; text-shadow: 3px 3px 0px #000; margin-bottom: 20px; }
        .menu-btn { background: #ffaa00; border: 3px solid #fff; border-radius: 8px; color: #fff; font-family: 'Impact', sans-serif; font-size: 28px; padding: 10px 40px; cursor: pointer; text-shadow: 2px 2px 0px #000; box-shadow: 0px 5px 0px #b37700; transition: 0.1s; margin-bottom: 25px; }
        .menu-btn:active { transform: translateY(5px); box-shadow: 0px 0px 0px #b37700; }
        
        .char-selector { display: flex; gap: 20px; background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px; border: 2px solid #00ffcc; }
        .char-option { width: 50px; height: 50px; border: 3px solid #fff; cursor: pointer; display: flex; align-items: center; justify-content: center; border-radius: 6px; font-weight: bold; font-size: 14px; color: white; text-shadow: 1px 1px 1px #000; }
        .char-option.selected { border-color: #00ffcc; box-shadow: 0px 0px 15px #00ffcc; transform: scale(1.1); }
        
        #win-msg, #crash-msg { display: none; position: absolute; width: 100%; top: 40%; text-align: center; font-family: 'Impact', sans-serif; font-size: 50px; letter-spacing: 3px; text-shadow: 3px 3px 0px #000; pointer-events: none; z-index: 5; }
        #win-msg { color: #00ff00; }
        #crash-msg { color: #ff3333; }
    </style>
</head>
<body>

    <div id="canvas-container">
        <div id="main-menu" class="overlay">
            <div class="menu-title">GEOMETRY DASH</div>
            <button class="menu-btn" id="playBtn">PLAY</button>
            <div style="color: #fff; font-family: 'Impact', sans-serif; margin-bottom: 10px; letter-spacing: 1px;">SELECT SKIN:</div>
            <div class="char-selector">
                <div id="skin-0" class="char-option selected" style="background: #ffcc00;">CUBE</div>
                <div id="skin-1" class="char-option" style="background: #ff3366;">NEON</div>
                <div id="skin-2" class="char-option" style="background: #33ccff;">ROBOT</div>
            </div>
        </div>

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
        const mainMenu = document.getElementById("main-menu");
        const playBtn = document.getElementById("playBtn");

        const GROUND_Y = 320;
        let attempt = 1;
        let gameOver = false;
        let hasWon = false;
        let inMenu = true;
        let totalDistance = 14000; 
        let distanceTraveled = 0;
        let gameSpeed = 8.5; 

        let isHoldingJump = false;

        const player = {
            x: 180,
            y: GROUND_Y - 32,
            size: 32,
            vy: 0,
            gravity: 1.4, 
            jumpForce: -16.5,
            isGrounded: true,
            rotation: 0,
            form: 'cube' 
        };

        let obstacles = [];
        let portals = [];

        function selectSkin(index) {
            selectedSkin = index;
            document.querySelectorAll('.char-option').forEach((opt, i) => {
                if(i === index) opt.classList.add('selected');
                else opt.classList.remove('selected');
            });
        }

        document.getElementById("skin-0").addEventListener("click", () => selectSkin(0));
        document.getElementById("skin-1").addEventListener("click", () => selectSkin(1));
        document.getElementById("skin-2").addEventListener("click", () => selectSkin(2));

        function startGame() {
            inMenu = false;
            mainMenu.style.display = "none";
            attempt = 1;
            attemptElement.innerText = "ATTEMPT " + attempt;
            initLevel();
        }
        
        playBtn.addEventListener("click", startGame);
        
        function initLevel() {
            obstacles = [];
            portals = [];
            fireworks = [];
            distanceTraveled = 0;
            gameOver = false;
            hasWon = false;
            winMsg.style.display = "none";
            crashMsg.style.display = "none";
            player.y = GROUND_Y - player.size;
            player.vy = 0;
            player.rotation = 0;
            player.isGrounded = true;
            player.form = 'cube';
            player.gravity = 1.4;
            
            portals.push({ x: 4500, type: 'ship', checked: false });
            portals.push({ x: 9500, type: 'cube', checked: false });

            let nextSpawnX = 700;
            while (nextSpawnX < totalDistance - 800) {
                if (Math.abs(nextSpawnX - 4500) < 200 || Math.abs(nextSpawnX - 9500) < 200) {
                    nextSpawnX += 300;
                    continue;
                }

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
                if (gameOver) restartGame();
            }
        });

        window.addEventListener("keyup", (e) => {
            if (e.key === " " || e.code === "Space" || e.key === "ArrowUp") {
                isHoldingJump = false;
            }
        });

        canvas.addEventListener("mousedown", (e) => {
            isHoldingJump = true;
            if (gameOver) restartGame();
        });

        window.addEventListener("mouseup", () => {
            isHoldingJump = false;
        });

        function restartGame() {
            attempt++;
            attemptElement.innerText = "ATTEMPT " + attempt;
            initLevel();
        }

        function createFirework() {
            let x = Math.random() * canvas.width;
            let y = Math.random() * (canvas.height - 150);
            let colors = ["#00ffcc", "#ffaa00", "#ff0055", "#00ff00", "#ffff00", "#ff00ff"];
            let color = colors[Math.floor(Math.random() * colors.length)];
            for (let i = 0; i < 30; i++) {
                let angle = Math.random() * Math.PI * 2;
                let speed = Math.random() * 4 + 2;
                fireworks.push({
                    x: x, y: y,
                    vx: Math.cos(angle) * speed,
                    vy: Math.sin(angle) * speed,
                    color: color,
                    alpha: 1,
                    life: Math.random() * 30 + 30
                });
            }
        }

        function gameLoop() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            ctx.strokeStyle = "rgba(0, 255, 204, 0.08)";
            ctx.lineWidth = 2;
            let gridOffset = distanceTraveled % 45;
            for (let x = -gridOffset; x < canvas.width; x += 45) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, GROUND_Y); ctx.stroke();
            }

            ctx.fillStyle = "#000814";
            ctx.fillRect(0, GROUND_Y, canvas.width, canvas.height - GROUND_Y);
            ctx.fillStyle = "#00ffcc";
            ctx.fillRect(0, GROUND_Y, canvas.width, 5); 

            if (!inMenu) {
                if (!gameOver && !hasWon) {
