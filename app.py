import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key="API KEY")

sys_prompt = """You are a helpful AI Code Reviewer. 
Users will submit Python code, and you are expected to analyze it for common issues such as syntax errors, incorrect imports, and style violations.
Provide a detailed bug report and suggest corrected code. 
If the code is correct, confirm that no issues were found.
Always include a helpful statement at the end saying:  
"""

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

st.title("AI Code Analyzer ")

user_code = st.text_area(label="Enter your Python code", placeholder="Paste your Python code here...", height=300)

if st.button("Analyze Code"):
    if user_code.strip() == "":
        st.warning("Please enter some Python code before submitting.")
    else:
        try:
            response = model.generate_content(f"Review this Python code:\n\n{user_code}")
            st.subheader("Review Report For Code")
            st.write(response.text) 
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
