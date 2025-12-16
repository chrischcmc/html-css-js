import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from pathlib import Path

def load_file(path):
    return Path(path).read_text()

# Load HTML, CSS, JS
html = load_file("index.html")
css = load_file("styles.css")
js = load_file("script.js")

# Load CSV and convert to HTML
df = pd.read_csv("sample.csv")
table_html = df.to_html(index=False, escape=False)  # escape=False allows HTML styling

# Replace placeholders
html = html.replace("{{CSS}}", f"<style>{css}</style>")
html = html.replace("{{JS}}", f"<script>{js}</script>")
html = html.replace("{{TABLE}}", table_html)  # <-- important

# Render the final HTML inside iframe
components.html(html, height=400)

