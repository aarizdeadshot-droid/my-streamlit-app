import streamlit as st
import random

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
    st.session_state.player_pose = "🤺 READY"
    st.session_state.enemy_pose = "READY 🤺"

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
        ["PlayGroup-kindergarden", "Class 1-8", "Class 9-10 (Matric / O-Levels)", "Class 11-12 (Inter / A-Levels)", "University Student", "Graduated"]
    )

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
        ["Coding 💻", "Gaming 🎮", "Football ⚽", "Reading 📚", "Photography 📷", "Music 🎵", "Art🎨"],
        default=["Coding 💻"]
    )
    bio = st.text_area("Bio", placeholder="I am a Junior python Develolper...", max_chars=15000)

st.divider()

# 5. Step 3: Contact Info
st.header("🌐 Step 3: Contact & Links")
col_left3, col_right3 = st.columns(2)

with col_left3:
    email = st.text_input("Email Address", placeholder="yourname@example.com")
with col_right3:
    WhatsApp_Number = st.text_input("WhatsApp Number", placeholder="WhatsApp Number")

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
# 7. TAEKWONDO GAME ENGINE WITH VISUAL POSES
# ==========================================
st.header("🥋 Taekwondo Combat Arena")

def reset_game():
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.stamina = 100
    fighter_title = full_name.upper() if full_name else "PLAYER"
    st.session_state.battle_log = [f"🥋 **Match Started!** {fighter_title} faces off against Black Belt 2nd Dan Sir Ishaq."]
    st.session_state.player_pose = "(o_o)¬ 🥋 [READY]"
    st.session_state.enemy_pose = "[READY] 🥋 ⌐(o_o)"
    st.session_state.game_active = True

if not st.session_state.game_active:
    if st.button("🔥 Start The Game", use_container_width=True):
        if not full_name or not school_name or not email:
            st.warning("⚠️ **Access Denied!** You must fill in your **Full Name**, **School Name**, and **Email Address** in Steps 1–3 before starting the game!")
        else:
            reset_game()
            st.rerun()

else:
    # Game Header Controls
    g_col1, g_col2 = st.columns([3, 1])
    with g_col1:
        st.subheader(f"Match: {full_name} (Blue) vs Sir Ishaq (Red)")
    with g_col2:
        if st.button("🔄 Reset Match"):
            reset_game()
            st.rerun()

    # VISUAL ARENA (Displays Action Poses)
    st.markdown("### 🏟️ Teakwondo Arena")
    with st.container(border=True):
        arena_left, arena_center, arena_right = st.columns([2, 1, 2])
        
        with arena_left:
            st.markdown(f"#### 🟦 {full_name}")
            st.code(st.session_state.player_pose, language="text")
            
        with arena_center:
            st.markdown("## 💥 VS 💥")
            
        with arena_right:
            st.markdown("#### 🟥 Sir Ishaq")
            st.code(st.session_state.enemy_pose, language="text")

    # Health & Stamina Displays
    st.write(f"**{full_name}'s Health**")
    st.progress(st.session_state.player_hp / 100, text=f"HP: {st.session_state.player_hp}/100")
    
    st.write("**Sir Ishaq's Health**")
    st.progress(st.session_state.enemy_hp / 100, text=f"HP: {st.session_state.enemy_hp}/100")

    st.write(f"⚡ **Stamina:** {st.session_state.stamina}/100")

    # Check Win/Loss Conditions
    if st.session_state.player_hp <= 0:
        st.error("💥 **KNOCKOUT!** You were defeated by Sir Ishaq.")
        st.session_state.player_pose = "(x_x) 😵 [KO'D]"
        st.session_state.enemy_pose = "🏆 ⌐(>_<) [WINNER]"
        st.session_state.game_active = False
    elif st.session_state.enemy_hp <= 0:
        st.balloons()
        st.success(f"🏆 **VICTORY!** {full_name} knocked out Sir Ishaq with a perfect technique!")
        st.session_state.player_pose = "🏆 (^_^) 🥋 [WINNER]"
        st.session_state.enemy_pose = "[KO'D] 😵 (x_x)"
        st.session_state.game_active = False
    else:
        # Move Action Buttons
        st.markdown("### Choose Your Move:")
        m1, m2, m3, m4 = st.columns(4)

        move = None
        if m1.button("🦵 Jab Kick", help="Low cost, fast hit"):
            move = "jab"
        if m2.button("💥 Roundhouse", help="High damage, chance to miss"):
            move = "roundhouse"
        if m3.button("🌪️ 360 Spin Kick", help="Massive damage, heavy stamina cost"):
            move = "spin"
        if m4.button("🛡️ Guard & Rest", help="Restores stamina & blocks damage"):
            move = "guard"

        # Combat Logic & Pose Animation Updates
        if move:
            player_dmg = 0
            enemy_dmg = 0
            log_text = ""

            # Player Turn Logic & Animation Setup
            if move == "jab":
                if st.session_state.stamina >= 10:
                    player_dmg = random.randint(8, 14)
                    st.session_state.stamina -= 10
                    st.session_state.player_pose = "🦵 (o_o)/~~  [JAB KICK!]"
                    log_text += f" You landed a sharp Jab Kick for **{player_dmg} DMG**!"
                else:
                    st.session_state.player_pose = "(>_<) 💦 [EXHAUSTED]"
                    log_text += " ⚠️ Out of stamina! Your attack failed."

            elif move == "roundhouse":
                if st.session_state.stamina >= 20:
                    st.session_state.stamina -= 20
                    if random.random() > 0.25:
                        player_dmg = random.randint(18, 26)
                        st.session_state.player_pose = "💥 (o_o)═🦵 [ROUNDHOUSE KICK!]"
                        log_text += f" 💥 **BOOM!** Roundhouse Kick lands for **{player_dmg} DMG**!"
                    else:
                        st.session_state.player_pose = "💨 (o_o)_  [MISSED KICK]"
                        log_text += " 💨 You swung with a Roundhouse but missed!"
                else:
                    st.session_state.player_pose = "(>_<) 💦 [EXHAUSTED]"
                    log_text += " ⚠️ Out of stamina!"

            elif move == "spin":
                if st.session_state.stamina >= 35:
                    st.session_state.stamina -= 35
                    if random.random() > 0.4:
                        player_dmg = random.randint(30, 42)
                        st.session_state.player_pose = "🌪️ 🦵(>o<)🦵 [360 SPIN KICK!]"
                        log_text += f" 🌪️ **CRITICAL!** 360 Spin Kick connects for **{player_dmg} DMG**!"
                    else:
                        st.session_state.player_pose = "💨 (~_~)  [SPUN & MISSED]"
                        log_text += " 💨 Your 360 Spin Kick missed wide!"
                else:
                    st.session_state.player_pose = "(>_<) 💦 [EXHAUSTED]"
                    log_text += " ⚠️ Out of stamina!"

            elif move == "guard":
                st.session_state.stamina = min(100, st.session_state.stamina + 35)
                st.session_state.player_pose = "🛡️ (u_u)🛡️ [GUARDING]"
                log_text += " 🛡️ You raised your guard and restored **+35 Stamina**."

            # Apply Damage to Enemy Pose
            st.session_state.enemy_hp = max(0, st.session_state.enemy_hp - player_dmg)
            if player_dmg > 0:
                st.session_state.enemy_pose = "[HIT! 💥] (><;)"

            # Enemy Counter-Attack Logic & Pose Updates
            if st.session_state.enemy_hp > 0:
                enemy_move = random.choice(["punch", "axe_kick", "heavy_side_kick"])
                
                if move == "guard":
                    enemy_dmg = random.randint(2, 6)
                    st.session_state.enemy_pose = "[BLOCKED!] 🦵 ⌐(o_o)"
                    log_text += f" Enemy kicked, but your guard absorbed it! Took only **{enemy_dmg} DMG**."
                else:
                    if enemy_move == "punch":
                        enemy_dmg = random.randint(6, 12)
                        st.session_state.enemy_pose = "[PUNCH!] 🥊 ⌐(o_o)"
                        log_text += f" Enemy punched you back for **{enemy_dmg} DMG**."
                    elif enemy_move == "axe_kick":
                        enemy_dmg = random.randint(12, 20)
                        st.session_state.enemy_pose = "[AXE KICK! 🦵] ⌐(o_o)"
                        log_text += f" Sir Ishaq delivered an Axe Kick for **{enemy_dmg} DMG**!"
                    elif enemy_move == "heavy_side_kick":
                        enemy_dmg = random.randint(20, 30)
                        st.session_state.enemy_pose = "[SIDE KICK! 💥🦵] ⌐(o_o)"
                        log_text += f" 🛑 Sir Ishaq caught you with a Side Kick for **{enemy_dmg} DMG**!"

                    st.session_state.player_pose += " 😵 [TAKING DAMAGE]"

                st.session_state.player_hp = max(0, st.session_state.player_hp - enemy_dmg)

            # Log Update & Screen Refresh
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
st.title("😡😡😡Still playing My Game do You your Office or school Work go ahead")
