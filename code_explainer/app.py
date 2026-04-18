import streamlit as st
from chain import explain_code

st.set_page_config(page_title="Code Explainer", page_icon="🔍", layout="wide")
st.title("Code Explainer")
st.caption("Paste any code — get a plain-English breakdown instantly.")

col1, col2 = st.columns(2)

with col1:
    language = st.selectbox(
        "Language",
        ["Python", "JavaScript", "TypeScript", "Java", "C++", "Go", "Rust", "SQL", "Other"]
    )
    code_input = st.text_area(
        "Paste your code here",
        height=350,
        placeholder="def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)"
    )
    explain_btn = st.button("Explain this code", type="primary", use_container_width=True)

with col2:
    if explain_btn:
        if not code_input.strip():
            st.warning("Please paste some code first.")
        else:
            with st.spinner("Analyzing your code..."):
                explanation = explain_code(code_input, language)
            st.markdown(explanation)
    else:
        st.info("Your explanation will appear here.")