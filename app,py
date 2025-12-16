import streamlit as st
import streamlit.components.v1 as components

# --- Function to load external files ---

def load_css(file_name):
    """Loads an external CSS file and injects it into the Streamlit app."""
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def load_js(file_name):
    """Loads an external JavaScript file and injects it into the Streamlit app."""
    with open(file_name) as f:
        # Note: st.markdown with script tags can have side effects and is generally discouraged
        # for complex JS. It's better for simple, self-contained scripts or links.
        # For complex JS, components.html is better (see next function).
        st.markdown(f'<script>{f.read()}</script>', unsafe_allow_html=True)

def load_html_component(file_name):
    """Loads an external HTML file within an iframe using components.html()."""
    with open(file_name) as f:
        # This approach uses an iframe, which is safer and better for complex components
        components.html(f.read(), height=300)

# --- Main App Logic ---

st.title("Project Using External Files")

# 1. Inject CSS from an external file
load_css("styles.css")

st.markdown("""
<div class="custom-box">
    <h2>Welcome to the App!</h2>
    <p>This box is styled using an external CSS file.</p>
</div>
""", unsafe_allow_html=True)

# 2. Inject JavaScript (simple inline approach for demonstration)
# For this example, we'll embed the JS inline within markdown for simplicity,
# but the load_js function above could be used too.
st.markdown('<script src="script.js"></script>', unsafe_allow_html=True)

# Add a Streamlit button that triggers the JS function via an HTML button
st.markdown('<button onclick="showAlert()">Click Me for JS Alert</button>', unsafe_allow_html=True)

st.write("---")

# 3. Example using components.html to render an external HTML snippet/file
# (We will use a simple inline string here for brevity, but you can pass a file path to st.html())
st.subheader("Using `st.html` (Iframe method)")

components.html("""
<!DOCTYPE html>
<html>
<body>
  <h3>This is an embedded HTML component (via iframe)</h3>
  <p>It's a completely separate environment from the main Streamlit page.</p>
</body>
</html>
""", height=200)
