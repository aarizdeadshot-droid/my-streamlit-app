import streamlit as st

# Set up clean light page layout
st.set_page_config(page_title="The Student Adventure Game", page_icon="🎮")

# Initialize game progression state safely
if "game_started" not in st.session_state:
    st.session_state.game_started = False

st.title("🎮 The Academy Adventure Game")
st.write("Enter your profile details below to generate your custom text adventure!")
st.markdown("---")

# --- STEP 1: USER PROFILE INPUTS ---
# Input text fields for user profile details
name = st.text_input("👤 Enter your Name:", placeholder="Type your name here...")
user_class = st.text_input("🏫 Enter your Class/Grade:", placeholder="e.g., Grade 10, Computer Science...")
superpower = st.selectbox("⚡ Choose your special skill:", ["Invisibility", "Super Speed", "Mind Reading", "Coding Genius"])
pet = st.text_input("🐾 Enter your favorite animal (Your Companion):", placeholder="e.g., Dragon, Cat, Wolf...")

# --- STEP 2: GAME ENGINE MECHANICS ---
if name and user_class and pet:
    # Hello Greeting Trigger Button
    if not st.session_state.game_started:
        if st.button(f"🚀 Start Game: Hello {name}!"):
            st.session_state.game_started = True
            st.rerun()

    # --- STEP 3: THE GAME STORY ---
    if st.session_state.game_started:
        st.success(f"👋 **Hello {name}!** Welcome to your custom adventure.")
        
        st.markdown(f"""
        ### 📖 The Story Begins...
        You are sitting quietly in your **{user_class}** room when suddenly, the clock stops ticking. 
        Your loyal companion, a magical **{pet}**, jumps out of your backpack and points toward the window!
        
        A mysterious portal has opened in the middle of the school hallway. The principal has been trapped inside!
        """)
        
        # Game choices structure
        choice = st.radio("What do you want to do?", [
            "Select an action...",
            f"Use your {superpower} ability to sneak into the portal",
            f"Send your {pet} inside first to scout the area",
            "Ignore the portal and try to escape the school premises"
        ])
        
        # Display story outcome based on chosen action paths
        if choice == f"Use your {superpower} ability to sneak into the portal":
            st.info(f"✨ Excellent choice! Your **{superpower}** skill worked perfectly. You saved the principal without anyone seeing you!")
        elif choice == f"Send your {pet} inside first to scout the area":
            st.info(f"🐾 Brave move! Your **{pet}** safely triggered all the traps inside, clearing a secure path for you to walk through.")
        elif choice == "Ignore the portal and try to escape the school premises":
            st.warning("🏃‍♂️ You ran out the front door, but the entire town outside turned upside down! There is no escaping this quest.")

        st.markdown("---")
        
        # Bye Greeting Trigger Button (End Game Game State reset)
        if st.button(f"🏁 Finish Game: Bye {name}!"):
            st.session_state.game_started = False
            st.success("💾 Game session reset successfully. Thanks for playing!")
            st.rerun()
else:
    st.warning("⚠️ Please fill in all the input boxes above (Name, Class, and Animal) to begin the game setup!")
