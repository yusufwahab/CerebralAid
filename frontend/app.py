import streamlit as st

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="AI4StrokeCare",
    layout="centered"
)

# -------------------------------
# Title & Description
# -------------------------------
st.title("AI4StrokeCare – Early Stroke Risk Screening")

st.warning(
    "⚠️ **Disclaimer:** This tool is for early stroke risk screening and awareness only. "
    "It does NOT provide medical diagnosis. "
    "If symptoms are present, seek immediate medical care."
)

st.markdown("---")

# -------------------------------
# User Inputs
# -------------------------------
st.subheader("Patient Information")

age = st.number_input("Age", min_value=0, max_value=120, value=50)

facial_asymmetry = st.slider(
    "Facial asymmetry severity",
    min_value=0,
    max_value=10,
    value=0,
    help="0 = none, 10 = severe drooping"
)

arm_weakness = st.checkbox("Arm weakness present")
speech_difficulty = st.checkbox("Speech difficulty present")

time_since_onset = st.number_input(
    "Time since symptom onset (hours)",
    min_value=0.0,
    max_value=72.0,
    value=1.0
)

st.markdown("---")

# -------------------------------
# Risk Assessment Logic (MVP)
# -------------------------------
def assess_risk(age, facial, arm, speech, time_hours):
    score = 0

    if facial >= 5:
        score += 2
    elif facial > 0:
        score += 1

    if arm:
        score += 2

    if speech:
        score += 2

    if age >= 60:
        score += 1

    if time_hours <= 4.5:
        score += 1  # critical intervention window

    if score >= 6:
        return "High", 0.85, "Seek immediate emergency medical care."
    elif score >= 3:
        return "Moderate", 0.65, "Consult a healthcare professional as soon as possible."
    else:
        return "Low", 0.35, "Monitor symptoms and seek care if conditions worsen."

# -------------------------------
# Run Assessment
# -------------------------------
if st.button("Run Risk Assessment"):
    risk, confidence, recommendation = assess_risk(
        age,
        facial_asymmetry,
        arm_weakness,
        speech_difficulty,
        time_since_onset
    )

    st.subheader("Assessment Result")

    if risk == "High":
        st.error(f"🚨 **Risk Level: {risk}**")
    elif risk == "Moderate":
        st.warning(f"⚠️ **Risk Level: {risk}**")
    else:
        st.success(f"✅ **Risk Level: {risk}**")

    st.write(f"**Confidence Score:** {confidence}")
    st.write(f"**Recommendation:** {recommendation}")

    st.caption(
        "This assessment is generated using prototype AI logic. "
        "In production, models will be trained and deployed using Microsoft Azure AI services."
    )
