import streamlit as st
import pandas as pd
from resume_parser import extract_text_from_pdf
from matcher import rank_resumes
from time import sleep

# Set Streamlit config
st.set_page_config(page_title="AI Resume Screener", layout="wide")

st.title("📄 AI-Powered Resume Screening Tool")
st.markdown("To make hiring smarter and faster🕚")

# Sidebar instructions
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/942/942748.png", width=100)
    st.title("🔍 Resume Screener App")
    st.markdown("Welcome to the AI-powered resume screening dashboard! 🚀")
    st.markdown("Upload multiple resumes in PDF format and provide a job description this app will analyze and rank resumes based on your provided job relevance.")
    st.markdown("---")
    st.markdown("🔧 Built with Python, NLP, spaCy & Streamlit.")

# Job description input
st.markdown("### 📝 Job Description")
job_desc = st.text_area("Write the job description here:", height=200)

# Resume uploads
st.markdown("### 📤 Upload Resumes (PDFs only)")
uploaded_files = st.file_uploader("Upload multiple resume PDFs:", type=["pdf"], accept_multiple_files=True)

# Main processing
if st.button("🚀 Rank Resumes"):
    if not uploaded_files or not job_desc.strip():
        st.warning("Please upload at least one resume and provide a job description.")
    else:
        resume_texts = []
        filenames = []
        progress = st.progress(0, text="⏳ Processing Resumes...")
        status_text = st.empty()

        for i, file in enumerate(uploaded_files):
            try:
                status_text.text(f"🔍 Processing: {file.name}")
                text = extract_text_from_pdf(file)
                if not text.strip():
                    st.warning(f"⚠️ {file.name} seems to be blank.")
                    continue
                resume_texts.append(text)
                filenames.append(file.name)
            except Exception as e:
                st.error(f"❌ Could not read {file.name}: {e}")
            progress.progress((i + 1) / len(uploaded_files))

        if resume_texts:
            scores = rank_resumes(resume_texts, job_desc)
            df = pd.DataFrame({
                "Candidate": filenames,
                "Match Score": scores
            }).sort_values(by="Match Score", ascending=False).reset_index(drop=True)

            st.success(f"✅ Done! {len(filenames)} resume(s) ranked.")
            st.dataframe(df, use_container_width=True)

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download CSV", data=csv, file_name="ranked_resumes.csv", mime="text/csv")
        else:
            st.error("No valid resumes processed.")
