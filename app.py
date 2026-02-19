import streamlit as st
from pages.home import render_home
from pages.departments import render_departments
from pages.aisle import render_aisle

# CONFIG
st.set_page_config(page_title="Instacart Analytics", layout="wide")

#HIDE STREAMLIT STYLE
st.markdown("""
<style>
section[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# READ PAGE FROM URL
page = st.query_params.get("page", "HOME")

# LOAD CSS
with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# NAVBAR
def active(p):
    return "active" if page == p else ""

# ===== NAVBAR =====
st.markdown(f"""
<div class="navbar">
    <a href="?page=HOME" class="logo">🥕 instacart</a>

<div class="menu">
    <a href="?page=HOME" class="{active('HOME')}">Home</a>
    <a href="?page=ABOUT" class="{active('ABOUT')}">About Us</a>
</div>
</div>
""", unsafe_allow_html=True)

#st.divider()


# ROUTER
if page == "HOME":
    render_home()

elif page == "DEPARTMENTS":
    render_departments()

elif page == "AISLE":
    render_aisle()

elif page == "ABOUT":
    st.header("ℹ️ About Us")

else:
    st.header("Page not found")

