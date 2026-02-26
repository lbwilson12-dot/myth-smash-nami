import streamlit as st
import random

st.set_page_config(page_title="Myth Smash", page_icon="💙")

# -----------------------------
# BRAND COLORS
# -----------------------------
NAMI_BLUE = "#FFFFFF"
LIGHT_BLUE = "#0c499c "
White = "FFFFFF"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {LIGHT_BLUE};
    }}
    h1 {{
        color: {NAMI_BLUE};
    }}
    .stButton>button {{
        background-color: {LIGHT_BLUE};
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# QUESTIONS
# -----------------------------
QUESTION_BANK = [
    {
        "question": "Only adults experience major depression.",
        "answer": "Myth",
        "explanation": "Depression affects people of all ages, including children and teens."
    },
    {
        "question": "You have to be in crisis to contact NAMI.",
        "answer": "Myth",
        "explanation": "NAMI provides education, resources, and peer support — not just crisis services."
    },
    {
        "question": "Peer support can reduce isolation.",
        "answer": "Fact",
        "explanation": "Peer support connects people with shared experiences and reduces stigma and isolation."
    },
    {
        "question": "Mental illness is rare.",
        "answer": "Myth",
        "explanation": "1 in 5 adults experience mental illness each year."
    },
    {
        "question": "A person with a mental health condition is usually more likely to be violent than anyone else in our population",
        "answer": "Myth",
        "explanation": "people with mental health conditions are not, as a group, more likely to be violent than the general population. In fact, they are over 10 times more likely to be victims of violent crime than perpetrators.",
    },
    {
        "question": "Women are 70% more likely than men to suffer from a Depressive Disorder",
        "answer": "Fact",
        "explanation": "This disparity is driven by a complex interaction of hormonal fluctuations, genetic vulnerability, and higher societal stressors.",
    
    },
]

# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "questions" not in st.session_state:
    st.session_state.questions = random.sample(QUESTION_BANK, len(QUESTION_BANK))
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.show_feedback = False
    st.session_state.selected_answer = None

# -----------------------------
# TITLE
# -----------------------------
st.title("💥 Myth Smash: NAMI Lane County Edition")
st.write("Test your knowledge. Smash stigma. Support mental health.")

# -----------------------------
# PROGRESS BAR
# -----------------------------
progress = st.session_state.index / len(st.session_state.questions)
st.progress(progress)

# -----------------------------
# GAME
# -----------------------------
if st.session_state.index < len(st.session_state.questions):

    q = st.session_state.questions[st.session_state.index]

    st.subheader("Statement:")
    st.write(q["question"])

    # FORM = SINGLE CLICK SUBMIT
    with st.form(key=f"form_{st.session_state.index}"):

        selected = st.radio(
            "Choose your answer:",
            ["Fact", "Myth"],
            key=f"radio_{st.session_state.index}"
        )

        submit = st.form_submit_button("Submit Answer")

        if submit:
            st.session_state.selected_answer = selected
            st.session_state.show_feedback = True

            if selected == q["answer"]:
                st.session_state.score += 1

    # FEEDBACK DISPLAY
    if st.session_state.show_feedback:

        if st.session_state.selected_answer == q["answer"]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Not quite! The correct answer is: {q['answer']}")

        st.info(q["explanation"])

        if st.button("Next Question"):
            st.session_state.index += 1
            st.session_state.show_feedback = False
            st.session_state.selected_answer = None
            st.rerun()

# -----------------------------
# GAME COMPLETE
# -----------------------------
else:
    st.balloons()
    st.subheader("🎉 Game Complete!")
    st.write(f"Your score: {st.session_state.score} / {len(st.session_state.questions)}")

    if st.session_state.score == len(st.session_state.questions):
        st.success("🔥 Mental Health Champion!")
    elif st.session_state.score >= len(st.session_state.questions) // 2:
        st.info("💙 Community Builder!")
    else:
        st.warning("🌱 Emerging Advocate!")

    st.markdown("---")

    # REGISTER BUTTON
    st.link_button(
        "💙 Register for NAMIWalks",
        "https://www.namiwalks.org/lanecounty" 
    )

    # SPONSOR BUTTON
    st.link_button(
        "🤝 Become a Sponsor",
        "https://forms.gle/rkfjprteYAynvR6e6" 
    )

    # SUBMIT SCORE & STAY CONNECTED
    st.link_button(
        "Submit Score & Stay Connected",
        f"https://docs.google.com/forms/d/e/1FAIpQLSdk_BFkywBWfGdR5M0UsEzVGgPRy7SlMBjAoQRbXpSPl0P7pA/viewform?usp=pp_url&entry.1110337880={st.session_state.score}"
    )

if st.button("Play Again"):
        st.session_state.questions = random.sample(QUESTION_BANK, len(QUESTION_BANK))
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.show_feedback = False
        st.session_state.selected_answer = None
        st.rerun()
score = st.session_state.score
