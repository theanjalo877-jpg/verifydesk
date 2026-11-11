"""Streamlit host for the self-contained VerifyDesk portfolio demo."""
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="VerifyDesk | Anjalo Theophine Wilson", page_icon="🛡️", layout="wide", initial_sidebar_state="collapsed")
# This is a fixed, reviewed application asset. Never use uploaded or user-provided HTML here.
st.iframe(Path(__file__).with_name("verifydesk.html"), height=1100, alt="VerifyDesk supplier change verification demo")
