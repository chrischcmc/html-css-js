import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

def load_file(path):
    return Path(path).read_text()

css = load_file("styles.css")
js = load_file("script.js")

st.title("External CSS & JS (Streamlit-safe)")

# ✅ CSS can be injected into main DOM (safe)
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.markdown("""
<div class="custom-box">
  <h2>Styled by external CSS</h2>
  <p>This works safely.</p>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ✅ JS MUST live inside iframe
components.html(
    f"""
    <!DOCTYPE html>
    <html>
    <head>
      <style>{css}</style>
      <script>{js}</script>
    </head>
    <body>
      <button onclick="showAlert()">Click Me</button>
    </body>
    </html>
    """,
    height=120,
)
