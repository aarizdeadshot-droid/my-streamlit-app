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
import random

# 1. Page & Aesthetic Configuration
st.set_page_config(page_title="Space Wave: Infinite Fleet", page_icon="🚀", layout="centered")
st.title("🚀 Space Wave: Infinite Fleet")
st.write("Defend your sector, collect cosmic scrap, and survive the endless alien waves!")

# 2. Initialize Space Station Systems (Session State)
if "scrap" not in st.session_state:
    st.session_state.scrap = 0
if "shields" not in st.session_state:
    st.session_state.shields = 100
if "wave" not in st.session_state:
    st.session_state.wave = 1
if "laser_tier" not in st.session_state:
    st.session_state.laser_tier = 1  # Laser weapon damage multi
if "drones" not in st.session_state:
    st.session_state.drones = 0      # Automated scrap collectors

weapon_names = {1: "Pulse Laser", 2: "Plasma Cannon", 3: "Photon Torpedo", 4: "Antimatter Beam"}

# 3. Dynamic Costs & Upgrades
upgrade_laser_costs = {1: 30, 2: 150, 3: 600, 4: float('inf')}
current_laser_cost = upgrade_laser_costs[st.session_state.laser_tier]
drone_cost = 20 + (st.session_state.drones ** 2) * 12

# Automated passive income from worker drones
passive_scrap = st.session_state.drones * 2
if passive_scrap > 0:
    st.session_state.scrap += passive_scrap

# 4. Core Core Game Action Methods
def fire_lasers():
    # Tap to shoot incoming wave debris and gather resources
    damage_dealt = st.session_state.laser_tier * 3
    st.session_state.scrap += damage_dealt
    
    # Progress wave mechanics slightly on action
    if random.randint(1, 10) == 10:
        st.session_state.wave += 1

def repair_shields():
    if st.session_state.scrap >= 10 and st.session_state.shields < 100:
        st.session_state.scrap -= 10
        st.session_state.shields = min(100, st.session_state.shields + 25)

def upgrade_weapons():
    global current_laser_cost
    if st.session_state.scrap >= current_laser_cost and st.session_state.laser_tier < 4:
        st.session_state.scrap -= current_laser_cost
        st.session_state.laser_tier += 1

def buy_drone():
    if st.session_state.scrap >= drone_cost:
        st.session_state.scrap -= drone_cost
        st.session_state.drones += 1

# 5. Dashboard Visual Design Setup
col_stats1, col_stats2, col_stats3 = st.columns(3)

with col_stats1:
    st.metric("Sector Wave", f"Wave {st.session_state.wave} 🛸")

with col_stats2:
    st.metric("Cosmic Scrap", f"{st.session_state.scrap} 💎")

with col_stats3:
    # Color warning conditional indicator for structural health
    if st.session_state.shields > 40:
        st.metric("Hull Shields", f"{st.session_state.shields}% 🛡️")
    else:
        st.metric("Hull Shields", f"{st.session_state.shields}% 🚨")

# Primary Engagement Zone
st.button("💥 Fire Laser Batteries!", on_click=fire_lasers, use_container_width=True)

st.divider()
st.subheader("🛰️ Hangar Deck & Tech Upgrades")

col_shop1, col_shop2 = st.columns(2)

with col_shop1:
    st.markdown("### Offensive Systems")
    if st.session_state.laser_tier < 4:
        next_weapon = weapon_names[st.session_state.laser_tier + 1]
        st.write(f"**Equip {next_weapon}**")
        st.caption(f"Multiplies blast scrap output. Cost: {current_laser_cost} Scrap")
        st.button(
            "⚡ Upgrade Cannons", 
            on_click=upgrade_weapons, 
            disabled=(st.session_state.scrap < current_laser_cost),
            use_container_width=True
        )
    else:
        st.success("🌌 Flagship status achieved! Max weapons armed.")

with col_shop2:
    st.markdown("### Automation & Repair")
    st.write(f"**Deploy Collector Drone**")
    st.caption(f"Passively collects +2 scrap. Cost: {drone_cost} Scrap (Owned: {st.session_state.drones})")
    st.button(
        "🛸 Launch Drone", 
        on_click=buy_drone, 
        disabled=(st.session_state.scrap < drone_cost),
        use_container_width=True
    )
    
    st.write("")
    st.write(f"**Emergency Shield Recharge**")
    st.caption("Restores 25% hull integrity. Cost: 10 Scrap")
    st.button(
        "🛠️ Fix Defenses", 
        on_click=repair_shields, 
        disabled=(st.session_state.scrap < 10 or st.session_state.shields >= 100),
        use_container_width=True
    )

# 6. Incoming Alien Wave Invasion Calculation
# Difficulty modifier scales dynamically based on current Sector wave
invasion_chance = 4 + (st.session_state.wave // 3)
if random.randint(1, 15) <= invasion_chance and st.session_state.wave > 1:
    damage_taken = random.randint(5, 15)
    st.error(f"⚠️ Warning! Incoming Enemy Starfighters attacked! Shields depleted by {damage_taken}%.")
    st.session_state.shields = max(0, st.session_state.shields - damage_taken)

# Game Over State Safety Evaluation
if st.session_state.shields <= 0:
    st.error("💀 Your ship's hulls ruptured. The space station was lost to the alien fleet!")
    if st.button("🔄 Respawn New Fleet"):
        st.session_state.scrap = 0
        st.session_state.shields = 100
        st.session_state.wave = 1
        st.session_state.laser_tier = 1
        st.session_state.drones = 0
