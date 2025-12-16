import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

def load(path):
    return Path(path).read_text()

html = load("index.html")
css = load("styles.css")
js = load("script.js")

html = html.replace("{{CSS}}", f"<style>{css}</style>")
html = html.replace("{{JS}}", f"<script>{js}</script>")

components.html(html, height=200)
