import random
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="The Aariz Developer | Student Hub",
    page_icon="✨",
    layout="centered",
)

# Initialize Session State Variables
if "card_generated" not in st.session_state:
    st.session_state.card_generated = False

if "game_active" not in st.session_state:
    st.session_state.game_active = False
    st.session_state.game_mode = "taekwondo"
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.stamina = 100
    st.session_state.battle_log = []
    st.session_state.player_pose = "🤺 READY"
    st.session_state.enemy_pose = "READY 🤺"

# 2. Developer Intro
st.title("The Aariz Developer ✨")
st.subheader("Interactive Student Profile & Bio Builder")
st.write(
    "Fill out the details below to generate a beautiful, shareable digital"
    " student card."
)

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
        [
            "PlayGroup-Kindergarten",
            "Class 1-8",
            "Class 9-10 (Matric / O-Levels)",
            "Class 11-12 (Inter / A-Levels)",
            "University Student",
            "Graduated",
        ],
    )

st.divider()

# 4. Step 2: Academic & Hobbies
st.header("📚 Step 2: Academic & Hobbies")
col_left2, col_right2 = st.columns(2)

with col_left2:
    school_name = st.text_input(
        "School / College / University / Office Name",
        placeholder="e.g. Army Public School",
    )
    fav_subject = st.text_input(
        "Favorite Subject", placeholder="e.g. Computer Science"
    )

with col_right2:
    hobbies = st.multiselect(
        "Select Your Hobbies",
        [
            "Coding 💻",
            "Gaming 🎮",
            "Football ⚽",
            "Reading 📚",
            "Photography 📷",
            "Music 🎵",
            "Art 🎨",
            
        ],
        default=["Coding 💻"],
    )
    bio = st.text_area(
        "Bio",
        placeholder="I am a Junior Python Developer...",
        max_chars=15000,
    )

st.divider()

# 5. Step 3: Contact Info
st.header("🌐 Step 3: Contact & Links")
col_left3, col_right3 = st.columns(2)

with col_left3:
    email = st.text_input("Email Address", placeholder="yourname@example.com")
with col_right3:
    WhatsApp_Number = st.text_input(
        "WhatsApp Number", placeholder="e.g. +923001234567"
    )

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
        st.markdown(
            f"📖 **Favorite Subject:**"
            f" {fav_subject if fav_subject else 'Not specified'}"
        )
        if hobbies:
            st.markdown(f"❤️ **Interests:** {' | '.join(hobbies)}")
        if bio:
            st.markdown(f'📝 **Bio:** *"{bio}"*')

        st.markdown("---")
        st.markdown(
            f"✉️ **Contact:** {email if email else 'No email provided'}"
        )
        if WhatsApp_Number:
            clean_num = "".join(filter(str.isdigit, WhatsApp_Number))
            st.markdown(
                f"🔗 **WhatsApp:**"
                f" [{WhatsApp_Number}](https://wa.me/{clean_num})"
            )

st.divider()

# ==========================================
# 7. GAME ENGINE & DUAL ARENAS
# ==========================================
st.header("🎮 Combat Arenas")


def reset_game(mode="taekwondo"):
    st.session_state.game_mode = mode
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.stamina = 100

    if mode == "taekwondo":
        fighter_title = full_name.upper() if full_name else "PLAYER"
        st.session_state.battle_log = [
            f"🥋 **Match Started!** {fighter_title} faces off against Black"
            " Belt 2nd Dan Sir Ishaq."
        ]
        st.session_state.player_pose = "(o_o)¬ 🥋 [READY]"
        st.session_state.enemy_pose = "[READY] 🥋 ⌐(o_o)"
    else:
        st.session_state.battle_log = [
            "⚔️ **Battle Commenced!** Muslims face off against Christians in"
            " combat!"
        ]
        st.session_state.player_pose = "⚔️ (o_o)🛡️ [READY]"
        st.session_state.enemy_pose = "[READY] 🛡️(o_o) 🗡️"

    st.session_state.game_active = True


if not st.session_state.game_active:
    btn_col1, btn_col2 = st.columns(2)

    with btn_col1:
        if st.button("🥋 Start Taekwondo Game", use_container_width=True):
            if not full_name or not school_name or not email:
                st.warning(
                    "⚠️ **Access Denied!** You must fill in your **Full"
                    " Name**, **School Name**, and **Email Address** in Steps"
                    " 1–3 before starting!"
                )
            else:
                reset_game("taekwondo")
                st.rerun()

    with btn_col2:
        if st.button(
            "⚔️ Start Muslims vs Christians Fight", use_container_width=True
        ):
            if not full_name or not school_name or not email:
                st.warning(
                    "⚠️ **Access Denied!** You must fill in your **Full"
                    " Name**, **School Name**, and **Email Address** in Steps"
                    " 1–3 before starting!"
                )
            else:
                reset_game("crusades")
                st.rerun()

else:
    mode = st.session_state.game_mode

    # Set Display Names based on selected mode
    if mode == "taekwondo":
        player_disp = full_name if full_name else "Player"
        enemy_disp = "Sir Ishaq"
    else:
        player_disp = "Muslims"
        enemy_disp = "Christians"

    # Game Header Controls
    g_col1, g_col2 = st.columns([3, 1])
    with g_col1:
        if mode == "taekwondo":
            st.subheader(f"Match: {player_disp} (Blue) vs Sir Ishaq (Red)")
        else:
            st.subheader("Battle: Muslims vs Christians")

    with g_col2:
        if st.button("🔄 Reset Match"):
            reset_game(mode)
            st.rerun()

    # VISUAL ARENA
    if mode == "taekwondo":
        st.markdown("### 🏟️ Taekwondo Arena")
        enemy_label = f"🟥 {enemy_disp}"
    else:
        st.markdown("### 🏟️ Battlefield")
        enemy_label = f"🔴 {enemy_disp}"

    with st.container(border=True):
        arena_left, arena_center, arena_right = st.columns([2, 1, 2])

        with arena_left:
            st.markdown(f"#### 🟦 {player_disp}")
            st.code(st.session_state.player_pose, language="text")

        with arena_center:
            st.markdown("## 💥 VS 💥")

        with arena_right:
            st.markdown(f"#### {enemy_label}")
            st.code(st.session_state.enemy_pose, language="text")

    # Health & Stamina Displays
    st.write(f"**{player_disp}'s Health**")
    st.progress(
        st.session_state.player_hp / 100,
        text=f"HP: {st.session_state.player_hp}/100",
    )

    st.write(f"**{enemy_disp}'s Health**")
    st.progress(
        st.session_state.enemy_hp / 100,
        text=f"HP: {st.session_state.enemy_hp}/100",
    )

    st.write(f"⚡ **Stamina:** {st.session_state.stamina}/100")

    # Check Win/Loss Conditions
    if st.session_state.player_hp <= 0:
        st.error(f"💥 **DEFEAT!** {player_disp} were defeated by {enemy_disp}.")
        st.session_state.player_pose = "(x_x) 😵 [KO'D]"
        st.session_state.enemy_pose = "🏆 ⌐(>_<) [WINNER]"
        st.session_state.game_active = False
    elif st.session_state.enemy_hp <= 0:
        st.balloons()
        st.success(
            f"🏆 **VICTORY!** {player_disp} defeated {enemy_disp} in combat!"
        )
        st.session_state.player_pose = "🏆 (^_^) 🥋 [WINNER]"
        st.session_state.enemy_pose = "[KO'D] 😵 (x_x)"
        st.session_state.game_active = False
    else:
        # Move Action Buttons
        st.markdown("### Choose Your Move:")
        m1, m2, m3, m4 = st.columns(4)

        move = None

        if mode == "taekwondo":
            if m1.button("🦵 Jab Kick", help="Low cost, fast hit"):
                move = "m1"
            if m2.button("💥 Roundhouse", help="High damage, chance to miss"):
                move = "m2"
            if m3.button(
                "🌪️ 360 Spin Kick", help="Massive damage, heavy stamina cost"
            ):
                move = "m3"
            if m4.button(
                "🛡️ Guard & Rest", help="Restores stamina & blocks damage"
            ):
                move = "m4"
        else:
            if m1.button("🗡️ Scimitar Slash", help="Fast strike, low cost"):
                move = "m1"
            if m2.button("🛡️ Shield Bash", help="Moderate damage"):
                move = "m2"
            if m3.button("🐎 Cavalry Charge", help="Heavy damage"):
                move = "m3"
            if m4.button("🏰 Defensive Guard", help="Restores stamina"):
                move = "m4"

        # Combat Logic & Pose Animation Updates
        if move:
            player_dmg = 0
            enemy_dmg = 0
            log_text = ""

            # Player Turn Logic
            if mode == "crusades":
                # ALWAYS WIN LOGIC FOR MUSLIMS MODE:
                # Attacks deal massive damage and cost minimal/no stamina
                if move in ["m1", "m2", "m3"]:
                    player_dmg = random.randint(40, 60)
                    st.session_state.player_pose = (
                        "⚔️ (o_o)/~~ [VICTORIOUS STRIKE!]"
                    )
                    log_text += (
                        f" {player_disp} landed a powerful strike for"
                        f" **{player_dmg} DMG**!"
                    )
                elif move == "m4":
                    st.session_state.stamina = 100
                    st.session_state.player_pose = "🛡️ (u_u)🛡️ [UNBREAKABLE]"
                    log_text += (
                        f" {player_disp} raised their shield and fully restored"
                        " Stamina!"
                    )
            else:
                # Standard Taekwondo Mode Logic
                if move == "m1":
                    if st.session_state.stamina >= 10:
                        player_dmg = random.randint(8, 15)
                        st.session_state.stamina -= 10
                        st.session_state.player_pose = (
                            "🦵 (o_o)/~~ [LIGHT ATTACK!]"
                        )
                        log_text += (
                            f" {player_disp} landed a hit for"
                            f" **{player_dmg} DMG**!"
                        )
                    else:
                        st.session_state.player_pose = "(>_<) 💦 [EXHAUSTED]"
                        log_text += " ⚠️ Out of stamina!"

                elif move == "m2":
                    if st.session_state.stamina >= 20:
                        st.session_state.stamina -= 20
                        if random.random() > 0.25:
                            player_dmg = random.randint(18, 26)
                            st.session_state.player_pose = (
                                "💥 (o_o)═🦵 [MEDIUM ATTACK!]"
                            )
                            log_text += (
                                f" 💥 **BOOM!** Attack lands for"
                                f" **{player_dmg} DMG**!"
                            )
                        else:
                            st.session_state.player_pose = "💨 (o_o)_ [MISSED]"
                            log_text += " 💨 Attack missed!"
                    else:
                        st.session_state.player_pose = "(>_<) 💦 [EXHAUSTED]"
                        log_text += " ⚠️ Out of stamina!"

                elif move == "m3":
                    if st.session_state.stamina >= 35:
                        st.session_state.stamina -= 35
                        if random.random() > 0.4:
                            player_dmg = random.randint(30, 42)
                            st.session_state.player_pose = (
                                "🌪️ (>o<) [HEAVY ATTACK!]"
                            )
                            log_text += (
                                f" 🌪️ **CRITICAL!** Heavy hit connects for"
                                f" **{player_dmg} DMG**!"
                            )
                        else:
                            st.session_state.player_pose = "💨 (~_~) [MISSED]"
                            log_text += " 💨 Heavy attack missed wide!"
                    else:
                        st.session_state.player_pose = "(>_<) 💦 [EXHAUSTED]"
                        log_text += " ⚠️ Out of stamina!"

                elif move == "m4":
                    st.session_state.stamina = min(
                        100, st.session_state.stamina + 35
                    )
                    st.session_state.player_pose = "🛡️ (u_u)🛡️ [GUARDING]"
                    log_text += (
                        " 🛡️ Raised guard and restored **+35 Stamina**."
                    )

            # Apply Damage to Enemy
            st.session_state.enemy_hp = max(
                0, st.session_state.enemy_hp - player_dmg
            )
            if player_dmg > 0:
                st.session_state.enemy_pose = "[HIT! 💥] (><;)"

            # Enemy Counter-Attack Logic
            if st.session_state.enemy_hp > 0:
                if mode == "crusades":
                    # Enemy attacks always deal 0 damage in Crusades Mode
                    enemy_dmg = 0
                    st.session_state.enemy_pose = "[ATTACK BLOCKED!] 🗡️ ⌐(o_o)"
                    log_text += (
                        f" {enemy_disp} attempted to counter-attack, but"
                        " dealt **0 DMG**!"
                    )
                else:
                    # Standard Taekwondo Mode Enemy Logic
                    enemy_move = random.choice(["light", "medium", "heavy"])

                    if move == "m4":
                        enemy_dmg = random.randint(2, 6)
                        st.session_state.enemy_pose = "[BLOCKED!] 🦵 ⌐(o_o)"
                        log_text += (
                            f" {enemy_disp} attacked, but guard absorbed it!"
                            f" Took only **{enemy_dmg} DMG**."
                        )
                    else:
                        if enemy_move == "light":
                            enemy_dmg = random.randint(6, 12)
                            st.session_state.enemy_pose = (
                                "[ATTACK!] 🥊 ⌐(o_o)"
                            )
                            log_text += (
                                f" {enemy_disp} hit back for **{enemy_dmg}"
                                " DMG**."
                            )
                        elif enemy_move == "medium":
                            enemy_dmg = random.randint(12, 20)
                            st.session_state.enemy_pose = (
                                "[STRIKE!] 🦵 ⌐(o_o)"
                            )
                            log_text += (
                                f" {enemy_disp} struck for **{enemy_dmg}"
                                " DMG**!"
                            )
                        elif enemy_move == "heavy":
                            enemy_dmg = random.randint(20, 30)
                            st.session_state.enemy_pose = (
                                "[HEAVY STRIKE! 💥] ⌐(o_o)"
                            )
                            log_text += (
                                f" 🛑 {enemy_disp} landed a heavy strike for"
                                f" **{enemy_dmg} DMG**!"
                            )

                        st.session_state.player_pose += " 😵 [TAKING DAMAGE]"

                st.session_state.player_hp = max(
                    0, st.session_state.player_hp - enemy_dmg
                )

            # Log Update
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
    st.write(
    "💡Tip : Press the upper left arrow onmobiles to close the menu and play it with fullscreen to enjoy.")
    st.write(
        "This application dynamically builds custom profile cards using raw"
        " input data variables.")
