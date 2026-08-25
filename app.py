import streamlit as st

# Configure wide layout 
st.set_page_config(page_title="400 FPS Python Game", page_icon="⚡", layout="wide")

st.title("⚡ Ultra-Performance 2D Space Evader")
st.write("Built with a high-speed rendering loop to maximize framerate performance.")

# Embedded HTML5 High-FPS Game Module
game_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background-color: #ffffff; font-family: sans-serif; text-align: center; }
        #canvas-container { position: relative; display: inline-block; margin-top: 10px; }
        canvas { background: #111116; border: 4px solid #222; border-radius: 8px; cursor: none; }
        #fps-counter { position: absolute; top: 10px; left: 10px; color: #00ffcc; font-family: monospace; font-size: 16px; font-weight: bold; background: rgba(0,0,0,0.6); padding: 5px 10px; border-radius: 4px; }
        #score-board { position: absolute; top: 10px; right: 10px; color: #ffffff; font-family: monospace; font-size: 16px; font-weight: bold; background: rgba(0,0,0,0.6); padding: 5px 10px; border-radius: 4px; }
    </style>
</head>
<body>

    <div id="canvas-container">
        <div id="fps-counter">FPS: 0</div>
        <div id="score-board">SCORE: 0</div>
        <canvas id="gameCanvas" width="800" height="450"></canvas>
    </div>

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        const fpsCounter = document.getElementById("fps-counter");
        const scoreBoard = document.getElementById("score-board");

        // --- GAME VARIABLES ---
        let score = 0;
        let gameOver = false;
        
        // Player setup (Spaceship)
        const player = { x: 100, y: 225, radius: 15, speed: 6, targetY: 225 };
        
        // Obstacles array (Asteroids)
        const obstacles = [];
        const maxObstacles = 8;
        
        // Stars background system for depth
        const stars = [];
        for(let i=0; i<40; i++) {
            stars.push({ x: Math.random() * canvas.width, y: Math.random() * canvas.height, size: Math.random() * 2, speed: Math.random() * 2 + 1 });
        }

        // --- FPS CALCULATION VECTOR ---
        let lastCalledTime;
        let fpsPool = [];

        // Track Mouse Input Movement
        canvas.addEventListener("mousemove", (e) => {
            const rect = canvas.getBoundingClientRect();
            player.targetY = e.clientY - rect.top;
        });

        // Initialize/Reset obstacles
        function spawnObstacle(obj = {}) {
            obj.x = canvas.width + Math.random() * 300;
            obj.y = Math.random() * (canvas.height - 40) + 20;
            obj.radius = Math.random() * 15 + 10;
            obj.speed = Math.random() * 4 + 4 + (score * 0.05); // Speed increases with score
            return obj;
        }

        for(let i=0; i<maxObstacles; i++) {
            obstacles.push(spawnObstacle({}));
        }

        // --- MAIN ENGINE ENGINE LOOP ---
        function engineLoop() {
            // 1. Calculate Frame Rate Delta
            if(!lastCalledTime) {
                lastCalledTime = performance.now();
            } else {
                let delta = (performance.now() - lastCalledTime)/1000;
                lastCalledTime = performance.now();
                let currentFps = Math.round(1/delta);
                
                // Average the FPS across 10 frames to avoid sudden jumping metrics
                fpsPool.push(currentFps);
                if(fpsPool.length > 10) fpsPool.shift();
                let avgFps = Math.round(fpsPool.reduce((a,b) => a+b) / fpsPool.length);
                fpsCounter.innerText = "FPS: " + avgFps;
            }

            // 2. Clear Screen Context
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // 3. Draw Background Space Stars
            ctx.fillStyle = "#ffffff";
            stars.forEach(star => {
                ctx.beginPath();
                ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
                ctx.fill();
                if(!gameOver) {
                    star.x -= star.speed;
                    if(star.x < 0) star.x = canvas.width;
                }
            });

            if (!gameOver) {
                // 4. Update Player Physics Position
                let dy = player.targetY - player.y;
                player.y += dy * 0.15; // Smooth interpolation movement lag

                // 5. Draw Player Vector (Neon Jet)
                ctx.fillStyle = "#00ffcc";
                ctx.shadowBlur = 10;
                ctx.shadowColor = "#00ffcc";
                ctx.beginPath();
                ctx.moveTo(player.x + 20, player.y);
                ctx.lineTo(player.x - 15, player.y - 12);
                ctx.lineTo(player.x - 15, player.y + 12);
                ctx.closePath();
                ctx.fill();
                ctx.shadowBlur = 0; // Reset shadow blur immediately

                // 6. Move and Draw Obstacles (Asteroids)
                ctx.fillStyle = "#ff3366";
                obstacles.forEach(obs => {
                    obs.x -= obs.speed;

                    // Draw Asteroid
                    ctx.beginPath();
                    ctx.arc(obs.x, obs.y, obs.radius, 0, Math.PI * 2);
                    ctx.fill();

                    // Collision Detection (Circle Overlap Formula)
                    let distDX = player.x - obs.x;
                    let distDY = player.y - obs.y;
                    let totalDistance = Math.sqrt(distDX * distDX + distDY * distDY);

                    if (totalDistance < player.radius + obs.radius) {
                        gameOver = true;
                    }

                    // Recycle out of bounds obstacles
                    if (obs.x + obs.radius < 0) {
                        spawnObstacle(obs);
                        score += 10;
                        scoreBoard.innerText = "SCORE: " + score;
                    }
                });
            } else {
                // Game Over Screen Draw
                ctx.fillStyle = "rgba(0,0,0,0.8)";
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                ctx.fillStyle = "#ff3366";
                ctx.font = "bold 40px sans-serif";
                ctx.fillText("GAME OVER", canvas.width/2 - 120, canvas.height/2 - 10);
                
                ctx.fillStyle = "#ffffff";
                ctx.font = "20px sans-serif";
                ctx.fillText("Final Score: " + score, canvas.width/2 - 60, canvas.height/2 + 30);
                ctx.fillText("Click anywhere inside map to restart", canvas.width/2 - 160, canvas.height/2 + 70);
            }

            // Request next hardware frame step instantly
            requestAnimationFrame(engineLoop);
        }

        // Restart listener trigger click
        window.addEventListener("click", () => {
            if(gameOver) {
                score = 0;
                scoreBoard.innerText = "SCORE: " + score;
                gameOver = false;
                obstacles.forEach(obs => spawnObstacle(obs));
                player.y = 225;
            }
        });

        // Launch Game Loop Engine
        engineLoop();
    </script>
</body>
</html>
"""

# Render HTML game block in Streamlit canvas
st.components.v1.html(game_html, height=480, scrolling=False)

st.info("💡 **Performance Note:** Make sure your monitor's hardware refresh rate (Hz) and browser settings permit unthrottled frames to watch the counter skyrocket!")
