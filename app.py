import streamlit as st

# 1. App Configuration Setup
st.set_page_config(
    page_title="EduAI - Python Basics",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Premium Dark & High-Contrast Institutional Custom UI Theme CSS
st.markdown("""
    <style>
    /* Main Background & Base Styling */
    .stApp {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
    }
    
    /* Institutional Accent Typography Rules */
    h1, h2, h3, h4, p, span, label {
        font-family: 'Inter', 'Segoe UI', system-ui, sans-serif !important;
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38BDF8, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    /* Course Module Badges */
    .badge {
        background-color: #1E293B;
        color: #38BDF8;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid #334155;
        display: inline-block;
        margin-bottom: 1rem;
    }

    /* Info Cards mimicking UniAthena micro-learning cards */
    .metric-card {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }
    
    .metric-val {
        font-size: 1.8rem;
        font-weight: 700;
        color: #F8FAFC;
    }
    
    .metric-lbl {
        font-size: 0.9rem;
        color: #94A3B8;
        margin-top: 4px;
    }

    /* Core Classroom Video Framework Box Layout */
    .video-frame {
        border-radius: 12px;
        overflow: hidden;
        border: 2px solid #334155;
        box-shadow: 0 20px 25px -5px rgba(0,0,0,0.3);
        margin-bottom: 1.5rem;
    }
    
    /* Sidebar list overriding to pure contrast elements */
    [data-testid="stSidebar"] {
        background-color: #0B0F19 !important;
        border-right: 1px solid #1E293B;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Sidebar Course syllabus index navigation
st.sidebar.markdown("### 🎓 Python Micro-Degree")
st.sidebar.markdown("---")

# Navigation state triggers
selected_lesson = st.sidebar.radio(
    "Course Syllabus Map:",
    [
        "🚀 Course Overview & Welcome",
        "📺 Module 1: AI Video - Introduction to Python Variables",
        "📺 Module 2: AI Video - Conditionals and Logic",
        "📺 Module 3: AI Video - Loops and Iteration"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Your Progress")
st.sidebar.progress(25 if "Welcome" in selected_lesson else 60)
st.sidebar.caption("1 of 4 Syllabus milestones unlocked")


# 4. VIEW RENDER ROUTER: Welcome Portal Overview View
if "Overview" in selected_lesson:
    st.markdown('<span class="badge">FREE MICRO-COURSE</span>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title">Programming Basics with AI Avatar</h1>', unsafe_allow_html=True)
    st.markdown("##### Powered by specialized generative instructional models. Accessible anytime, completely self-paced.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Hero Introduction Image Banner / Graphic representation slot
    st.image("https://unsplash.com", 
             caption="Flexible Micro-learning structure powered by Artificial Intelligence tutors.", 
             use_container_width=True)
    
    st.markdown("### 📌 About This Micro-Learning Unit")
    st.write(
        "Welcome to the premium introductory track for Python. Designed specifically for professional development, "
        "this module breaks down programming configurations into snackable content chunks. Each core concept is "
        "taught by an automated high-fidelity AI professor avatar paired with dynamic digital live whiteboard logs."
    )
    
    # Statistical Info Cards row grid layout
    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="metric-card"><div class="metric-val">15 Mins</div><div class="metric-lbl">Total Video Runtime</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="metric-card"><div class="metric-val">Beginner</div><div class="metric-lbl">Skill Requirement Entry Level</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="metric-card"><div class="metric-val">100% Free</div><div class="metric-lbl">Verified Certificate Track Option</div></div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("👉 Start Learning Now (Go to Module 1)", type="primary"):
        st.info("Excellent selection! Click on 'Module 1' inside the left sidebar panel to initiate your video lesson block.")


# 5. VIEW RENDER ROUTER: Core AI Classroom Learning Environment View
else:
    # Dynamically structure information fields depending on targeted subpage item selection
    if "Variables" in selected_lesson:
        title = "Module 1: Mastering Variables & Data Types"
        summary = "Learn how computers assign temporary runtime data memory using variables like Strings, Integers, and Floats."
        # Using a reliable instructional Python streaming animation/sample educational programming resource source video asset
        video_url = "https://w3schools.com" 
        notes = "💡 **Key Takeaway:** A variable acts like a labeled storage storage box. You assign values to it using the `=` operator sign token."
        
    elif "Conditionals" in selected_lesson:
        title = "Module 2: Branching Code logic via If-Else Statements"
        summary = "Direct your logic flowchart execution paths using true/false criteria validations smoothly."
        video_url = "https://sample-videos.com"
        notes = "💡 **Key Takeaway:** Indentation syntax blocks determine scope hierarchy inside Python script condition evaluation routes."
        
    else:
        title = "Module 3: Controlling Repeated Executions via Loops"
        summary = "Automate scaling iterative operations with elegant runtime loop patterns easily."
        video_url = "https://w3schools.com"
        notes = "💡 **Key Takeaway:** `for` loops iterate over a predefined sequence range, while `while` loops run continually until a boundary condition resolves."

    # Render Active Lesson UI Container Frame
    st.markdown(f'<span class="badge">LECTURE PREVIEW LAYER</span>', unsafe_allow_html=True)
    st.header(title)
    st.caption(summary)
    st.markdown("---")
    
    # Multi-Column Layout mimicking premium course platforms (Video Left, Study Materials Right)
    video_col, notes_col = st.columns([2, 1])
    
    with video_col:
        st.markdown('<div class="video-frame">', unsafe_allow_html=True)
        # Main instructional lecture video streaming asset element container
        st.video(video_url)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Action interaction panel row below player frame window
        ac1, ac2 = st.columns(2)
        with ac1:
            st.button("✅ Mark Video Module Complete", use_container_width=True)
        with ac2:
            st.button("📥 Download Presentation Slide Assets (.PDF)", use_container_width=True)

    with notes_col:
        st.markdown("### 📝 Digital Class Notes")
        st.info(notes)
        
        # Interactive sandbox playground area for validation test runs
        st.markdown("#### ⚡ Quick Check Challenge")
        st.write("Write an expression assigning the value `5` directly to a variable handle called `x`:")
        code_input = st.text_input("Type your python response script block here:", placeholder="x = ...")
        
        if code_input:
            clean_ans = code_input.replace(" ", "")
            if clean_ans == "x=5":
                st.success("🎯 Absolutely correct! Memory allocation criteria verified perfectly.")
            else:
                st.warning("⚠️ Not quite. Ensure you map value '5' rightwards of the equality variable assignment operator.")
