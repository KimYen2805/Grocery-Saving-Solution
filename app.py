import streamlit as st
from pages.home import render_home
from pages.departments import render_departments
from pages.aisle import render_aisle

# ======================
# CONFIG
# ======================
st.set_page_config(page_title="Instacart Analytics", layout="wide")

# READ PAGE FROM URL
page = st.query_params.get("page", "HOME")

# LOAD CSS
with open("css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ======================
# NAVBAR
# ======================
nav1, nav2, nav3, nav4 = st.columns([4, 1, 1, 1])

with nav1:
    with nav1:  
        st.markdown(
        """
        <a href="?page=HOME" class="logo-link">
            <div class="logo">🥕 instacart</div>
        </a>
        """,
        unsafe_allow_html=True
    )
       

with nav2:
    if st.button("HOME"):
        st.query_params["page"] = "HOME"

with nav3:
    if st.button("LOGIN"):
        st.query_params["page"] = "LOGIN"

with nav4:
    if st.button("ABOUT US"):
        st.query_params["page"] = "ABOUT"

st.divider()

# ======================
# ROUTER
# ======================
if page == "HOME":
    render_home()

elif page == "DEPARTMENTS":
    render_departments()

elif page == "AISLE":
    render_aisle()

elif page == "LOGIN":
    st.header("🔐 Login")

elif page == "ABOUT":
    st.header("ℹ️ About Us")

else:
    st.header("Page not found")

