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

# Flashcards data with 20 questions
flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who wrote '1984'?", "answer": "George Orwell"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "What year did the Titanic sink?", "answer": "1912"},
    {"question": "What is the smallest prime number?", "answer": "2"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the largest mammal?", "answer": "Blue Whale"},
    {"question": "Who discovered penicillin?", "answer": "Alexander Fleming"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
    {"question": "In which year did the Berlin Wall fall?", "answer": "1989"},
    {"question": "What is the main ingredient in guacamole?", "answer": "Avocado"},
    {"question": "What is the longest river in the world?", "answer": "Nile"},
    {"question": "What is the powerhouse of the cell?", "answer": "Mitochondria"},
    {"question": "Who was the first President of the United States?", "answer": "George Washington"},
    {"question": "What is the boiling point of water?", "answer": "100°C"},
    {"question": "What is the most spoken language in the world?", "answer": "Mandarin Chinese"},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
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
            background-color: #6a0dad;  /* Deep purple-blue */
            padding: 20px;
            text-align: center;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            font-size: 20px;
            color: #f9f9f9; /* Light color for contrast */
        }
        .answer {
            color: #00ff7f; /* Light green for the answer */
            font-weight: bold;
            margin-top: 20px;
        }
        .stButton>button {
            border-radius: 5px;
            font-size: 16px;
            padding: 10px 20px;
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

# Show answer if the card is flipped
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

# Display user score
st.markdown("### Your Score")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Correct", value=st.session_state.right)
with col2:
    st.metric(label="Incorrect", value=st.session_state.wrong)

# Completion message
if progress == 1.0:
    st.success(f"🎉 You've completed all flashcards! Your final score: {st.session_state.right} right, {st.session_state.wrong} wrong.")
