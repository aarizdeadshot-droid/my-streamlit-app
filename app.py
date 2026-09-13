# ==========================================
# 7. HISTORICAL COMBAT ARENA (CRUSADES THEME)
# ==========================================
st.header("⚔️ Medieval Historical Arena")


def reset_game():
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.stamina = 100
    fighter_title = full_name.upper() if full_name else "MUSLIM CHAMPION"
    st.session_state.battle_log = [
        f"⚔️ **Battle Commenced!** {fighter_title} enters the field against"
        " Crusader Knight Sir Guy."
    ]
    st.session_state.player_pose = "⚔️ (o_o)🛡️ [READY]"
    st.session_state.enemy_pose = "[READY] 🛡️(o_o) 🗡️"
    st.session_state.game_active = True


if not st.session_state.game_active:
    if st.button("🔥 Start The Battle", use_container_width=True):
        if not full_name or not school_name or not email:
            st.warning(
                "⚠️ **Access Denied!** You must fill in your **Full Name**,"
                " **School Name**, and **Email Address** in Steps 1–3 before"
                " starting the battle!"
            )
        else:
            reset_game()
            st.rerun()

else:
    # Game Header Controls
    g_col1, g_col2 = st.columns([3, 1])
    with g_col1:
        st.subheader(
            f"Battle: {full_name} (Muslim Champion) vs Sir Guy (Crusader"
            " Knight)"
        )
    with g_col2:
        if st.button("🔄 Reset Battle"):
            reset_game()
            st.rerun()

    # VISUAL ARENA (Displays Combat Poses)
    st.markdown("### 🏟️ Battlefield")
    with st.container(border=True):
        arena_left, arena_center, arena_right = st.columns([2, 1, 2])

        with arena_left:
            st.markdown(f"#### 🟢 {full_name}")
            st.code(st.session_state.player_pose, language="text")

        with arena_center:
            st.markdown("## 💥 VS 💥")

        with arena_right:
            st.markdown("#### 🔴 Crusader Sir Guy")
            st.code(st.session_state.enemy_pose, language="text")

    # Health & Stamina Displays
    st.write(f"**{full_name}'s Health**")
    st.progress(
        st.session_state.player_hp / 100,
        text=f"HP: {st.session_state.player_hp}/100",
    )

    st.write("**Sir Guy's Health**")
    st.progress(
        st.session_state.enemy_hp / 100,
        text=f"HP: {st.session_state.enemy_hp}/100",
    )

    st.write(f"⚡ **Stamina:** {st.session_state.stamina}/100")

    # Check Win/Loss Conditions
    if st.session_state.player_hp <= 0:
        st.error("💥 **DEFEAT!** You were overcome in battle by Sir Guy.")
        st.session_state.player_pose = "(x_x) 😵 [FALLEN]"
        st.session_state.enemy_pose = "🏆 ⌐(>_<) [VICTORIOUS]"
        st.session_state.game_active = False
    elif st.session_state.enemy_hp <= 0:
        st.balloons()
        st.success(
            f"🏆 **VICTORY!** {full_name} claims victory on the battlefield!"
        )
        st.session_state.player_pose = "🏆 (^_^) ⚔️ [VICTORIOUS]"
        st.session_state.enemy_pose = "[DEFEATED] 😵 (x_x)"
        st.session_state.game_active = False
    else:
        # Action Buttons
        st.markdown("### Choose Your Strategy:")
        m1, m2, m3, m4 = st.columns(4)

        move = None
        if m1.button("🗡️ Scimitar Slash", help="Fast strike, low stamina cost"):
            move = "slash"
        if m2.button("🛡️ Shield Bash", help="Moderate damage & disruption"):
            move = "bash"
        if m3.button("🐎 Cavalry Charge", help="Heavy damage, high stamina cost"):
            move = "charge"
        if m4.button("🏰 Defensive Guard", help="Restores stamina & blocks damage"):
            move = "guard"

        # Combat Logic & Pose Updates
        if move:
            player_dmg = 0
            enemy_dmg = 0
            log_text = ""

            # Player Action Logic
            if move == "slash":
                if st.session_state.stamina >= 10:
                    player_dmg = random.randint(10, 16)
                    st.session_state.stamina -= 10
                    st.session_state.player_pose = (
                        "🗡️ (o_o)/~~  [SCIMITAR SLASH!]"
                    )
                    log_text += (
                        f" You struck with a quick Scimitar Slash for"
                        f" **{player_dmg} DMG**!"
                    )
                else:
                    st.session_state.player_pose = "(>_<) 💦 [EXHAUSTED]"
                    log_text += " ⚠️ Out of stamina! Strike failed."

            elif move == "bash":
                if st.session_state.stamina >= 20:
                    st.session_state.stamina -= 20
                    if random.random() > 0.2:
                        player_dmg = random.randint(18, 25)
                        st.session_state.player_pose = (
                            "🛡️💥 (o_o)  [SHIELD BASH!]"
                        )
                        log_text += (
                            f" 💥 **IMPACT!** Shield Bash connects for"
                            f" **{player_dmg} DMG**!"
                        )
                    else:
                        st.session_state.player_pose = (
                            "💨 (o_o)_  [BASH MISSED]"
                        )
                        log_text += " 💨 Your shield bash missed!"
                else:
                    st.session_state.player_pose = "(>_<) 💦 [EXHAUSTED]"
                    log_text += " ⚠️ Out of stamina!"

            elif move == "charge":
                if st.session_state.stamina >= 35:
                    st.session_state.stamina -= 35
                    if random.random() > 0.35:
                        player_dmg = random.randint(32, 45)
                        st.session_state.player_pose = (
                            "🐎⚔️ (>o<)  [CAVALRY CHARGE!]"
                        )
                        log_text += (
                            f" 🌪️ **DEVASTATING!** Cavalry Charge hits for"
                            f" **{player_dmg} DMG**!"
                        )
                    else:
                        st.session_state.player_pose = (
                            "💨 (~_~)  [CHARGE EVADED]"
                        )
                        log_text += " 💨 Sir Guy dodged your charge!"
                else:
                    st.session_state.player_pose = "(>_<) 💦 [EXHAUSTED]"
                    log_text += " ⚠️ Out of stamina!"

            elif move == "guard":
                st.session_state.stamina = min(
                    100, st.session_state.stamina + 35
                )
                st.session_state.player_pose = "🛡️ (u_u)🛡️ [HOLDING LINE]"
                log_text += (
                    " 🛡️ You held your guard and regained **+35 Stamina**."
                )

            # Apply Damage to Enemy
            st.session_state.enemy_hp = max(
                0, st.session_state.enemy_hp - player_dmg
            )
            if player_dmg > 0:
                st.session_state.enemy_pose = "[HIT! 💥] (><;)"

            # Enemy Counter-Attack Logic
            if st.session_state.enemy_hp > 0:
                enemy_move = random.choice(
                    ["sword_strike", "lance_thrust", "crossbow_bolt"]
                )

                if move == "guard":
                    enemy_dmg = random.randint(2, 6)
                    st.session_state.enemy_pose = "[BLOCKED!] 🗡️ ⌐(o_o)"
                    log_text += (
                        " Sir Guy attacked, but your guard deflected it! Took"
                        f" only **{enemy_dmg} DMG**."
                    )
                else:
                    if enemy_move == "sword_strike":
                        enemy_dmg = random.randint(8, 14)
                        st.session_state.enemy_pose = "[SWORD STRIKE!] 🗡️ ⌐(o_o)"
                        log_text += (
                            f" Sir Guy slashed back for **{enemy_dmg} DMG**."
                        )
                    elif enemy_move == "lance_thrust":
                        enemy_dmg = random.randint(14, 22)
                        st.session_state.enemy_pose = "[LANCE THRUST! 🔱] ⌐(o_o)"
                        log_text += (
                            " Sir Guy landed a heavy Lance Thrust for"
                            f" **{enemy_dmg} DMG**!"
                        )
                    elif enemy_move == "crossbow_bolt":
                        enemy_dmg = random.randint(22, 32)
                        st.session_state.enemy_pose = (
                            "[CROSSBOW BOLT! 🏹] ⌐(o_o)"
                        )
                        log_text += (
                            f" 🛑 Crossbow bolt struck you for **{enemy_dmg}"
                            " DMG**!"
                        )

                    st.session_state.player_pose += " 😵 [TAKING DAMAGE]"

                st.session_state.player_hp = max(
                    0, st.session_state.player_hp - enemy_dmg
                )

            # Log Update & Screen Refresh
            st.session_state.battle_log.insert(0, log_text)
            st.rerun()

    # Combat Log Display
    st.markdown("### 📜 Battle Log")
    with st.container(border=True):
        for entry in st.session_state.battle_log[:5]:
            st.write(entry)
