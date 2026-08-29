import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="The Aariz Developer | Student Hub",
    page_icon="✨",
    layout="centered"
)
st.header("At the end by the information there will a digital card of you") 

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
st.title("Let's move to main game")
import random
import streamlit as st

st.set_page_config(page_title="DIGITAL_FIGHTER.EXE", page_icon="📟", layout="centered")

# --- CUSTOM CSS DIGITAL RETRO INJECTION ---
st.markdown("""
<style>
    /* Neon Cyberpunk Theme */
    @import url('https://googleapis.com');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0d0f12 !important;
        font-family: 'Share Tech Mono', monospace !important;
        color: #00ff66 !important;
    }
    
    h1, h2, h3, p, span, div {
        font-family: 'Share Tech Mono', monospace !important;
    }
    
    /* Glowing Headers */
    h1 {
        color: #00ffbb !important;
        text-shadow: 0 0 10px rgba(0, 255, 187, 0.6);
        text-align: center;
    }
    
    /* Digital Info Box */
    [data-testid="stNotification"] {
        background-color: #161b22 !important;
        border: 2px solid #00ff66 !important;
        border-radius: 4px !important;
        box-shadow: 0 0 15px rgba(0, 255, 102, 0.2);
        color: #00ff66 !important;
    }

    /* Cyber Buttons */
    button {
        background-color: #1a1f29 !important;
        color: #00ff66 !important;
        border: 1px solid #00ff66 !important;
        box-shadow: 0 0 5px rgba(0, 255, 102, 0.3) !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
    }
    
    button:hover {
        background-color: #00ff66 !important;
        color: #0d0f12 !important;
        box-shadow: 0 0 15px #00ff66 !important;
        border: 1px solid #00ff66 !important;
    }
    
    /* Matrix-like Progress/Health Bar */
    div[data-testid="stProgress"] > div > div > div > div {
        background-color: #00ff66 !important;
        box-shadow: 0 0 8px #00ff66;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Digital States
if "p1_health" not in st.session_state:
    st.session_state.p1_health = 100
if "p2_health" not in st.session_state:
    st.session_state.p2_health = 100
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "log" not in st.session_state:
    st.session_state.log = "[SYSTEM]: BOOT_SEQUENCE_COMPLETE. READY TO FIGHT."

def reset_game():
    st.session_state.p1_health = 100
    st.session_state.p2_health = 100
    st.session_state.game_over = False
    st.session_state.log = "[SYSTEM]: MEMORY_RESET. INITIALIZING ROUND_02."

# Header Terminal UI
st.title("💾 DIGITAL_FIGHTER.EXE")
st.write("`[STABLE_RELEASE // VER_2026.08]`")
st.divider()

# Core Data Layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("### `[USR_01 / PLAYER]`")
    st.progress(st.session_state.p1_health / 100.0)
    st.markdown(f"**HP_STAT:** `{st.session_state.p1_health} / 100`")

with col2:
    st.markdown("### `[CPU_02 / ENEMY]`")
    st.progress(st.session_state.p2_health / 100.0)
    st.markdown(f"**HP_STAT:** `{st.session_state.p2_health} / 100`")

st.divider()

# Terminal Log
st.info(st.session_state.log)

# Action Mechanics
def play_round(p1_move, p1_damage, p1_miss_chance):
    if st.session_state.game_over:
        return

    # Player Move
    if random.random() < p1_miss_chance:
        p1_msg = f">> P1_EXE: {p1_move} ... [FAILED / MISSED]"
        actual_p1_dmg = 0
    else:
        actual_p1_dmg = random.randint(max(1, p1_damage - 4), p1_damage + 4)
        p1_msg = f">> P1_EXE: {p1_move} ... [SUCCESS / DEAL: {actual_p1_dmg} DMG]"

    st.session_state.p2_health = max(0, st.session_state.p2_health - actual_p1_dmg)

    if st.session_state.p2_health == 0:
        st.session_state.game_over = True
        st.session_state.log = f"{p1_msg}\n\n[TERMINAL]: CRITICAL_ERROR at CPU_02. PLAYER WINS."
        return

    # CPU Counter
    cpu_moves = [
        ("KINETIC_HADOKEN", 16, 0.20),
        ("CYBER_UPPERCUT", 24, 0.35),
        ("BIT_STRIKE", 9, 0.05)
    ]
    cpu_move, cpu_dmg, cpu_miss = random.choice(cpu_moves)

    if random.random() < cpu_miss:
        cpu_msg = f">> CPU_EXE: {cpu_move} ... [FAILED / MISSED]"
        actual_cpu_dmg = 0
    else:
        actual_cpu_dmg = random.randint(max(1, cpu_dmg - 3), cpu_dmg + 3)
        cpu_msg = f">> CPU_EXE: {cpu_move} ... [SUCCESS / DEAL: {actual_cpu_dmg} DMG]"

    st.session_state.p1_health = max(0, st.session_state.p1_health - actual_cpu_dmg)

    if st.session_state.p1_health == 0:
        st.session_state.game_over = True
        st.session_state.log = f"{p1_msg}\n\n{cpu_msg}\n\n[TERMINAL]: USER_01 SYSTEM_CRASH. CPU WINS."
    else:
        st.session_state.log = f"{p1_msg}\n\n{cpu_msg}"

# Command Control Buttons
if not st.session_state.game_over:
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("RUN: BIT_PUNCH", use_container_width=True):
            play_round("BIT_PUNCH", 10, 0.05)
            st.rerun()
    with c2:
        if st.button("RUN: BEAM_KICK", use_container_width=True):
            play_round("BEAM_KICK", 22, 0.25)
            st.rerun()
    with c3:
        if st.button("RUN: HADOKEN.SH", use_container_width=True):
            play_round("HADOKEN.SH", 32, 0.45)
            st.rerun()
else:
    if st.button("REBOOT_SYSTEM.BAT", use_container_width=True):
        reset_game()
        st.rerun()
