"""Full-width Streamlit host for the VerifyDesk demo."""
from base64 import b64encode
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
    padding: 0 !important;
}
[data-testid="stVerticalBlock"] { gap: 0 !important; }
[data-testid="stElementContainer"]:has(iframe[title="VerifyDesk supplier change verification demo"]),
[data-testid="stIframe"] {
    height: 100dvh !important;
    min-height: 480px;
}
iframe[title="VerifyDesk supplier change verification demo"] {
    display: block;
    width: 100% !important;
    height: 100dvh !important;
    min-height: 480px;
    border: 0 !important;
}
[data-testid="stHeader"] { display: none !important; }
</style>
""")
# Only embed this fixed project asset; never use user-uploaded HTML here.
assets = Path(__file__).parent
photo = b64encode((assets / "review-desk.webp").read_bytes()).decode("ascii")
page = (assets / "verifydesk.html").read_text(encoding="utf-8")
st.iframe(page.replace('src="review-desk.webp"', f'src="data:image/webp;base64,{photo}"', 1),
          height=1100, alt="VerifyDesk supplier change verification demo")


