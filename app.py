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

st.set_page_config(page_title="THE DRAGON VS THE UNDISPUTED", page_icon="🥊", layout="centered")

# --- COMPLETE ARCADE INTERIOR HOUSING INJECTION ---
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0b0c10 !important;
        font-family: 'Press Start 2P', monospace !important;
        color: #fff;
    }

    /* Outer CRT Screen Frame Containing Everything */
    .arcade-cabinet-screen {
        background: #111424;
        border: 10px solid #222;
        border-radius: 14px;
        padding: 20px;
        box-shadow: inset 0 0 40px #000, 0 0 25px rgba(102, 252, 241, 0.3);
        margin-bottom: 20px;
    }
    
    /* Internal HUD Panel for health gauges */
    .internal-hud {
        display: flex;
        justify-content: space-between;
        background: rgba(0,0,0,0.6);
        padding: 10px;
        border: 2px solid #333;
        margin-bottom: 15px;
        font-size: 9px;
    }
    .hud-player { color: #ffcc00; }
    .hud-cpu { color: #ff3333; text-align: right; }
    
    /* Health Core Bar Containers */
    .hp-track {
        width: 140px; height: 12px; background: #441111;
        border: 1px solid #ff3333; margin-top: 4px; overflow: hidden;
    }
    .hp-fill { height: 100%; background: #00ff66; transition: width 0.2s ease; }

    /* Moving Audience Rows */
    .audience-gallery {
        display: flex;
        justify-content: space-around;
        padding: 8px 0;
        background: rgba(0,0,0,0.3);
        border-bottom: 3px dotted #ff0055;
    }
    .pixel-fan {
        width: 10px; height: 14px; background: #45a29e;
        animation: cheer 0.3s infinite alternate ease-in-out;
    }
    .pixel-fan:nth-child(even) { background: #66fcf1; animation-delay: 0.1s; }

    /* Referee Layer */
    .referee-container { display: flex; justify-content: center; margin: 8px 0; }
    .pixel-ref {
        width: 14px; height: 24px;
        background: linear-gradient(to bottom, #fff 30%, #000 30%, #000 70%, #fff 70%);
        border: 1px solid #fff; animation: refSway 1s infinite alternate ease-in-out;
    }

    /* Fighting Ground Canvas */
    .ring-floor {
        background: #c5a880; border-top: 5px double #ff0055;
        height: 140px; display: flex; justify-content: space-between;
        align-items: flex-end; padding: 0 25px; position: relative;
    }

    /* Bruce Lee Block-Pixel Assembly */
    .bruce-lee-sprite { display: flex; flex-direction: column; align-items: center; width: 45px; transition: transform 0.1s; }
    .bruce-head { width: 16px; height: 16px; background: #ffdbac; border-radius: 3px; border-bottom: 3px solid #000; }
    .bruce-chest { width: 24px; height: 22px; background: #ffdbac; display:flex; justify-content:space-between; }
    .bruce-arm { width: 5px; height: 15px; background: #ffdbac; }
    .bruce-pants { width: 22px; height: 22px; background: #ffcc00; border-left: 3px solid #000; border-right: 3px solid #000; }
    .bruce-boots { display: flex; justify-content: space-between; width: 24px; }
    .bruce-foot { width: 8px; height: 6px; background: #111; }

    /* Yuri Boyka Block-Pixel Assembly */
    .yuri-boyka-sprite { display: flex; flex-direction: column; align-items: center; width: 45px; transition: transform 0.1s; }
    .boyka-head { width: 18px; height: 18px; background: #e0ac69; border-radius: 3px; border-bottom: 3px solid #222; }
    .boyka-chest { width: 28px; height: 22px; background: #e0ac69; }
    .boyka-pants { width: 26px; height: 22px; background: #111; border-top: 3px solid #cc0000; }
    .boyka-boots { display: flex; justify-content: space-between; width: 28px; }
    .boyka-foot { width: 9px; height: 6px; background: #fff; }

    /* Action Keyframes & Toggles */
    .p1-striking { animation: attackLeft 0.15s ease-in-out; }
    .p2-striking { animation: attackRight 0.15s ease-in-out; }
    .damaged { animation: hitFlash 0.2s 2 ease-in-out; }

    @keyframes cheer { from { transform: translateY(0); } to { transform: translateY(-6px); } }
    @keyframes refSway { from { transform: rotate(-4deg); } to { transform: rotate(4deg); } }
    @keyframes attackLeft { 0% { transform: translateX(0); } 50% { transform: translateX(50px); } 100% { transform: translateX(0); } }
    @keyframes attackRight { 0% { transform: translateX(0); } 50% { transform: translateX(-50px); } 100% { transform: translateX(0); } }
    @keyframes hitFlash { 0% { background: #ff0000; opacity: 0.5; } 100% { } }

    /* Internal Embedded Ticker Feed Box */
    .internal-feed {
        background: #000; border: 2px solid #66fcf1;
        padding: 8px; margin-top: 15px; font-size: 8px;
        color: #66fcf1; text-align: center; line-height: 1.4;
    }

    /* Clean Streamlit Default Headers */
    [data-testid="stHeader"] {display:none;}
    div.block-container {padding-top: 2rem !important;}
    
    /* Control System Overrides */
    button {
        font-family: 'Press Start 2P', monospace !important; font-size: 10px !important;
        background: #1f2833 !important; color: #66fcf1 !important;
        border: 2px solid #45a29e !important; padding: 12px 4px !important;
    }
    button:hover { background: #66fcf1 !important; color: #0b0c10 !important; }
</style>
""", unsafe_allow_html=True)

# --- RUN APPDATA SYSTEM STATE ---
if "game_active" not in st.session_state:
    st.session_state.game_active = False
if "p1_hp" not in st.session_state:
    st.session_state.p1_hp = 100
if "p2_hp" not in st.session_state:
    st.session_state.p2_hp = 100
if "p1_ani" not in st.session_state:
    st.session_state.p1_ani = ""
if "p2_ani" not in st.session_state:
    st.session_state.p2_ani = ""
if "log_feed" not in st.session_state:
    st.session_state.log_feed = "ROUND_01: FIGHT"

def reset_arena():
    st.session_state.p1_hp = 100
    st.session_state.p2_hp = 100
    st.session_state.p1_ani = ""
    st.session_state.p2_ani = ""
    st.session_state.log_feed = "ROUND_02: FIGHT"

# --- SCENE SWITCH CONTROLLERS ---

# SPLASH HOUSING SCREEN
if not st.session_state.game_active:
    st.markdown("""
    <div class="arcade-cabinet-screen">
        <h1 style='text-align: center; color: #66fcf1; font-size:18px;'>FISTS_OF_GLORY.EXE</h1>
        <hr style='border: 1px solid #45a29e;'>
        <p style='color:#fff; font-size:10px; text-align:center; margin: 30px 0;'>BRUCE LEE [P1]<br><br>VS<br><br>YURI BOYKA [CPU]</p>
        <div class="internal-feed">PRESS INITIALIZE BUTTON BELOW TO MOUNT CAB MATRIX</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("INITIALIZE_SYSTEM", use_container_width=True):
        st.session_state.game_active = True
        st.rerun()

# LIVE INTEGRATED MACHINE ARENA SCREEN
else:
    st.markdown(f"""
    <div class="arcade-cabinet-screen">
        
        <!-- Inside Screen HUD Layout Tracker -->
        <div class="internal-hud">
            <div class="hud-player">
                <div>BRUCE (P1)</div>
                <div class="hp-track"><div class="hp-fill" style="width: {st.session_state.p1_hp}%;"></div></div>
                <div style="margin-top:4px;">{st.session_state.p1_hp}/100 HP</div>
            </div>
            <div class="hud-cpu">
                <div>BOYKA (CPU)</div>
                <div class="hp-track"><div class="hp-fill" style="width: {st.session_state.p2_hp}%; background:#ff3333;"></div></div>
                <div style="margin-top:4px;">{st.session_state.p2_hp}/100 HP</div>
            </div>
        </div>
        
        <!-- Live Audience Grid -->
        <div class="audience-gallery">
            <div class="pixel-fan"></div><div class="pixel-fan"></div>
            <div class="pixel-fan"></div><div class="pixel-fan"></div>
            <div class="pixel-fan"></div><div class="pixel-fan"></div>
            <div class="pixel-fan"></div><div class="pixel-fan"></div>
        </div>
        
        <!-- Ring Referee Assembly -->
        <div class="referee-container">
            <div class="pixel-ref"></div>
        </div>
        
        <!-- Canvas Arena Floor Mat -->
        <div class="ring-floor">
            <!-- P1 Fighter Render -->
            <div class="bruce-lee-sprite {st.session_state.p1_ani}">
                <div class="bruce-head"></div>
                <div class="bruce-chest"><div class="bruce-arm"></div><div class="bruce-arm"></div></div>
                <div class="bruce-pants"></div>
                <div class="bruce-boots"><div class="bruce-foot"></div><div class="bruce-foot"></div></div>
            </div>
            
            <!-- CPU Fighter Render -->
            <div class="yuri-boyka-sprite {st.session_state.p2_ani}">
                <div class="boyka-head"></div>
                <div class="boyka-chest"></div>
                <div class="boyka-pants"></div>
                <div class="boyka-boots"><div class="boyka-foot"></div><div class="boyka-foot"></div></div>
            </div>
        </div>
        
        <!-- Inside Screen Combat Text Logger Feed -->
        <div class="internal-feed">
            {st.session_state.log_feed}
        </div>
        
    </div>
    """, unsafe_allow_html=True)

    # TURN COMBAT LOGIC CALCULATIONS ENGINE
    def process_turn(move_name, base_dmg, dodge_chance):
        if st.session_state.p1_hp <= 0 or st.session_state.p2_hp <= 0:
            return

        st.session_state.p1_ani = "p1-striking"
        st.session_state.p2_ani = ""

        # Bruce Striking Event
        if random.random() < dodge_chance:
            st.session_state.log_feed = f"P1 USE: {move_name} -> BOYKA DODGED"
            p1_dmg = 0
        else:
            p1_dmg = random.randint(base_dmg - 2, base_dmg + 3)
            st.session_state.p2_ani = "damaged"
            st.session_state.p2_hp = max(0, st.session_state.p2_hp - p1_dmg)
