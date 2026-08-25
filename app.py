import streamlit as st

st.set_page_config(page_title="Python Geometry Dash", page_icon="🔺", layout="centered")

st.title("🔺 Geometry Dash Sandbox")
st.write("Press **SPACEBAR** or click inside the game window area to jump over spikes!")

game_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; background-color: #ffffff; text-align: center; overflow: hidden; }
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

        const GROUND_Y = 320;
        let attempt = 1;
        let gameOver = false;
        let totalDistance = 10000; 
        let distanceTraveled = 0;

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

        let obstacles = [];
        
        function initLevel() {
            obstacles = [];
            distanceTraveled = 0;
            gameOver = false;
            
            let nextSpawnX = 600;
            while (nextSpawnX < totalDistance) {
                nextSpawnX += Math.floor(Math.random() * 300) + 350;
                let type = Math.random() > 0.7 ? 2 : 1;
                obstacles.push({ x: nextSpawnX, type: type, width: 30, height: 30 });
            }
        }

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

        window.addEventListener("keydown", (e) => {
            if (e.key === " " || e.code === "Space") {
                e.preventDefault(); 
                triggerJump();
            }
        });

        canvas.addEventListener("mousedown", (e) => {
            triggerJump();
        });

        initLevel();

        function gameLoop() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            ctx.strokeStyle = "rgba(255,255,255,0.07)";
            ctx.lineWidth = 2;
            let gridOffset = distanceTraveled % 40;
            for (let x = -gridOffset; x < canvas.width; x += 40) {
                ctx.beginPath();
                ctx.moveTo(x, 0);
                ctx.lineTo(x, GROUND_Y);
                ctx.stroke();
            }

            ctx.fillStyle = "#000000";
            ctx.fillRect(0, GROUND_Y, canvas.width, canvas.height - GROUND_Y);
            ctx.fillStyle = "#00ffcc";
            ctx.fillRect(0, GROUND_Y, canvas.width, 4); 

            if (!gameOver) {
                let gameSpeed = 7.5; 
                distanceTraveled += gameSpeed;

                let progressPercent = Math.min(100, Math.floor((distanceTraveled / totalDistance) * 100));
                progressElement.innerText = "PROGRESS: " + progressPercent + "%";

                if (progressPercent >= 100) {
                    gameOver = true; 
                }

                player.vy += player.gravity;
                player.y += player.vy;

                if (player.y >= GROUND_Y - player.size) {
                    player.y = GROUND_Y - player.size;
                    player.vy = 0;
                    player.isGrounded = true;
                    player.rotation = Math.round(player.rotation / (Math.PI / 2)) * (Math.PI / 2);
                } else {
                    player.rotation += 0.08;
                }

                ctx.fillStyle = "#FF4136"; 
                ctx.strokeStyle = "#FFFFFF";
                ctx.lineWidth = 1.5;

                obstacles.forEach(spike => {
                    let screenX = spike.x - distanceTraveled + player.x;

                    if (screenX > -100 && screenX < canvas.width + 100) {
                        for (let count = 0; count < spike.type; count++) {
                            let currentSpikeX = screenX + (count * 28);
                            
                            ctx.beginPath();
                            ctx.moveTo(currentSpikeX, GROUND_Y);
                            ctx.lineTo(currentSpikeX + spike.width / 2, GROUND_Y - spike.height);
                            ctx.lineTo(currentSpikeX + spike.width, GROUND_Y);
                            ctx.closePath();
                            ctx.fill();
                            ctx.stroke();

                            let boxLeft = player.x;
                            let boxRight = player.x + player.size;
                            let boxTop = player.y;
                            let boxBottom = player.y + player.size;

                            let spikeLeft = currentSpikeX + 4; 
                            let spikeRight = currentSpikeX + spike.width - 4;
                            let spikeTop = GROUND_Y - spike.height + 4;

                            if (boxRight > spikeLeft && boxLeft < spikeRight && boxBottom > spikeTop) {
                                gameOver = true; 
                            }
                        }
                    }
                });

                ctx.save();
                ctx.translate(player.x + player.size / 2, player.y + player.size / 2);
                ctx.rotate(player.rotation);

                ctx.fillStyle = "#FFDC00"; 
                ctx.fillRect(-player.size / 2, -player.size / 2, player.size, player.size);
                
                ctx.strokeStyle = "#001f3f";
                ctx.lineWidth = 3;
                ctx.strokeRect(-player.size / 2 + 4, -player.size / 2 + 4, player.size - 8, player.size - 8);
                
                ctx.fillStyle = "#001f3f";
                ctx.fillRect(-8, -8, 5, 5);
                ctx.fillRect(3, -8, 5, 5);
                
                ctx.restore();

            } else {
                ctx.fillStyle = "rgba(0,0,0,0.75)";
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.font = "bold 36px sans-serif";
                ctx.textAlign = "center";

                if (distanceTraveled >= totalDistance) {
                    ctx.fillStyle = "#2ECC40"; 
                    ctx.fillText("🏆 LEVEL COMPLETED!", canvas.width / 2, canvas.height / 2 - 20);
                    ctx.font = "18px sans-serif";
                    ctx.fillStyle = "#ffffff";
                    ctx.fillText("You mastered the rhythm! Click to play again.", canvas.width / 2, canvas.height / 2 + 25);
                } else {
                    ctx.fillStyle = "#FF4136"; 
                    ctx.fillText("💥 CRASHED!", canvas.width / 2, canvas.height / 2 - 20);
                    ctx.font = "18px sans-serif";
                    ctx.fillStyle = "#ffffff";
                    ctx.fillText("Click inside or press SPACEBAR to instantly retry.", canvas.width / 2, canvas.height / 2 + 25);
                }
            }

            requestAnimationFrame(gameLoop);
        }

        gameLoop();
    </script>
</body>
</html>
"""

st.components.v1.html(game_html, height=430, scrolling=False)
