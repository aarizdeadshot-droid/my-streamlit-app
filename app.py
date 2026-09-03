import streamlit as st
import random
import time

# 1. Page Configuration
st.set_page_config(
    page_title="The Aariz Developer | Student Hub",
    page_icon="✨",
    layout="centered"
)

# Initialize Session State Variables
if "card_generated" not in st.session_state:
    st.session_state.card_generated = False

if "game_active" not in st.session_state:
    st.session_state.game_active = False
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.stamina = 100
    st.session_state.battle_log = []

# 2. Developer Intro
st.title("The Aariz Developer ✨")
st.subheader("Interactive Student Profile & Bio Builder")
st.write("Fill out the details below to generate a beautiful, shareable digital student card.")

st.divider()

# 3. Step 1: Personal Details
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

# 4. Step 2: Academic & Hobbies
st.header("📚 Step 2: Academic & Hobbies")
col_left2, col_right2 = st.columns(2)

with col_left2:
    school_name = st.text_input("School / College / University Name", placeholder="e.g. Army Public School")
    fav_subject = st.text_input("Favorite Subject", placeholder="e.g. Computer Science")

with col_right2:
    hobbies = st.multiselect(
        "Select Your Hobbies",
        ["Coding 💻", "Gaming 🎮", "Cricket 🏏", "Football ⚽", "Reading 📚", "Photography 📷", "Music 🎵", "Art🎨"],
        default=["Coding 💻"]
    )
    bio = st.text_area("Short Bio", placeholder="I am passionate about technology...", max_chars=150)

st.divider()

# 5. Step 3: Contact Info
st.header("🌐 Step 3: Contact & Links")
col_left3, col_right3 = st.columns(2)

with col_left3:
    email = st.text_input("Email Address", placeholder="yourname@example.com")
with col_right3:
    github_link = st.text_input("GitHub Profile Link", placeholder="https://github.com")

st.divider()

# 6. Profile Card Generation
st.header("🪪 Generated Digital Profile Card")

if st.button("🔥 Create My Profile Card", use_container_width=True):
    if not full_name:
        st.error("❌ Please enter your **Full Name** in Step 1.")
        st.session_state.card_generated = False
    elif not school_name:
        st.error("❌ Please enter your **School/College Name** in Step 2.")
        st.session_state.card_generated = False
    else:
        st.session_state.card_generated = True
        st.balloons()

if st.session_state.card_generated:
    st.success("🎉 Your digital card is ready!")
    with st.container(border=True):
        st.markdown(f"## 🪪 {full_name.upper()}")
        st.markdown(f"**🏫 Institution:** {school_name}")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label="Class", value=student_class)
        with c2:
            st.metric(label="Age", value=f"{age} Y/O")
        with c3:
            st.metric(label="Roll No.", value=roll_number if roll_number else "N/A")
        
        st.markdown("---")
        st.markdown(f"📖 **Favorite Subject:** {fav_subject if fav_subject else 'Not specified'}")
        if hobbies:
            st.markdown(f"❤️ **Interests:** {' | '.join(hobbies)}")
        if bio:
            st.markdown(f"📝 **Bio:** *\"{bio}\"*")
            
        st.markdown("---")
        st.markdown(f"✉️ **Contact:** {email if email else 'No email provided'}")
        if github_link:
            st.markdown(f"🔗 **GitHub:** [{github_link}]({github_link})")

st.divider()

# ==========================================
# 7. TAEKWONDO GAME ENGINE
# ==========================================
st.header("🥋 Taekwondo Combat Arena")

def reset_game():
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.stamina = 100
    st.session_state.battle_log = ["🥋 **Match Started!** Face off against Red Belt Master Jin."]
    st.session_state.game_active = True

if not st.session_state.game_active:
    if st.button("🔥 Start The Game", use_container_width=True):
        reset_game()
        st.rerun()

else:
    # Game Header Controls
    g_col1, g_col2 = st.columns([3, 1])
    with g_col1:
        st.subheader("Match: You (Blue Corner) vs Master Jin (Red Corner)")
    with g_col2:
        if st.button("🔄 Reset Match"):
            reset_game()
            st.rerun()

    # Health & Stamina Displays
    st.write("**Your Health**")
    st.progress(st.session_state.player_hp / 100, text=f"HP: {st.session_state.player_hp}/100")
    
    st.write("**Master Jin Health**")
    st.progress(st.session_state.enemy_hp / 100, text=f"HP: {st.session_state.enemy_hp}/100")

    st.write(f"⚡ **Stamina:** {st.session_state.stamina}/100")

    # Check Win/Loss Conditions
    if st.session_state.player_hp <= 0:
        st.error("💥 **KNOCKOUT!** You were defeated by Master Jin.")
        st.session_state.game_active = False
    elif st.session_state.enemy_hp <= 0:
        st.balloons()
        st.success("🏆 **VICTORY!** You knocked out Master Jin with a perfect technique!")
        st.session_state.game_active = False
    else:
        # Move Action Buttons
        st.markdown("### Choose Your Martial Arts Move:")
        m1, m2, m3, m4 = st.columns(4)

        move = None
        if m1.button("🦵 Fast Jab Kick", help="Low cost, guaranteed hit"):
            move = "jab"
        if m2.button("💥 Roundhouse Kick", help="High damage, chance to miss"):
            move = "roundhouse"
        if m3.button("🌪️ 360 Spin Kick", help="Massive damage, uses heavy stamina"):
            move = "spin"
        if m4.button("🛡️ Guard & Rest", help="Restores stamina & reduces incoming damage"):
            move = "guard"

        # Combat Logic Execution
        if move:
            player_dmg = 0
            enemy_dmg = 0
            log_text = ""

            # Player Turn
            if move == "jab":
                if st.session_state.stamina >= 10:
                    player_dmg = random.randint(8, 14)
                    st.session_state.stamina -= 10
                    log_text += f" You landed a sharp Jab Kick for **{player_dmg} DMG**!"
                else:
                    log_text += " ⚠️ Out of stamina! Your attack failed."

            elif move == "roundhouse":
                if st.session_state.stamina >= 20:
                    st.session_state.stamina -= 20
                    if random.random() > 0.25: # 75% hit rate
                        player_dmg = random.randint(18, 26)
                        log_text += f" 💥 **BOOM!** Powerful Roundhouse Kick lands for **{player_dmg} DMG**!"
                    else:
                        log_text += " 💨 You swung with a Roundhouse but missed!"
                else:
                    log_text += " ⚠️ Out of stamina!"

            elif move == "spin":
                if st.session_state.stamina >= 35:
                    st.session_state.stamina -= 35
                    if random.random() > 0.4: # 60% hit rate
                        player_dmg = random.randint(30, 42)
                        log_text += f" 🌪️ **CRITICAL!** Dynamic 360 Spin Kick connects for **{player_dmg} DMG**!"
                    else:
                        log_text += " 💨 Your 360 Spin Kick missed wide!"
                else:
                    log_text += " ⚠️ Out of stamina!"

            elif move == "guard":
                st.session_state.stamina = min(100, st.session_state.stamina + 35)
                log_text += " 🛡️ You raised your guard and restored **+35 Stamina**."

            # Apply Damage to Enemy
            st.session_state.enemy_hp = max(0, st.session_state.enemy_hp - player_dmg)

            # Enemy Counter-Attack (if still alive)
            if st.session_state.enemy_hp > 0:
                enemy_move = random.choice(["punch", "axe_kick", "heavy_side_kick"])
                
                if move == "guard":
                    enemy_dmg = random.randint(2, 6) # Reduced damage when guarding
                    log_text += f" Enemy attacked, but your guard absorbed it! Took only **{enemy_dmg} DMG**."
                else:
                    if enemy_move == "punch":
                        enemy_dmg = random.randint(6, 12)
                        log_text += f" Enemy punched you back for **{enemy_dmg} DMG**."
                    elif enemy_move == "axe_kick":
                        enemy_dmg = random.randint(12, 20)
                        log_text += f" Master Jin delivered an Axe Kick for **{enemy_dmg} DMG**!"
                    elif enemy_move == "heavy_side_kick":
                        enemy_dmg = random.randint(20, 30)
                        log_text += f" 🛑 Master Jin caught you with a Side Kick for **{enemy_dmg} DMG**!"

                st.session_state.player_hp = max(0, st.session_state.player_hp - enemy_dmg)

            # Log Update & Refresh Screen
            st.session_state.battle_log.insert(0, log_text)
            st.rerun()

    # Combat Log Display
    st.markdown("### 📜 Combat Log")
    with st.container(border=True):
        for entry in st.session_state.battle_log[:5]:
            st.write(entry)

# 8. Sidebar Information Terminal
with st.sidebar:
    st.title("⚙️ System Control")
    st.write("This application dynamically builds custom profile cards using raw input data variables.")
    st.info("💡 **Aariz Developer Tip:** Click the arrow icon in the top left corner on mobile devices to collapse this menu panel.")
    st.write("System Status:")
    st.progress(100, text="All modules operational")
