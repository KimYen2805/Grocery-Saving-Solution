import streamlit as st
import pandas as pd


def render_aisle():
    st.header("🛒 Aisle Page")

    # Load aisle data
    df = pd.read_csv("data/aisles.csv")
    aisles = df["aisle"].tolist()

    col1, col2 = st.columns([1, 1.2])

    # ================= LEFT PANEL =================
    with col1:
       # st.markdown('<div class="department-panel">', unsafe_allow_html=True)

        st.markdown(
            '<div class="department-aisle-title">List of Aisles</div>',
            unsafe_allow_html=True
        )

        with st.form("department_form"):
            selected = []
            for aisle in aisles:
                if st.checkbox(aisle.capitalize(), key=aisle):
                    selected.append(aisle)

            # submit button inside the form in the left panel
            submit = st.form_submit_button("Submit", use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # ================= RIGHT PANEL =================
    with col2:
        st.markdown('<div class="department-panel">', unsafe_allow_html=True)
        st.markdown('<div class="department-aisle-title">Bundle Recommendation</div>', unsafe_allow_html=True)

        if submit and selected:
            st.success(f"Selected: {', '.join(selected)}")
        else:
            st.info("Select aisle(s) and click Submit")

        st.markdown('</div>', unsafe_allow_html=True)

