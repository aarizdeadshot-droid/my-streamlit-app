import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="The Aariz Developer | Student Hub",
    page_icon="✨",
    layout="centered"
)

# 2. Developer
st.title("The Aariz Developer ✨")
st.subheader("Interactive Student Profile & Bio Builder")
st.write("Fill out the details below to generate a beautiful, shareable digital student card.")

st.divider()

# 3. Step 1: Identity
st.header("👤 Step 1: Personal Details")
col_left, col_right = st.columns(2)

with col_left:
    full_name = st.text_input("Full Name", placeholder="e.g. Aariz Bin Azmat")
    age = st.number_input("Age", min_value=5, max_value=100, value=16, step=1)

with col_right:
    student_class = st.selectbox(
        "Current Class / Grade",
        ["Class 1-5", "Class 6-8", "Class 9-10 (Matric / O-Levels)", "Class 11-12 (Inter / A-Levels)", "University Student", "Graduated"]
    )
    roll_number = st.text_input("Roll Number / ID (Optional)", placeholder="e.g. SE-1024")

st.divider()

# 4. Step 2: Academic & Personal Interests
st.header("📚 Step 2: Academic & Hobbies")
col_left2, col_right2 = st.columns(2)

with col_left2:
    school_name = st.text_input("School / College / University Name", placeholder="e.g. Army Public School / Beaconhouse")
    fav_subject = st.text_input("Favorite Subject", placeholder="e.g. Computer Science, Mathematics")

with col_right2:
    hobbies = st.multiselect(
        "Select Your Hobbies",
        ["Coding 💻", "Gaming 🎮", "Cricket 🏏", "Football ⚽", "Reading 📚", "Photography 📷", "Music 🎵", "Art🎨"],
        default=["Coding 💻"]
    )
    bio = st.text_area("Short Bio (Tell us about yourself)", placeholder="I am passionate about technology and software development...", max_chars=150)

st.divider()

# 5. Step 3: Contact & Social Info
st.header("🌐 Step 3: Contact & Links")
col_left3, col_right3 = st.columns(2)

with col_left3:
    email = st.text_input("Email Address", placeholder="yourname@example.com")
with col_right3:
    github_link = st.text_input("GitHub Profile Link (Optional)", placeholder="https://github.com")

st.divider()

# 6. Profile Card Generation
st.header("🪪 Generated Digital Profile Card")

if st.button("🔥 Create My Profile Card", use_container_width=True):
    if not full_name:
        st.error("❌ Please enter your **Full Name** in Step 1 to generate your card.")
    elif not school_name:
        st.error("❌ Please enter your **School/College Name** in Step 2 to generate your card.")
    else:
        # Success celebration
        st.balloons()
        st.success("🎉 Your digital card is ready!")
        
        # Profile Card Box UI
        with st.container(border=True):
            st.markdown(f"## 🪪 {full_name.upper()}")
            st.markdown(f"**🏫 Institution:** {school_name}")
            
            # Sub-layout inside the card
            c1, c2, c3 = st.columns(3)
            with c1:
                st.metric(label="Class", value=student_class)
            with c2:
                st.metric(label="Age", value=f"{age} Y/O")
            with c3:
                st.metric(label="Roll No.", value=roll_number if roll_number else "N/A")
            
            st.markdown("---")
            st.markdown(f"📖 **Favorite Subject:** {fav_subject if fav_subject else 'Not specified'}")
            
            # Formatting the hobbies list
            if hobbies:
                hobby_tags = " | ".join(hobbies)
                st.markdown(f"❤️ **Interests:** {hobby_tags}")
            
            if bio:
                st.markdown(f"📝 **Bio:** *\"{bio}\"*")
                
            st.markdown("---")
            st.markdown(f"✉️ **Contact:** {email if email else 'No email provided'}")
            if github_link:
                st.markdown(f"🔗 **GitHub:** [{github_link}]({github_link})")

# 7. Sidebar Information Terminal
with st.sidebar:
    st.title("⚙️ System Control")
    st.write("This application dynamically builds custom profile cards using raw input data variables.")
    
    st.info("💡 **Aariz Developer Tip:** Click the arrow icon in the top left corner on mobile devices to expand or collapse this menu panel.")
    
    # Progress bar just for visual aesthetics
    st.write("System Status:")
    st.progress(100, text="All modules operational")
    import streamlit as st
import streamlit.components.v1 as components

# 1. Page Configuration
st.set_page_config(page_title="Neon Wave Simulator", page_icon="📐", layout="centered")
st.title("📐 Neon Wave Simulator")
st.write("Hold **SPACEBAR** or **HOLD CLICK** inside the box to fly up diagonally. **RELEASE** to fall down diagonally!")

# 2. Geometry Dash Style Zig-Zag Engine Component
game_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            background-color: #0b0c10;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            font-family: 'Courier New', Courier, monospace;
        }
        canvas {
            border: 3px solid #1f2833;
            background-color: #1f1135; /* Dark purple backdrop match */
            box-shadow: 0 0 25px rgba(102, 252, 241, 0.15);
            border-radius: 6px;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <canvas id="waveCanvas" width="600" height="400"></canvas>

<script>
    const canvas = document.getElementById("waveCanvas");
    const ctx = canvas.getContext("2d");

    // Game Variables
    let isPressing = false;
    let gameOver = false;
    let score = 0;
    let frameCount = 0;

    // Player Wave Vehicle Settings
    let player = {
        x: 100,
        y: 200,
        size: 10,
        speedY: 3.5, // Strict diagonal velocity factor
        trail: []    # Stores historical points for the neon path line
    };

    // Obstacle Spikes Track Array
    let obstacles = [];

    // Key Event Input Managers
    window.addEventListener("keydown", function(e) {
        if (e.code === "Space") {
            e.preventDefault();
            if (gameOver) { resetGame(); } else { isPressing = true; }
        }
    });

    window.addEventListener("keyup", function(e) {
        if (e.code === "Space") { isPressing = false; }
    });

    // Touch/Mouse Input Managers
    canvas.addEventListener("mousedown", (e) => {
        if (gameOver) { resetGame(); } else { isPressing = true; }
    });
    window.addEventListener("mouseup", () => { isPressing = false; });
    
    canvas.addEventListener("touchstart", (e) => { e.preventDefault(); if (gameOver) { resetGame(); } else { isPressing = true; } });
    window.addEventListener("touchend", () => { isPressing = false; });

    function resetGame() {
        player.y = 200;
        player.trail = [];
        obstacles = [];
        score = 0;
        gameOver = false;
        frameCount = 0;
        isPressing = false;
    }

    function spawnSpikeWall() {
        let size = Math.floor(Math.random() * 60) + 40;
        let isCeiling = Math.random() > 0.5;

        obstacles.push({
            x: canvas.width,
            size: size,
            isCeiling: isCeiling,
            passed: false
        });
    }

    // Engine Core Step Update
    function update() {
        frameCount++;

        if (!gameOver) {
            // GD Movement: Sharp Up or Down adjustment instantly
            if (isPressing) {
                player.y -= player.speedY;
            } else {
                player.y += player.speedY;
            }

            // Save point position memory for trail tracking line
            player.trail.push({x: player.x, y: player.y});
            if (player.trail.length > 80) {
                player.trail.shift();
            }

            // Boundary Hit check (Floor & Ceiling Hazard Lines)
            if (player.y < 15 || player.y > canvas.height - 15) {
                gameOver = true;
            }

            // Generation timing sequence
            if (frameCount % 70 === 0) {
                spawnSpikeWall();
            }

            // Obstacle Movement calculations
            for (let i = obstacles.length - 1; i >= 0; i--) {
                obstacles[i].x -= 4; // Constant horizontal scrolling rate

                // Precise Triangle Intersection Collision Calculations
                let obs = obstacles[i];
                if (player.x > obs.x && player.x < obs.x + obs.size) {
                    if (obs.isCeiling && player.y < obs.size) {
                        gameOver = true;
                    }
                    if (!obs.isCeiling && player.y > canvas.height - obs.size) {
                        gameOver = true;
                    }
                }

                // Increment score counter safely
                if (!obs.passed && obs.x + obs.size < player.x) {
                    score++;
                    obs.passed = true;
                }

                // Memory cleanup
                if (obs.x + obs.size < 0) {
                    obstacles.splice(i, 1);
                }
            }
        }

        draw();
        requestAnimationFrame(update);
    }

    // Rendering Painting Methods
    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Draw Dangerous Spike Boarders (Ceiling/Floor Lines)
        ctx.fillStyle = "#4b134f";
        ctx.fillRect(0, 0, canvas.width, 15);
        ctx.fillRect(0, canvas.height - 15, canvas.width, 15);

        // Draw Player Neon ZigZag Trail Line
        if (player.trail.length > 1) {
            ctx.beginPath();
            ctx.moveTo(player.trail[0].x, player.trail[0].y);
            
            // Adjust trails visually relative to scroll speed simulation mapping
            let scrollOffset = 4; 
            for (let i = 1; i < player.trail.length; i++) {
                let segment = player.trail[i];
                // Shift trail left progressively to make it look anchored to space
                let adjustedX = player.x - (player.trail.length - i) * scrollOffset;
                ctx.lineTo(adjustedX, segment.y);
            }
            
            ctx.strokeStyle = "#fffb00"; /* High glow yellow trail line */
            ctx.lineWidth = 4;
            ctx.shadowBlur = 15;
            ctx.shadowColor = "#fffb00";
            ctx.stroke();
            ctx.shadowBlur = 0; // Turn off glow effects for standard shapes
        }

        // Draw Triangle Spikes
        for (let obs of obstacles) {
            ctx.fillStyle = "#c3073f";
            ctx.strokeStyle = "#950714";
            ctx.lineWidth = 2;
            ctx.beginPath();

            if (obs.isCeiling) {
                ctx.moveTo(obs.x, 0);
                ctx.lineTo(obs.x + obs.size, 0);
                ctx.lineTo(obs.x + (obs.size / 2), obs.size);
            } else {
                ctx.moveTo(obs.x, canvas.height);
                ctx.lineTo(obs.x + obs.size, canvas.height);
                ctx.lineTo(obs.x + (obs.size / 2), canvas.height - obs.size);
            }
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
        }

        // Draw Player Cone/Dart Shape
        ctx.fillStyle = "#ffffff";
        ctx.strokeStyle = "#00f0ff";
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(player.x + 12, player.y);
        ctx.lineTo(player.x - 8, player.y - 8);
        ctx.lineTo(player.x - 4, player.y);
        ctx.lineTo(player.x - 8, player.y + 8);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Print Score Dashboard UI Elements
        ctx.fillStyle = "#ffffff";
        ctx.font = "900 22px 'Courier New'";
        ctx.fillText("ATTEMPT ATTEMPTS: " + score, 20, 45);

        // Render Game-over display screens
        if (gameOver) {
            ctx.fillStyle = "rgba(11, 12, 16, 0.85)";
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = "#ff4c4c";
            ctx.font = "900 36px 'Courier New'";
            ctx.textAlign = "center";
            ctx.fillText("CRASH DETECTED", canvas.width / 2, canvas.height / 2 - 25);

            ctx.fillStyle = "#ffffff";
            ctx.font = "16px 'Courier New'";
            ctx.fillText("Tap Screen or Press Spacebar to Retry", canvas.width / 2, canvas.height / 2 + 20);
            ctx.textAlign = "left";
        }
    }

    // Initialize Game Engine Runtime Loop
    update();
</script>
</body>
</html>
"""

# 3. Render Component inside Web UI Frame layout
components.html(game_html, height=430)

        st.session_state.shields = 100
        st.session_state.wave = 1
        st.session_state.laser_tier = 1
        st.session_state.drones = 0
