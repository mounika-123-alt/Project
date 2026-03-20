import streamlit as st
from utils.clv import calculate_clv
from utils.rag import AdvancedRAG
from utils.chatbot import generate_response

st.set_page_config(page_title="CLV Chatbot", layout="wide")

st.title("💰 Customer Lifetime Value Chatbot (Offline AI)")

# Response Mode
mode = st.selectbox("Response Mode", ["Concise", "Detailed"])

# Sidebar CLV Calculator
st.sidebar.header("📊 CLV Calculator")

pf = st.sidebar.number_input("Purchase Frequency", value=1)
aov = st.sidebar.number_input("Average Order Value", value=100)
lifespan = st.sidebar.number_input("Customer Lifespan", value=1)

if st.sidebar.button("Calculate CLV"):
    clv, insight = calculate_clv(pf, aov, lifespan)
    st.sidebar.success(f"CLV = ₹{clv}")
    st.sidebar.info(insight)

# Initialize RAG
if "rag" not in st.session_state:
    st.session_state.rag = AdvancedRAG()

# Load Documents
if st.button("📄 Load PDF Documents"):
    try:
        st.session_state.rag.load_documents()
        st.success("Documents loaded successfully!")
    except Exception as e:
        st.error(f"Error loading documents: {e}")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Chat input
user_input = st.text_input("💬 Ask your question:")

if user_input:
    context = st.session_state.rag.query(user_input)

    response = generate_response(user_input, context, mode)

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# Display chat
for role, msg in st.session_state.history:
    if role == "You":
        st.markdown(f"**🧑 {role}:** {msg}")
    else:
        st.markdown(f"**🤖 {role}:** {msg}")