import streamlit as st

# 1. Premium App Configuration Setup
st.set_page_config(
    page_title="UniAthena Professional - Python with AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize global session tracking variables for course progress
if "completed_lessons" not in st.session_state:
    st.session_state.completed_lessons = set()

# 2. Premium Academic Theme Custom UI Theme CSS
st.markdown("""
    <style>
    /* Main Background & Base Styling */
    .stApp {
        background-color: #0A0F1D !important;
        color: #F1F5F9 !important;
    }
    
    h1, h2, h3, h4, p, label {
        font-family: 'Inter', 'Segoe UI', system-ui, sans-serif !important;
    }
    
    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38BDF8, #A78BFA);
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

    /* Video Frame optimized for wide scaling and fullscreen playback */
    .video-frame {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #334155;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.5);
        background-color: #020617;
        padding: 6px;
        margin-bottom: 1.5rem;
        width: 100%;
    }
    
    /* Sidebar customization */
    [data-testid="stSidebar"] {
        background-color: #020617 !important;
        border-right: 1px solid #1E293B;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Practical Core Data: High-Quality Python & AI Practical Tutorials
course_modules = {
    "Overview": {
        "title": "Course Portal Overview",
        "desc": "Executive Diploma program structured into flexible micro-learning modules.",
        "video": None,
        "practical_notes": None
    },
    "Module 1": {
        "title": "Module 1: Python Basics & Variables",
        "desc": "Master environmental setup, standard naming protocols, variable types, and memory tracking.",
        "video": "https://www.youtube.com/watch?v=rfscVS0vtbw",  # Full freeCodeCamp Practical Foundation
        "practical_notes": "🧪 **Hands-on Lab:** Use variables to assign storage locations for real datasets. Avoid starting labels with numbers.",
        "quiz_prompt": "Create a 3 question academic multiple choice quiz covering basic Python data types like Strings, Floats, and Integers."
    },
    "Module 2": {
        "title": "Module 2: Practical Math Operations",
        "desc": "Building automated calculation logic routines using standard and advanced math modules.",
        "video": "https://www.youtube.com/watch?v=ix9cRaBkVe0",  # Python Arithmetic Operators & Math Functions
        "practical_notes": "🧪 **Hands-on Lab:** Use operators like modulus `%` and exponents `**` to calculate equations programmatically.",
        "quiz_prompt": "Create an easy 3 question quiz testing basic arithmetic operators and math module definitions in Python."
    },
    "Module 3": {
        "title": "Module 3: Code Structure & Logic Loops",
        "desc": "Mastering control flows, nested arrays, lists, dictionaries, and code loop structures.",
        "video": "https://www.youtube.com/watch?v=eWzpxwHX7YE",  # Control Flow & Arrays Tutorial
        "practical_notes": "🧪 **Hands-on Lab:** Practice data structure isolation using list indexing rules and dictionaries.",
        "quiz_prompt": "Create an intermediate 3 question quiz evaluating list slicing indexing and dictionary lookup keys in Python."
    },
    "Module 4": {
        "title": "Module 4: Environment Setup & Data Science Basics",
        "desc": "Learn how to use Anaconda environments, run files in Jupyter, and import NumPy/Pandas packages.",
        "video": "https://www.youtube.com/watch?v=CMEWVn1uZpQ",  # Setup Environment & Pandas Foundations
        "practical_notes": "🧪 **Hands-on Lab:** Run packages inside a workspace and manage multi-dimensional datasets smoothly.",
        "quiz_prompt": "Create a 3 question quiz verifying installation steps for Anaconda and how to correctly import external packages like Pandas."
    },
    "Module 5": {
        "title": "Module 5: Python Application in AI Ecosystems",
        "desc": "Deep dive into real-world AI framework development and building automated script systems.",
        "video": "https://www.youtube.com/watch?v=FaC9RyS1Pk0",  # Python Roadmap for AI Projects
        "practical_notes": "🧪 **Hands-on Lab:** Analyze salary metric files and utilize AI models to speed up development pipelines.",
        "quiz_prompt": "Create a 3 question quiz examining Python's role within the machine learning pipeline and module calling structures."
    },
    "Module 6": {
        "title": "Module 6: Building AI Agents from Scratch",
        "desc": "Final Capstone practical: Writing script files to connect with external LLM engines and structure data.",
        "video": "https://www.youtube.com/watch?v=bTMPwUgLZf0",  # Code execution for a real AI Agent
        "practical_notes": "🧪 **Hands-on Lab:** Build an autonomous research system utilizing API keys and tool structures in Python.",
        "quiz_prompt": "Create an advanced 3 question quiz testing custom functional properties, token configurations, and building functional AI systems in Python."
    }
}

# 4. Sidebar Student Panel and Micro-Learning Map
st.sidebar.markdown("### 🏛️ UniAthena Digital Campus")
st.sidebar.markdown('<span class="badge-certified">PYTHON & AI SPECIALIZATION</span>', unsafe_allow_html=True)
st.sidebar.markdown("---")

selected_key = st.sidebar.radio(
    "Syllabus Milestones:",
    options=list(course_modules.keys()),
    format_func=lambda x: course_modules[x]["title"]
)

# Calculate system certification metrics dynamically
total_lessons = len(course_modules) - 1
completion_rate = int((len(st.session_state.completed_lessons) / total_lessons) * 100)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Graded Progress Tracker")
st.sidebar.progress(completion_rate)
st.sidebar.caption(f"Cleared {len(st.session_state.completed_lessons)} of {total_lessons} Modules ({completion_rate}%)")

if completion_rate == 100:
    st.sidebar.balloons()
    st.sidebar.success("🏆 Certification Requirements Fulfilled! Ready for Academic Audit.")

# 5. VIEW ROUTER: Landing Introduction View
if selected_key == "Overview":
    st.markdown('<h1 class="hero-title">Professional Certificate in Python Programming & AI</h1>', unsafe_allow_html=True)
    st.write("#### Blended Academic Track matching UniAthena's micro-learning structural specifications.")
    st.markdown("---")
    
    st.image("https://unsplash.com", 
             caption="Flexible Micro-learning structure powered by Artificial Intelligence tutors.", use_container_width=True)
    
    st.markdown("### 📌 Course Architecture & Guidelines")
    st.info("💡 **UniAthena Blueprint:** Select a module from the left sidebar. Watch the practical lesson, read the code notes, and complete the automated evaluation quiz to lock in your academic certification points.")
    
    if st.button("Proceed to First Lecture 🚀", type="primary"):
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
        st.markdown("<h4>📺 High-Fidelity Practical Lecture</h4>", unsafe_allow_html=True)
        st.caption("💡 **Tip:** Hover over the player window and click the **Square Frame Icon** in the bottom-right corner to open Fullscreen mode instantly.")
        
        st.markdown('<div class="video-frame">', unsafe_allow_html=True)
        # Plays real production YouTube code tutorial assets cleanly 
        st.video(module["video"])
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Practical Sandbox lab notes area
        st.markdown("### 📝 Lab Workbook Notes")
        st.info(module["practical_notes"])
        
        # Mark Lesson Complete tracking checkbox utility
        if selected_key not in st.session_state.completed_lessons:
            if st.button("🗳️ Mark Module Complete", key=f"btn_{selected_key}", use_container_width=True):
                st.session_state.completed_lessons.add(selected_key)
                st.rerun()
        else:
            st.success("✨ Module Saved! Graduation credits successfully updated.")

    with col_right:
        st.markdown("<h4>✍️ Module Quiz Assessment</h4>", unsafe_allow_html=True)
        st.caption("Complete the quiz parameters below to unlock your certificate checkpoint.")
        
        # Inject the interactive quiz layer matching the localized context variables
        quizPlaceholder(prompt=module["quiz_prompt"])
