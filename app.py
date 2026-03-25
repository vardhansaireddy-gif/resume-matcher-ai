import sys
import os

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from agents.coordinator import Coordinator

# Page config (optional but nice)
st.set_page_config(page_title="AI Resume Screening", layout="centered")

st.title("🤖 AI Resume Screening & Skill Matching System")

st.write("Upload your resume and compare it with a job description.")

# File upload
uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

# Job description input
job_desc = st.text_area("📝 Enter Job Description")

# Button
if st.button("🚀 Analyze Resume"):
    if uploaded_file is not None and job_desc.strip() != "":
        try:
            coordinator = Coordinator()

            score, gaps, suggestions = coordinator.run(uploaded_file, job_desc)

            st.success("✅ Analysis Complete!")

            # Score
            st.subheader("📊 Match Score")
            st.metric(label="Similarity Score", value=f"{score:.2f}%")

            # Missing Skills
            st.subheader("⚠️ Missing Skills")
            if gaps:
                for skill in gaps:
                    st.write(f"- {skill}")
            else:
                st.write("No missing skills 🎉")

            # Suggestions
            st.subheader("💡 Recommendations")
            if suggestions:
                for s in suggestions:
                    st.write(f"- {s}")
            else:
                st.write("Your resume looks strong!")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

    else:
        st.warning("⚠️ Please upload a resume and enter a job description.")