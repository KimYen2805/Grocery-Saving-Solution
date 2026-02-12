import streamlit as st

from data_loader import load_data
from features import build_rfm
from clustering import add_clusters
from plots import (
    top_products_pie,
    boxplot_orders_by_cluster,
    users_per_cluster,
    orders_distribution,
)

@st.cache_data
def load_all():
    df = load_data()
    rfm = build_rfm(df)
    rfm = add_clusters(rfm)
    # return df, rfm
    return rfm


def render_home():

    # ======================
    # LOAD DATA
    # ======================
    # df, rfm = load_all()

    # ======================
    # HERO
    # ======================
    st.markdown("""
    <div class="hero">
        <div class="hero-content">
            <h1>Turn raw grocery data into actionable insights</h1>
            <p>Using advanced data mining, we reveal what customers buy together</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ======================
    # NAVIGATION CARDS
    # ======================
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

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ======================
    # CHART SELECTOR
    # ======================
    with st.container():
         st.markdown("""
    <div class="chart-selector">
        <p>Select the chart you want to explore from the list below</p>
    </div>
    """, unsafe_allow_html=True)

    chart_choice = st.selectbox(
        "",
        [
            "1 Top 10 Products",
            "2 Order Frequency by Segment",
            "3 Customer Distribution",
            "4 Orders Distribution",
        ],
        label_visibility="collapsed"
    )


    # ======================
    # CHART DISPLAY
    # ======================
    if chart_choice.startswith("1"):
        st.subheader("🍎 Top 10 Products")
        # st.plotly_chart(
        #     top_products_pie(df),
        #     use_container_width=True
        # )

    # elif chart_choice.startswith("2"):
    #     st.subheader("📊 Order Frequency by Segment")
    #     st.pyplot(
    #         boxplot_orders_by_cluster(rfm)
    #     )

    # elif chart_choice.startswith("3"):
    #     st.subheader("👥 Customer Distribution")
    #     st.pyplot(
    #         users_per_cluster(rfm)
    #     )

    # elif chart_choice.startswith("4"):
    #     st.subheader("📈 Orders Distribution")
    #     st.pyplot(
    #         orders_distribution(rfm)
    #     )
