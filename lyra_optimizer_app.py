
import streamlit as st

# ----- Optimization Functions -----

def core_optimize(prompt, platform):
    return f"[{platform}-OPTIMIZED]: {prompt.strip().capitalize()} (structured and clarified)."

def comprehensive_optimize(prompt, answers, platform):
    refined = f"{prompt.strip().capitalize()} — with focus on {answers[0]}, tone: {answers[1]}, audience: {answers[2]}"
    return f"[{platform}-OPTIMIZED/ADVANCED]: {refined}"

# ----- Streamlit UI -----

st.set_page_config(page_title="Lyra Prompt Optimizer", layout="centered")

st.title("🤖 Lyra - AI Prompt Optimizer")

st.markdown("""
Welcome! I'm **Lyra**, your AI prompt optimizer. I transform vague requests into precise, effective prompts that unlock the full power of ChatGPT, Claude, Gemini, and more.

---

### What I need to know:
- **Target AI** (ChatGPT, Claude, Gemini, or Other)
- **Prompt Style**:  
  - **DETAIL** → Full enhancement (with clarifying questions)  
  - **BASIC** → Quick improvements

Just enter your rough prompt and I’ll handle the optimization!
""")

# Inputs
target_ai = st.selectbox("🎯 Target AI", ["ChatGPT", "Claude", "Gemini", "Other"])
mode = st.radio("🛠️ Prompt Style", ["DETAIL", "BASIC"])
rough_prompt = st.text_area("📝 Your Rough Prompt", height=150)

if st.button("🚀 Optimize Prompt"):
    if not rough_prompt.strip():
        st.warning("Please enter a rough prompt.")
    elif mode == "BASIC":
        optimized = core_optimize(rough_prompt, target_ai)
        st.subheader("✅ Your Optimized Prompt:")
        st.code(optimized, language="markdown")
        st.markdown("**What Changed:** Applied structure and clarity for improved AI response.")
    else:
        # DETAIL mode - ask questions
        st.subheader("📋 Answer a few quick questions:")
        q1 = st.text_input("1. What’s the specific output you're hoping for?")
        q2 = st.text_input("2. Any tone, formatting, or length preferences?")
        q3 = st.text_input("3. Who is the audience or end-user?")

        if q1 and q2 and q3:
            optimized = comprehensive_optimize(rough_prompt, [q1, q2, q3], target_ai)
            st.subheader("✅ Your Optimized Prompt:")
            st.code(optimized, language="markdown")
            st.markdown("""
**Key Improvements:** Targeted structure, added specificity, audience-tuned  
**Techniques Applied:** Few-shot reasoning, context layering, tone alignment  
**Pro Tip:** Try adding example outputs to get even better performance!
            """)
        else:
            st.info("Please answer all clarification questions above.")
