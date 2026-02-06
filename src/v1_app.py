import streamlit as st

# CONFIG
st.set_page_config(page_title="Instacart Analytics", layout="wide")

# READ PAGE FROM URL
page = st.query_params.get("page", "HOME")

# LOAD CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# NAVBAR
nav1, nav2, nav3, nav4 = st.columns([4, 1, 1, 1])

with nav1:
    st.markdown('<div class="logo">🥕 instacart</div>', unsafe_allow_html=True)

with nav2:
    if st.button("HOME"):
        st.experimental_set_query_params(page="HOME")

with nav3:
    if st.button("LOGIN"):
        st.experimental_set_query_params(page="LOGIN")

with nav4:
    if st.button("ABOUT US"):
        st.experimental_set_query_params(page="ABOUT")

st.divider()

# HOME PAGE
if page == "HOME":

    # HERO
    st.markdown("""
    <div class="hero">
        <div class="hero-content">
            <h1>Turn raw grocery data into actionable insights</h1>
            <p>Using advanced data mining, we reveal what customers buy together</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <a href="?page=DEPARTMENTS" class="card-link">
            <div class="card-box">
                <img src="https://cdn-icons-png.flaticon.com/512/2921/2921822.png" width="120"/>
                <h3>Departments</h3>
                <p>Analyze customer behavior by department</p>
            </div>
        </a>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <a href="?page=AISLE" class="card-link">
            <div class="card-box">
                <img src="https://cdn-icons-png.flaticon.com/512/3081/3081559.png" width="120"/>
                <h3>Aisle</h3>
                <p>Explore product performance by aisle</p>
            </div>
        </a>
        """, unsafe_allow_html=True)

# OTHER PAGES
elif page == "DEPARTMENTS":
    st.header("🏬 Departments Page")

elif page == "AISLE":
    st.header("🛒 Aisle Page")

elif page == "LOGIN":
    st.header("🔐 Login")

elif page == "ABOUT":
    st.header("ℹ️ About Us")

else:
    st.header("Page not found")

# CHART SELECTOR SECTION
st.markdown("""
<div class="chart-selector">
    <p>Select the chart you want to explore from the list below</p>
</div>
""", unsafe_allow_html=True)

# Dropdown choice for number of charts to display
num_charts = st.selectbox(
    "Number of charts",
    options=[1, 2, 3, 4],
    label_visibility="collapsed"
)


#graphical analysis app

from data_loader import load_data
from features import build_rfm
from clustering import add_clusters
from plots import (
    boxplot_orders_by_cluster,
    users_per_cluster,
    orders_distribution,
    top_products_pie,
)

st.set_page_config(layout="wide")
st.title("📦 Instacart Growth Segmentation")

@st.cache_data
def load_all():
    df = load_data()
    rfm = build_rfm(df)
    rfm = add_clusters(rfm)
    return df, rfm

df, rfm = load_all()

# Display plots
st.subheader("🍎 Top 10 Products by Orders")
st.plotly_chart(top_products_pie(df, n=10), use_container_width=True)

st.subheader("📊 Order Frequency by Segment")
st.pyplot(boxplot_orders_by_cluster(rfm))

st.subheader("👥 Customer Distribution")
st.pyplot(users_per_cluster(rfm))

st.subheader("📈 Orders Distribution")
st.pyplot(orders_distribution(rfm))

