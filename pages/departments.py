import streamlit as st
import pandas as pd


def render_departments():
    st.header("🏢 Department Page")

    df = pd.read_csv("data/departments.csv")
    departments = df["department"].dropna().unique().astype(str).tolist()

    col1, col2 = st.columns([1, 1.2])

    # ================= LEFT PANEL =================
    with col1:
       # st.markdown('<div class="department-panel">', unsafe_allow_html=True)

        st.markdown(
            '<div class="department-aisle-title">List of Department</div>',
            unsafe_allow_html=True
        )

        with st.form("department_form"):
            selected = []
            for dep in departments:
                if st.checkbox(dep.capitalize(), key=dep):
                    selected.append(dep)

            # submit button inside the form in the left panel
            submit = st.form_submit_button("Submit", use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # ================= RIGHT PANEL =================
    with col2:
        st.markdown('<div class="department-panel">', unsafe_allow_html=True)
        st.markdown(
            '<div class="department-aisle-title">Bundle Recommendation</div>',
            unsafe_allow_html=True
        )
#add 
        if submit and selected:
            st.success(f"Selected: {', '.join(selected)}")
        else:
            st.info("Select department(s) and click Submit")

        st.markdown('</div>', unsafe_allow_html=True)