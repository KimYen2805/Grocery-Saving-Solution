import streamlit as st
from pages.home import render_home
from pages.departments import render_departments
from pages.aisle import render_aisle
from pages.dashboard import render_dashboard
from pages.about_us import render_about 

#  Page configuration
st.set_page_config(page_title="Instacart Analytics", layout="wide")

#Hide Streamlit default menu and footer
st.markdown("""
<style>
section[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# Router
page = st.query_params.get("page", "HOME")

# Load CSS
with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Navigation bar with active state
def active(p):
    return "active" if page == p else ""
# Custom navigation bar
st.markdown(f"""
<div class="navbar">
    <a href="?page=HOME" class="logo">🥕 instacart</a>

<div class="menu">
    <a href="?page=HOME" class="{active('HOME')}">Home</a>
    <a href="?page=ABOUT" class="{active('ABOUT')}">About Us</a>
</div>
</div>
""", unsafe_allow_html=True)

# Page routing logic 
if page == "HOME":
    render_home()

elif page == "DEPARTMENTS":
    render_departments()

elif page == "AISLE":
    render_aisle()

elif page == "DASHBOARD":
    render_dashboard()

elif page == "ABOUT":
    render_about()

else:
    st.header("Page not found")

