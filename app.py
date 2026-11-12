"""Full-width Streamlit host for the VerifyDesk demo."""
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="VerifyDesk", page_icon="🛡️", layout="wide", initial_sidebar_state="collapsed")
# Presentation overrides for the pinned Streamlit version.
# Retain the Streamlit toolbar while removing the outer dark frame and padding.
st.html("""
<style>
.stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
    background: #f1f5f5 !important;
    color: #172c36 !important;
}
[data-testid="stMainBlockContainer"] {
    max-width: 100% !important;
    padding: 3.5rem 0 0 !important;
}
[data-testid="stVerticalBlock"] { gap: 0 !important; }
[data-testid="stElementContainer"]:has(iframe[title="VerifyDesk supplier change verification demo"]),
[data-testid="stIframe"] {
    height: calc(100dvh - 3.5rem) !important;
    min-height: 480px;
}
iframe[title="VerifyDesk supplier change verification demo"] {
    display: block;
    width: 100% !important;
    height: calc(100dvh - 3.5rem) !important;
    min-height: 480px;
    border: 0 !important;
}
</style>
""")
# Only embed this fixed project asset; never use user-uploaded HTML here.
st.iframe(Path(__file__).with_name("verifydesk.html"), height=1100,
          alt="VerifyDesk supplier change verification demo")

