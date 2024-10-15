import streamlit as st
import random

# Initialize session state variables for progress and current card
if 'current_card' not in st.session_state:
    st.session_state.current_card = 0
if 'show_answer' not in st.session_state:
    st.session_state.show_answer = False
if 'right' not in st.session_state:
    st.session_state.right = 0
if 'wrong' not in st.session_state:
    st.session_state.wrong = 0

# Flashcards data
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who wrote '1984'?", "answer": "George Orwell"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "What year did the Titanic sink?", "answer": "1912"},
]

# Shuffle the flashcards
random.shuffle(flashcards)

# Function to move to the next card
def next_card():
    st.session_state.current_card += 1
    if st.session_state.current_card >= len(flashcards):
        st.session_state.current_card = 0
    st.session_state.show_answer = False

# Current flashcard
current_flashcard = flashcards[st.session_state.current_card]

# Custom CSS for styling
st.markdown("""
    <style>
        .flashcard {
            border-radius: 10px;
            background-color: #f9f9f9;
            padding: 20px;
            text-align: center;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            font-size: 20px;
            color: #333;
        }
        .answer {
            color: #007BFF;
            font-weight: bold;
        }
        .stButton>button {
            border-radius: 5px;
            font-size: 16px;
            padding: 10px 20px;
        }
        .progress-bar {
            background-color: #28a745;
            border-radius: 10px;
            height: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("🧠 Flashcard Quiz App")
st.markdown("Test your knowledge with this interactive flashcard app. Answer the questions and track your progress!")

# Progress bar for cards
total_cards = len(flashcards)
progress = (st.session_state.current_card + 1) / total_cards
st.progress(progress)

# Display the flashcard
st.markdown(f"<div class='flashcard'>{current_flashcard['question']}</div>", unsafe_allow_html=True)

# Button to flip the card
if st.button("🔄 Flip to see the answer"):
    st.session_state.show_answer = True

# Show answer if flipped
if st.session_state.show_answer:
    st.markdown(f"<p class='answer'>Answer: {current_flashcard['answer']}</p>", unsafe_allow_html=True)

# Right/Wrong Buttons with icons
col1, col2 = st.columns(2)
with col1:
    if st.button("✅ Right"):
        st.session_state.right += 1
        next_card()

with col2:
    if st.button("❌ Wrong"):
        st.session_state.wrong += 1
        next_card()

# Display user progress
st.markdown("### Your Score")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Correct", value=st.session_state.right)
with col2:
    st.metric(label="Incorrect", value=st.session_state.wrong)

# Completion message
if progress == 1.0:
    st.success(f"🎉 You've completed all flashcards! Your final score: {st.session_state.right} right, {st.session_state.wrong} wrong.")
