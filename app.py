import random
import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="The Aariz | Student portal",
    page_icon="✨",
    layout="centered",
)

# Initialize Session State Variables
if "card_generated" not in st.session_state:
    st.session_state.card_generated = False

if "choosing_faction" not in st.session_state:
    st.session_state.choosing_faction = False

if "game_active" not in st.session_state:
    st.session_state.game_active = False
    st.session_state.game_mode = "taekwondo"
    st.session_state.chosen_faction = "Muslims"
    st.session_state.player_hp = 100
    st.session_state.enemy_hp = 100
    st.session_state.stamina = 100
    st.session_state.battle_log = []
    st.session_state.player_pose = "READY"
    st.session_state.enemy_pose = "READY"

# 2. Developer Intro 
COVER_IMAGE = "Aariz.png"
print(COVER_IMAGE)
st.title("The Aariz | Student Portal")
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
    full_name = st.text_input("Full Name", placeholder="e.g. Aariz Bin Azmat,Azmat Hameed etc.")
    age = st.number_input("Age", min_value=5, max_value=122, value=16, step=1)

with col_right:
    student_class = st.selectbox(
        "Current Class / Grade",
        [
            "PlayGroup-Kindergarten",
            "Class 1-4 (Primary School)",
            "Class 5-8(Middle School)",
            "Class 9-10 (Matric / O-Levels / High School)",
            "Class 11-12 (Inter / A-Levels / High School)",
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
        "School / College / University Name",
        placeholder="e.g. The Educators <?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="878pt" height="1044pt" viewBox="0 0 878 1044" version="1.1"><defs><clipPath id="clip1"><path d="M 204 302 L 674 302 L 674 425 L 204 425 Z M 204 302 "></path></clipPath><clipPath id="clip2"><path d="M 237.097656 573.832031 C 260.578125 603 285.789063 628.519531 312.355469 650.519531 C 352.832031 684.039063 396.386719 709.40625 441.6875 727.082031 C 490.035156 707.484375 533.246094 681.40625 571.53125 648.898438 C 610.335938 615.945313 644.132813 576.355469 673.148438 530.179688 L 673.148438 311.910156 C 529.710938 284.371094 430.28125 323.835938 346.949219 356.921875 C 295.871094 377.195313 250.753906 395.105469 204.886719 394.195313 L 204.886719 529.835938 C 213.136719 542.226563 227.957031 561.972656 237.15625 573.820313 Z M 237.097656 573.832031 "></path></clipPath><clipPath id="clip3"><path d="M 204 372 L 674 372 L 674 509 L 204 509 Z M 204 372 "></path></clipPath><clipPath id="clip4"><path d="M 237.097656 573.832031 C 260.578125 603 285.789063 628.519531 312.355469 650.519531 C 352.832031 684.039063 396.386719 709.40625 441.6875 727.082031 C 490.035156 707.484375 533.246094 681.40625 571.53125 648.898438 C 610.335938 615.945313 644.132813 576.355469 673.148438 530.179688 L 673.148438 311.910156 C 529.710938 284.371094 430.28125 323.835938 346.949219 356.921875 C 295.871094 377.195313 250.753906 395.105469 204.886719 394.195313 L 204.886719 529.835938 C 213.136719 542.226563 227.957031 561.972656 237.15625 573.820313 Z M 237.097656 573.832031 "></path></clipPath><clipPath id="clip5"><path d="M 204 461 L 674 461 L 674 598 L 204 598 Z M 204 461 "></path></clipPath><clipPath id="clip6"><path d="M 237.097656 573.832031 C 260.578125 603 285.789063 628.519531 312.355469 650.519531 C 352.832031 684.039063 396.386719 709.40625 441.6875 727.082031 C 490.035156 707.484375 533.246094 681.40625 571.53125 648.898438 C 610.335938 615.945313 644.132813 576.355469 673.148438 530.179688 L 673.148438 311.910156 C 529.710938 284.371094 430.28125 323.835938 346.949219 356.921875 C 295.871094 377.195313 250.753906 395.105469 204.886719 394.195313 L 204.886719 529.835938 C 213.136719 542.226563 227.957031 561.972656 237.15625 573.820313 Z M 237.097656 573.832031 "></path></clipPath><clipPath id="clip7"><path d="M 396 317 L 530 317 L 530 444 L 396 444 Z M 396 317 "></path></clipPath><clipPath id="clip8"><path d="M 237.097656 573.832031 C 260.578125 603 285.789063 628.519531 312.355469 650.519531 C 352.832031 684.039063 396.386719 709.40625 441.6875 727.082031 C 490.035156 707.484375 533.246094 681.40625 571.53125 648.898438 C 610.335938 615.945313 644.132813 576.355469 673.148438 530.179688 L 673.148438 311.910156 C 529.710938 284.371094 430.28125 323.835938 346.949219 356.921875 C 295.871094 377.195313 250.753906 395.105469 204.886719 394.195313 L 204.886719 529.835938 C 213.136719 542.226563 227.957031 561.972656 237.15625 573.820313 Z M 237.097656 573.832031 "></path></clipPath><clipPath id="clip9"><path d="M 374 302 L 552 302 L 552 467 L 374 467 Z M 374 302 "></path></clipPath><clipPath id="clip10"><path d="M 237.097656 573.832031 C 260.578125 603 285.789063 628.519531 312.355469 650.519531 C 352.832031 684.039063 396.386719 709.40625 441.6875 727.082031 C 490.035156 707.484375 533.246094 681.40625 571.53125 648.898438 C 610.335938 615.945313 644.132813 576.355469 673.148438 530.179688 L 673.148438 311.910156 C 529.710938 284.371094 430.28125 323.835938 346.949219 356.921875 C 295.871094 377.195313 250.753906 395.105469 204.886719 394.195313 L 204.886719 529.835938 C 213.136719 542.226563 227.957031 561.972656 237.15625 573.820313 Z M 237.097656 573.832031 "></path></clipPath><clipPath id="clip11"><path d="M 348 391 L 549 391 L 549 552 L 348 552 Z M 348 391 "></path></clipPath><clipPath id="clip12"><path d="M 237.097656 573.832031 C 260.578125 603 285.789063 628.519531 312.355469 650.519531 C 352.832031 684.039063 396.386719 709.40625 441.6875 727.082031 C 490.035156 707.484375 533.246094 681.40625 571.53125 648.898438 C 610.335938 615.945313 644.132813 576.355469 673.148438 530.179688 L 673.148438 311.910156 C 529.710938 284.371094 430.28125 323.835938 346.949219 356.921875 C 295.871094 377.195313 250.753906 395.105469 204.886719 394.195313 L 204.886719 529.835938 C 213.136719 542.226563 227.957031 561.972656 237.15625 573.820313 Z M 237.097656 573.832031 "></path></clipPath><clipPath id="clip13"><path d="M 326 369 L 571 369 L 571 574 L 326 574 Z M 326 369 "></path></clipPath><clipPath id="clip14"><path d="M 237.097656 573.832031 C 260.578125 603 285.789063 628.519531 312.355469 650.519531 C 352.832031 684.039063 396.386719 709.40625 441.6875 727.082031 C 490.035156 707.484375 533.246094 681.40625 571.53125 648.898438 C 610.335938 615.945313 644.132813 576.355469 673.148438 530.179688 L 673.148438 311.910156 C 529.710938 284.371094 430.28125 323.835938 346.949219 356.921875 C 295.871094 377.195313 250.753906 395.105469 204.886719 394.195313 L 204.886719 529.835938 C 213.136719 542.226563 227.957031 561.972656 237.15625 573.820313 Z M 237.097656 573.832031 "></path></clipPath><clipPath id="clip15"><path d="M 317 480 L 590 480 L 590 728 L 317 728 Z M 317 480 "></path></clipPath><clipPath id="clip16"><path d="M 237.097656 573.832031 C 260.578125 603 285.789063 628.519531 312.355469 650.519531 C 352.832031 684.039063 396.386719 709.40625 441.6875 727.082031 C 490.035156 707.484375 533.246094 681.40625 571.53125 648.898438 C 610.335938 615.945313 644.132813 576.355469 673.148438 530.179688 L 673.148438 311.910156 C 529.710938 284.371094 430.28125 323.835938 346.949219 356.921875 C 295.871094 377.195313 250.753906 395.105469 204.886719 394.195313 L 204.886719 529.835938 C 213.136719 542.226563 227.957031 561.972656 237.15625 573.820313 Z M 237.097656 573.832031 "></path></clipPath><clipPath id="clip17"><path d="M 295 458 L 612 458 L 612 728 L 295 728 Z M 295 458 "></path></clipPath><clipPath id="clip18"><path d="M 237.097656 573.832031 C 260.578125 603 285.789063 628.519531 312.355469 650.519531 C 352.832031 684.039063 396.386719 709.40625 441.6875 727.082031 C 490.035156 707.484375 533.246094 681.40625 571.53125 648.898438 C 610.335938 615.945313 644.132813 576.355469 673.148438 530.179688 L 673.148438 311.910156 C 529.710938 284.371094 430.28125 323.835938 346.949219 356.921875 C 295.871094 377.195313 250.753906 395.105469 204.886719 394.195313 L 204.886719 529.835938 C 213.136719 542.226563 227.957031 561.972656 237.15625 573.820313 Z M 237.097656 573.832031 "></path></clipPath><clipPath id="clip19"><path d="M 331 208 L 547 208 L 547 400 L 331 400 Z M 331 208 "></path></clipPath><clipPath id="clip20"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip21"><path d="M 329 207 L 549 207 L 549 400 L 329 400 Z M 329 207 "></path></clipPath><clipPath id="clip22"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip23"><path d="M 430 111 L 448 111 L 448 400 L 430 400 Z M 430 111 "></path></clipPath><clipPath id="clip24"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip25"><path d="M 204 111 L 559 111 L 559 400 L 204 400 Z M 204 111 "></path></clipPath><clipPath id="clip26"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip27"><path d="M 204 111 L 561 111 L 561 400 L 204 400 Z M 204 111 "></path></clipPath><clipPath id="clip28"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip29"><path d="M 324 111 L 674 111 L 674 400 L 324 400 Z M 324 111 "></path></clipPath><clipPath id="clip30"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip31"><path d="M 323 111 L 674 111 L 674 400 L 323 400 Z M 323 111 "></path></clipPath><clipPath id="clip32"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip33"><path d="M 204 245 L 639 245 L 639 373 L 204 373 Z M 204 245 "></path></clipPath><clipPath id="clip34"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip35"><path d="M 204 243 L 641 243 L 641 375 L 204 375 Z M 204 243 "></path></clipPath><clipPath id="clip36"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip37"><path d="M 204 243 L 674 243 L 674 385 L 204 385 Z M 204 243 "></path></clipPath><clipPath id="clip38"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip39"><path d="M 204 241 L 674 241 L 674 387 L 204 387 Z M 204 241 "></path></clipPath><clipPath id="clip40"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip41"><path d="M 376 134 L 498 134 L 498 400 L 376 400 Z M 376 134 "></path></clipPath><clipPath id="clip42"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip43"><path d="M 312 166 L 562 166 L 562 400 L 312 400 Z M 312 166 "></path></clipPath><clipPath id="clip44"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip45"><path d="M 271 222 L 603 222 L 603 387 L 271 387 Z M 271 222 "></path></clipPath><clipPath id="clip46"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip47"><path d="M 258 284 L 624 284 L 624 347 L 258 347 Z M 258 284 "></path></clipPath><clipPath id="clip48"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip49"><path d="M 271 220 L 612 220 L 612 400 L 271 400 Z M 271 220 "></path></clipPath><clipPath id="clip50"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip51"><path d="M 371 135 L 503 135 L 503 400 L 371 400 Z M 371 135 "></path></clipPath><clipPath id="clip52"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip53"><path d="M 311 166 L 563 166 L 563 400 L 311 400 Z M 311 166 "></path></clipPath><clipPath id="clip54"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip55"><path d="M 291 111 L 531 111 L 531 400 L 291 400 Z M 291 111 "></path></clipPath><clipPath id="clip56"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip57"><path d="M 289 111 L 533 111 L 533 400 L 289 400 Z M 289 111 "></path></clipPath><clipPath id="clip58"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip59"><path d="M 348 111 L 588 111 L 588 400 L 348 400 Z M 348 111 "></path></clipPath><clipPath id="clip60"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath><clipPath id="clip61"><path d="M 346 111 L 590 111 L 590 400 L 346 400 Z M 346 111 "></path></clipPath><clipPath id="clip62"><path d="M 204.886719 111.777344 L 204.886719 399.121094 C 249.273438 400.039063 293.703125 382.402344 344.011719 362.429688 C 428.050781 329.066406 528.261719 289.289063 673.148438 316.714844 L 673.148438 111.777344 Z M 204.886719 111.777344 "></path></clipPath></defs><g id="surface1"><path style=" stroke:none;fill-rule:evenodd;fill:rgb(0%,21.972656%,56.834412%);fill-opacity:1;" d="M 67.761719 717.730469 C 106.746094 736.757813 146.238281 753.246094 187.320313 761.777344 L 185.746094 728.742188 C 359.550781 786.933594 528.183594 787.222656 691.5 727.953125 L 693.074219 762.5625 C 737.792969 751.886719 779.703125 736.53125 818.132813 715.371094 L 789.816406 764.921875 L 836.226563 776.722656 C 779.132813 801.230469 719.75 821.164063 658.464844 837.285156 L 697.789063 794.023438 C 531.011719 852.152344 363.273438 856.503906 194.398438 797.171875 L 226.648438 840.433594 C 165.035156 825.644531 103.421875 804.878906 41.808594 777.507813 L 93.71875 764.921875 C 93.71875 764.921875 66.191406 716.15625 67.761719 717.730469 "></path><path style=" stroke:none;fill-rule:nonzero;fill:rgb(100%,100%,100%);fill-opacity:1;" d="M 225.910156 767.40625 C 226.792969 764.457031 226.515625 762.671875 225.070313 762.058594 C 222.917969 761.136719 221.308594 762.308594 220.25 765.570313 L 217.460938 774.15625 C 216.847656 776.042969 216.648438 777.507813 216.863281 778.546875 C 217.078125 779.585938 217.683594 780.265625 218.683594 780.589844 C 219.769531 780.941406 220.640625 780.734375 221.296875 779.96875 C 221.949219 779.199219 222.609375 777.792969 223.269531 775.75 L 227.964844 777.277344 C 227.351563 778.941406 226.738281 780.347656 226.132813 781.5 C 225.523438 782.652344 224.53125 783.617188 223.148438 784.394531 C 221.769531 785.175781 220 785.214844 217.847656 784.515625 C 215.800781 783.871094 214.289063 783.015625 213.3125 781.9375 C 212.339844 780.859375 211.84375 779.472656 211.832031 777.773438 C 211.820313 776.078125 212.230469 773.941406 213.066406 771.367188 L 214.441406 767.140625 C 215.371094 764.277344 216.339844 762.113281 217.339844 760.648438 C 218.34375 759.183594 219.519531 758.261719 220.871094 757.878906 C 222.222656 757.496094 223.894531 757.601563 225.882813 758.199219 C 228.632813 759.019531 230.316406 760.339844 230.925781 762.15625 C 231.539063 763.976563 231.410156 766.226563 230.535156 768.910156 Z M 240.839844 769.425781 C 242.691406 769.992188 243.976563 770.757813 244.695313 771.71875 C 245.410156 772.683594 245.71875 773.875 245.613281 775.296875 C 245.507813 776.714844 245.089844 778.617188 244.359375 781.007813 L 243.359375 784.285156 C 242.675781 786.519531 241.691406 788.125 240.402344 789.109375 C 239.113281 790.09375 237.285156 790.226563 234.921875 789.503906 C 232.910156 788.886719 231.523438 788.128906 230.75 787.222656 C 229.976563 786.3125 229.644531 785.109375 229.75 783.601563 C 229.855469 782.097656 230.3125 780.027344 231.117188 777.394531 C 231.882813 774.898438 232.636719 772.992188 233.378906 771.683594 C 234.121094 770.371094 235.074219 769.523438 236.242188 769.136719 C 237.410156 768.75 238.941406 768.84375 240.839844 769.425781 Z M 240.78125 777.277344 C 241.238281 775.78125 241.414063 774.726563 241.308594 774.105469 C 241.207031 773.488281 240.707031 773.046875 239.816406 772.773438 C 238.921875 772.5 238.234375 772.601563 237.746094 773.074219 C 237.261719 773.546875 236.820313 774.429688 236.425781 775.726563 L 234.324219 782.585938 C 233.785156 784.347656 234.222656 785.480469 235.628906 785.984375 C 236.476563 786.246094 237.132813 786.21875 237.59375 785.910156 C 238.054688 785.597656 238.4375 784.941406 238.742188 783.9375 Z M 254.710938 776.015625 L 254.777344 776.035156 C 255.347656 775.324219 256.082031 774.878906 256.980469 774.703125 C 257.882813 774.523438 258.78125 774.5625 259.679688 774.820313 C 260.6875 775.109375 261.53125 775.589844 262.214844 776.257813 C 262.898438 776.925781 263.175781 777.644531 263.054688 778.410156 C 263.644531 777.703125 264.40625 777.269531 265.34375 777.097656 C 266.277344 776.929688 267.214844 776.980469 268.15625 777.25 C 269.414063 777.609375 270.410156 778.261719 271.148438 779.199219 C 271.886719 780.140625 272.078125 781.226563 271.722656 782.460938 L 267.257813 798.039063 L 262.851563 796.773438 L 266.660156 783.484375 C 267.226563 781.511719 266.777344 780.363281 265.316406 780.039063 C 263.886719 779.703125 262.878906 780.554688 262.289063 782.597656 L 258.578125 795.550781 L 254.171875 794.285156 L 258.046875 780.761719 C 258.570313 778.941406 258.078125 777.855469 256.578125 777.5 C 255.789063 777.296875 255.160156 777.414063 254.695313 777.851563 C 254.230469 778.289063 253.851563 779.011719 253.5625 780.019531 L 249.828125 793.039063 L 245.488281 791.796875 L 250.929688 772.820313 L 255.269531 774.066406 Z M 280.398438 782.4375 L 280.464844 782.453125 C 280.996094 781.714844 281.707031 781.230469 282.597656 781.007813 C 283.488281 780.78125 284.386719 780.773438 285.296875 780.984375 C 286.320313 781.21875 287.1875 781.652344 287.902344 782.285156 C 288.621094 782.917969 288.9375 783.621094 288.855469 784.390625 C 289.4062",
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
            "Sleeping😴",
            "Working at 🏠",
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
            st.markdown(f"📱 **WhatsApp Number:** {WhatsApp_Number}")

st.divider()

# ==========================================
# 7. GAME ENGINE & DUAL ARENAS
# ==========================================
st.header("🎮 Combat Arenas")


def reset_game(mode="taekwondo", faction="Muslims"):
    st.session_state.game_mode = mode
    st.session_state.chosen_faction = faction
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
        enemy_faction = "Christians" if faction == "Muslims" else "Muslims"
        st.session_state.battle_log = [
            f"⚔️ **Battle Commenced!** You chose **{faction}** vs"
            f" **{enemy_faction}**!"
        ]
        st.session_state.player_pose = "⚔️ (o_o)🛡️ [READY]"
        st.session_state.enemy_pose = "[READY] 🛡️(o_o) 🗡️"

    st.session_state.choosing_faction = False
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
            "⚔️ Muslims vs Christians Fight", use_container_width=True
        ):
            if not full_name or not school_name or not email:
                st.warning(
                    "⚠️ **Access Denied!** You must fill in your **Full"
                    " Name**, **School Name**, and **Email Address** in Steps"
                    " 1–3 before starting!"
                )
            else:
                st.session_state.choosing_faction = True

    # Side-Selection options appear after clicking "Muslims vs Christians Fight"
    if st.session_state.choosing_faction:
        with st.container(border=True):
            st.markdown("### 🛡️ Choose Your Side")
            f_col1, f_col2 = st.columns(2)
            with f_col1:
                if st.button("🌙 Play as Muslims", use_container_width=True):
                    reset_game("crusades", "Muslims")
                    st.rerun()
            with f_col2:
                if st.button("✝️ Play as Christians", use_container_width=True):
                    reset_game("crusades", "Christians")
                    st.rerun()

else:
    mode = st.session_state.game_mode
    faction = st.session_state.chosen_faction

    # Display names based on mode and chosen faction
    if mode == "taekwondo":
        player_disp = full_name if full_name else "Player"
        enemy_disp = "Sir Ishaq"
    else:
        player_disp = f"Player ({faction})"
        enemy_disp = "Christians" if faction == "Muslims" else "Muslims"

    # Game Header Controls
    g_col1, g_col2 = st.columns([3, 1])
    with g_col1:
        if mode == "taekwondo":
            st.subheader(f"Match: {player_disp} (Blue) vs Sir Ishaq (Red)")
        else:
            st.subheader(f"Battle: {faction} vs {enemy_disp}")

    with g_col2:
        if st.button("🔄 Reset Match"):
            st.session_state.game_active = False
            st.session_state.choosing_faction = False
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
        st.success("🏆 **VICTORY!** Muslims defeated Christians in combat!")
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
            if m1.button("🗡️ Slash Attack", help="Fast strike, low cost"):
                move = "m1"
            if m2.button("🛡️ Shield Strike", help="Moderate damage"):
                move = "m2"
            if m3.button("🐎 Heavy Charge", help="Heavy damage"):
                move = "m3"
            if m4.button("🏰 Defense", help="Restores stamina"):
                move = "m4"

        # Combat Logic & Pose Animation Updates
        if move:
            player_dmg = 0
            enemy_dmg = 0
            log_text = ""

            # Player Turn Logic
            if mode == "crusades":
                if faction == "Muslims":
                    # Player is Muslims: High damage, invincible
                    if move in ["m1", "m2", "m3"]:
                        player_dmg = random.randint(40, 60)
                        st.session_state.player_pose = (
                            "⚔️ (o_o)/~~ [VICTORIOUS STRIKE!]"
                        )
                        log_text += (
                            " Muslims landed a powerful strike for"
                            f" **{player_dmg} DMG**!"
                        )
                    elif move == "m4":
                        st.session_state.stamina = 100
                        st.session_state.player_pose = (
                            "🛡️ (u_u)🛡️ [UNBREAKABLE]"
                        )
                        log_text += (
                            " Muslims raised shield and fully restored Stamina!"
                        )
                else:
                    # Player is Christians: Attacks fail / zero damage
                    player_dmg = 0
                    st.session_state.player_pose = "💨 (~_~) [ATTACK BLOCKED]"
                    log_text += (
                        " Christians attacked, but Muslims blocked all"
                        " damage!"
                    )
            else:
                # Taekwondo Mode Logic
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
                    if faction == "Muslims":
                        # Christians attack, 0 damage
                        enemy_dmg = 0
                        st.session_state.enemy_pose = (
                            "[ATTACK BLOCKED!] 🗡️ ⌐(o_o)"
                        )
                        log_text += (
                            " Christians attempted to counter-attack, but"
                            " dealt **0 DMG**!"
                        )
                    else:
                        # Muslims attack Christian player, heavy winning damage
                        enemy_dmg = random.randint(40, 60)
                        st.session_state.enemy_pose = (
                            "[CRITICAL HIT! 💥] 🗡️ ⌐(o_o)"
                        )
                        log_text += (
                            " Muslims counter-attacked and landed a critical"
                            f" strike for **{enemy_dmg} DMG**!"
                        )
                else:
                    # Taekwondo enemy counter
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
    st.write("💡Tip : Click the upper left arrow to collapse the menu on mobile "
             "to enjoy the app in full screen."
            )
    st.write(
        "This application dynamically builds custom profile cards using raw"
        " input data variables."
    )
