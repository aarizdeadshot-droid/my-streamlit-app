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
st.title("Game Name: 🥋Teakwondo🥋")
