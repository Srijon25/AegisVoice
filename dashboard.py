# AegisVoice: ui/dashboard.py - Streamlit GUI for cancel phrase verification and simulation

import streamlit as st
from aegisvoice.recognizer import CancelPhraseRecognizer
from aegisvoice.evaluator import PhraseEvaluator
from aegisvoice.simulator import ThreatSimulator
from aegisvoice.profiles import ProfileManager

st.set_page_config(page_title="AegisVoice Dashboard", layout="centered")
st.title("🛡️ AegisVoice Cancel Phrase Detection")

# Load profile manager and select profile
manager = ProfileManager()
profiles = manager.get_profiles()
selected = st.selectbox("Choose Profile", profiles)
phrases = manager.get_phrases(selected) if selected else []

# Display phrases
st.write("### Cancel Phrases:")
st.write(", ".join(phrases) if phrases else "No phrases found.")

# Initialize modules
recognizer = CancelPhraseRecognizer(cancel_phrases=phrases)
evaluator = PhraseEvaluator(cancel_phrases=phrases)
simulator = ThreatSimulator()

# Simulate threat event
if st.button("🚨 Simulate Threat Event"):
    result = simulator.simulate_threat_event()
    st.warning(f"{result['message']}")

# Start listening
if st.button("🎙️ Listen for Cancel Phrase"):
    with st.spinner("Listening..."):
        recognized_text, conf = recognizer.listen_and_recognize()
        triggered = evaluator.is_triggered(recognized_text)
        response = simulator.respond_to_cancel(triggered)
        st.success(f"Recognized: '{recognized_text}'")
        st.write(f"Confidence Score: {conf:.2f}")
        st.info(response)

# Profile editor
with st.expander("⚙️ Edit Profile"):
    new_phrase = st.text_input("Add New Phrase")
    if st.button("➕ Add Phrase"):
        if selected:
            manager.add_phrase_to_profile(selected, new_phrase)
            st.rerun()
    remove_phrase = st.selectbox("Remove Phrase", phrases)
    if st.button("❌ Remove Phrase"):
        if selected:
            manager.remove_phrase_from_profile(selected, remove_phrase)
            st.rerun()
