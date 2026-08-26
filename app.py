import streamlit as st

# 1. App Configuration Setup
st.set_page_config(
    page_title="UniAthena Elite - Python Professional Certification",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize global session tracking variables for courses and badges
if "completed_lessons" not in st.session_state:
    st.session_state.completed_lessons = set()

# 2. Premium Academic Theme Custom UI Theme CSS
st.markdown("""
    <style>
    /* Main Background & Base Styling */
    .stApp {
        background-color: #0B0F19 !important;
        color: #F1F5F9 !important;
    }
    
    h1, h2, h3, h4, p, label {
        font-family: 'Inter', 'Segoe UI', system-ui, sans-serif !important;
    }
    
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38BDF8, #818CF8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .badge-certified {
        background-color: #1E1B4B;
        color: #C084FC;
        padding: 5px 12px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 700;
        border: 1px solid #4338CA;
        display: inline-block;
    }

    .video-frame {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #334155;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3);
        background-color: #020617;
        padding: 10px;
        margin-bottom: 1.5rem;
    }
    
    /* Sidebar customization */
    [data-testid="stSidebar"] {
        background-color: #020617 !important;
        border-right: 1px solid #1E293B;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Data Dictionary: Professional Syllabus, Video Assets & Quiz Configurations
course_modules = {
    "Overview": {
        "title": "Certified Professional Python Track Overview",
        "desc": "Executive Diploma program structured into flexible micro-learning modules.",
        "video": None
    },
    "Module 1": {
        "title": "Module 1: Syntax Foundations & Variables",
        "desc": "Understanding memory reservation, structural tokens, and strong data naming conventions.",
        "video": "https://w3schools.com",
        "quiz_prompt": "Create an academic multiple choice quiz with 3 questions checking basic python variables and syntax rules. Set difficulty to beginner."
    },
    "Module 2": {
        "title": "Module 2: Flow Control & Boolean Evaluation",
        "desc": "Structuring operational workflows through code branching logical statements.",
        "video": "https://sample-videos.com",
        "quiz_prompt": "Create a multiple choice assessment quiz with 3 questions testing python if-else statement scopes and indentation requirements. Set difficulty to easy."
    },
    "Module 3": {
        "title": "Module 3: Loop Structures & Infinite Controls",
        "desc": "Automating continuous executions efficiently using For and While loops.",
        "video": "https://w3schools.com",
        "quiz_prompt": "Create a python evaluation quiz with 3 questions focusing on loop iterations, breaking conditions, and range intervals. Set difficulty to intermediate."
    },
    "Module 4": {
        "title": "Module 4: Data Structures (Lists & Dictionaries)",
        "desc": "Mastering nested arrays, hash tables, and variable object grouping workflows.",
        "video": "https://w3schools.com",
        "quiz_prompt": "Create a 3 question multiple choice test on python data collections including list indices and dictionary key assignment rules."
    },
    "Module 5": {
        "title": "Module 5: Custom Functional Architecture",
        "desc": "Writing reusable code modules using return parameters, scoping configurations, and functions.",
        "video": "https://sample-videos.com",
        "quiz_prompt": "Generate a 3 question technical quiz covering Python function definition syntax, keyword arguments, and lexical scope bounds."
    },
    "Module 6": {
        "title": "Module 6: Object-Oriented Paradigm (OOP)",
        "desc": "Building classes, initializers, inheritance trees, and encapsulation protocols.",
        "video": "https://w3schools.com",
        "quiz_prompt": "Generate an academic multiple choice test with 3 questions exploring OOP concepts inside python like self arguments and method overriding rules."
    }
}

# 4. Sidebar Student Panel and Micro-Learning Map
st.sidebar.markdown("### 🏛️ UniAthena Portal")
st.sidebar.markdown('<span class="badge-certified">PROFESSIONAL CERTIFICATE</span>', unsafe_allow_html=True)
st.sidebar.markdown("---")

selected_key = st.sidebar.radio(
    "Syllabus Milestone Tracking Map:",
    options=list(course_modules.keys()),
    format_func=lambda x: course_modules[x]["title"]
)

# Calculate system certification metrics
total_lessons = len(course_modules) - 1 # Excluding entry overview
completion_rate = int((len(st.session_state.completed_lessons) / total_lessons) * 100)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Module Progress Track")
st.sidebar.progress(completion_rate)
st.sidebar.caption(f"Completed {len(st.session_state.completed_lessons)} of {total_lessons} Graded Modules ({completion_rate}%)")

if completion_rate == 100:
    st.sidebar.balloons()
    st.sidebar.success("🏆 Certification Requirements Fulfilled! Ready for Academic Audit.")

# 5. VIEW ROUTER: Landing Introduction View
if selected_key == "Overview":
    st.markdown('<h1 class="hero-title">Professional Certification in Python Foundations</h1>', unsafe_allow_html=True)
    st.write("#### Offered in compliance with global micro-learning accessibility criteria.")
    st.markdown("---")
    
    st.image("https://unsplash.com", 
             caption="Flexible Micro-learning structure powered by Artificial Intelligence tutors.", use_container_width=True)
    
    st.markdown("### 📌 Course Delivery Architecture")
    st.info("💡 **UniAthena Blueprint:** Watch the byte-sized micro-lecture block on the left panel, and complete the integrated interactive multiple choice assessment test right beside it to lock in your certification credit points.")
    
    if st.button("Proceed to First Module Lecture 🚀", type="primary"):
        st.info("Select 'Module 1' from the sidebar menu to begin learning.")

# 6. VIEW ROUTER: Core Micro-Learning Lecture & Graded Quiz View
else:
    module = course_modules[selected_key]
    st.markdown(f'<h3>{module["title"]}</h3>', unsafe_allow_html=True)
    st.caption(module["desc"])
    st.markdown("---")
    
    # Split UI space into standard UniAthena Academic layout (Lecture Left, Assessment Right)
    col_left, col_right = st.columns([1.1, 0.9])
    
    with col_left:
        st.markdown("<h4>📺 High-Fidelity Video Lecture</h4>", unsafe_allow_html=True)
        st.markdown('<div class="video-frame">', unsafe_allow_html=True)
        st.video(module["video"])
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Mark Lesson Complete validation utility
        if selected_key not in st.session_state.completed_lessons:
            if st.button("🗳️ Mark Lecture & Quiz Complete", key=f"btn_{selected_key}", use_container_width=True):
                st.session_state.completed_lessons.add(selected_key)
                st.rerun()
        else:
            st.success("✨ Module Complete! Credit units successfully saved to your dashboard.")

    with col_right:
        st.markdown("<h4>✍️ Module Quiz Assessment</h4>", unsafe_allow_html=True)
        st.caption("Verify understanding to unlock your credit units")
        
        # Inject the unique interactive quiz placeholder snippet mapped to our dynamic prompt text configs
        quizPlaceholder(prompt=module["quiz_prompt"])
