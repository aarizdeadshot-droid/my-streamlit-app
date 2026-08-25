import streamlit as st

# 1. Setup App Layout
st.set_page_config(page_title="Streamlit Brick Breaker", page_icon="🎮", layout="centered")

st.title("🎮 Retro Brick Breaker")
st.write("A classic arcade game built inside Python!")

# Initialize stateful variables safely to prevent refresh crashes
if "ball_x" not in st.session_state:
    st.session_state.ball_x = 200
    st.session_state.ball_y = 250
    st.session_state.dx = 12
    st.session_state.dy = -12
    st.session_state.paddle_x = 160
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.win = False
    # Setup grid layout matrix for bricks (1 = Active, 0 = Broken)
    st.session_state.bricks = [[1 for _ in range(6)] for _ in range(3)]

# Game configuration settings
PADDLE_WIDTH = 90
BALL_RADIUS = 8
BRICK_ROWS = 3
BRICK_COLS = 6
BRICK_WIDTH = 60
BRICK_HEIGHT = 20

# 2. Control Layout Inputs
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Use standard slider to handle platform physics manually safely
    st.session_state.paddle_x = st.slider("Move Paddle Left / Right:", 0, 310, int(st.session_state.paddle_x))

# 3. Process Game Step Engine
if not st.session_state.game_over and not st.session_state.win:
    # Update movement steps
    st.session_state.ball_x += st.session_state.dx
    st.session_state.ball_y += st.session_state.dy

    # Side boundaries collision check
    if st.session_state.ball_x <= BALL_RADIUS or st.session_state.ball_x >= 400 - BALL_RADIUS:
        st.session_state.dx *= -1
    
    # Ceiling boundary collision check
    if st.session_state.ball_y <= BALL_RADIUS:
        st.session_state.dy *= -1

    # Paddle hits check
    if 360 <= st.session_state.ball_y <= 370:
        if st.session_state.paddle_x <= st.session_state.ball_x <= st.session_state.paddle_x + PADDLE_WIDTH:
            st.session_state.dy = -abs(st.session_state.dy) # Bounce up securely

    # Floor drop calculation check (Lose Condition)
    if st.session_state.ball_y > 400:
        st.session_state.game_over = True

    # Brick collision loops check
    active_bricks = 0
    for r in range(BRICK_ROWS):
        for c in range(BRICK_COLS):
            if st.session_state.bricks[r][c] == 1:
                active_bricks += 1
                bx = c * (BRICK_WIDTH + 5) + 10
                by = r * (BRICK_HEIGHT + 5) + 30
                
                # Check overlapping coordinates box match boundary logic
                if bx <= st.session_state.ball_x <= bx + BRICK_WIDTH:
                    if by <= st.session_state.ball_y <= by + BRICK_HEIGHT:
                        st.session_state.bricks[r][c] = 0 # Break brick
                        st.session_state.dy *= -1
                        st.session_state.score += 10
                        break
                        
    if active_bricks == 0:
        st.session_state.win = True

# 4. Draw Pure HTML5 Graphics Canvas Vector Box
html_canvas = f"""
<div style="text-align:center;">
    <svg width="400" height="400" style="background-color:#222; border: 4px solid #fff; border-radius: 8px;">
"""

# Draw bricks vector rendering loop
for r in range(BRICK_ROWS):
    for c in range(BRICK_COLS):
        if st.session_state.bricks[r][c] == 1:
            bx = c * (BRICK_WIDTH + 5) + 10
            by = r * (BRICK_HEIGHT + 5) + 30
            colors = ["#FF5733", "#33FF57", "#3357FF"]
            html_canvas += f'<rect x="{bx}" y="{by}" width="{BRICK_WIDTH}" height="{BRICK_HEIGHT}" fill="{colors[r]}" />'

# Add Paddle & Ball structures dynamically onto the map
html_canvas += f'<rect x="{st.session_state.paddle_x}" y="365" width="{PADDLE_WIDTH}" height="10" fill="#00FFCC" rx="4" />'
html_canvas += f'<circle cx="{st.session_state.ball_x}" cy="{st.session_state.ball_y}" r="{BALL_RADIUS}" fill="#FFFF00" />'
html_canvas += "</svg></div>"

st.markdown(html_canvas, unsafe_allow_html=True)

# 5. Interface Notifications Layout Status Controls
st.subheader(f"🏆 Score: {st.session_state.score}")

if st.session_state.game_over:
    st.error("💥 Game Over! The ball dropped.")
if st.session_state.win:
    st.success("🎉 You Win! All bricks cleared.")

# Refresh mechanism step triggers
if not st.session_state.game_over and not st.session_state.win:
    if st.button("Next Step ⚡"):
        st.rerun()

if st.button("Reset Game 🔄"):
    st.session_state.ball_x = 200
    st.session_state.ball_y = 250
    st.session_state.dx = 12
    st.session_state.dy = -12
    st.session_state.score = 0
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.bricks = [[1 for _ in range(6)] for _ in range(3)]
    st.rerun()
