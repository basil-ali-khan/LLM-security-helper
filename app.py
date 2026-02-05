import streamlit as st
from groq import Groq

# --- App Configuration ---
st.set_page_config(
    page_title="LLM Security Helper",
    page_icon="🛡️",
    layout="wide"
)

# --- Sidebar: Security & Setup ---
with st.sidebar:
    st.header("🔐 Configuration")
    
    # Securely accept API Key
    api_key = st.text_input("Enter Groq API Key", type="password")
    
    st.info(
        "**Privacy Note:** Your key is used only for this session "
        "and is not stored permanently."
    )
    
    st.markdown("---")
    st.markdown("**Assignment:** LLM Security Helper")
    st.markdown("**Provider:** Groq (Llama 3)")

# --- Helper Function: Call Groq ---
def get_groq_response(prompt):
    if not api_key:
        st.error("Please enter your Groq API Key in the sidebar first.")
        return None
    
    try:
        # Initialize Groq Client
        client = Groq(api_key=api_key)
        
        with st.spinner("Analyzing with Llama 3..."):
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",  # Free tier friendly, high performance
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0, # Low temperature for factual security analysis
            )
            return completion.choices[0].message.content
            
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# --- Main App Interface ---
st.title("🛡️ LLM Security Helper App")
st.markdown("Automated security analysis using **Groq** and **Llama 3**.")

tab1, tab2 = st.tabs(["Part 1: Code Remediation", "Part 2: Threat Modeling (OWASP/ATLAS)"])

# ==========================================
# PART 1: Code -> Security Fixes
# ==========================================
with tab1:
    st.header("💻 Code Vulnerability Scanner")
    st.caption("Paste a code snippet to identify security flaws and get fixed code.")

    code_input = st.text_area("Input Code Snippet", height=200, placeholder="e.g., query = f'SELECT * FROM users WHERE name = {user_input}'")

    if st.button("Scan Code", key="btn_scan"):
        if code_input:
            prompt_p1 = f"""
            You are an expert Application Security Engineer. 
            Analyze the following code snippet for security vulnerabilities.
            
            Strict Requirements:
            1. Identify specific security vulnerabilities (e.g., SQL Injection, XSS, Hardcoded Secrets).
            2. Do NOT focus on general clean code or performance refactoring unless it impacts security.
            3. Provide the FIXED code block.
            4. Explain *why* the fix makes it secure.

            Code to analyze:
            ```
            {code_input}
            ```
            """
            
            result = get_groq_response(prompt_p1)
            if result:
                st.markdown("### 🔍 Analysis & Fixes")
                st.markdown(result)
        else:
            st.warning("Please enter some code to analyze.")

# ==========================================
# PART 2: Specs -> OWASP/ATLAS Mapping
# ==========================================
with tab2:
    st.header("📝 GenAI Threat Modeler")
    st.caption("Paste your Agentic App specs to map them against OWASP Top 10 for LLMs and MITRE ATLAS.")

    spec_input = st.text_area("App Specifications", height=200, placeholder="e.g., A chatbot that executes Python code based on user prompts to analyze CSV files.")

    if st.button("Analyze Specs", key="btn_specs"):
        if spec_input:
            prompt_p2 = f"""
            You are a Security Architect specializing in GenAI and LLM Agents.
            Analyze the following application specifications.

            Strict Requirements:
            1. Identify potential vulnerabilities based on the **OWASP Top 10 for LLM Applications**.
            2. Map these risks to the **MITRE ATLAS** (Adversarial Threat Landscape for Artificial-Intelligence Systems) framework tactics/techniques where applicable.
            3. Be specific, actionable, and clear. Use a table format if possible for the mapping.

            App Specifications:
            ```
            {spec_input}
            ```
            """
            
            result = get_groq_response(prompt_p2)
            if result:
                st.markdown("### 📋 Threat Model Report")
                st.markdown(result)
        else:
            st.warning("Please enter application specs.")