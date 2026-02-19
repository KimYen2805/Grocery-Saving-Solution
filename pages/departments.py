import streamlit as st
import pandas as pd

#SESSION STATE INITIALIZATION
def init_state():
    defaults = {
        "show_all": False,
        "submitted_departments": [],
        "show_bundle": False,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

# RENDER FUNCTION
def render_departments():
    init_state()

    df = pd.read_csv("data/departments.csv")
    departments = df["department"].dropna().astype(str).tolist()

    left, right = st.columns([1, 1.2], gap="large")

    # ================= LEFT PANEL =================
    with left:

        st.markdown('<div class="department-aisle-title">List of Department</div>', unsafe_allow_html=True)
        st.markdown('<div class="department-aisle-anchor"></div>', unsafe_allow_html=True)

        # Search and sorting controls
        c1, c2 = st.columns([3, 1])
        with c1:
            search = st.text_input("", placeholder="Search ...", label_visibility="collapsed")
        with c2:
            order = st.selectbox("", ["A → Z", "Z → A"], label_visibility="collapsed")

        #Filter department list
        filtered = [d for d in departments if search.lower() in d.lower()]
        filtered.sort(reverse=(order == "Z → A"))

        # Show only first 5 unless expanded 
        display_list = filtered if st.session_state.show_all else filtered[:5]

        selected = []

        # Checkbox list 
        for dep in display_list:
            key = f"dep_{dep}"
            checked = st.checkbox(dep.capitalize(), key=key)

            if checked:
                selected.append(dep)

        # Toggle full list 
        if len(filtered) > 5:
            if st.button("........", key="toggle_list"):
                st.session_state.show_all = not st.session_state.show_all
                st.rerun()

        # Submit button 
        st.markdown("<br>", unsafe_allow_html=True)

        btn_col1, btn_col2, btn_col3 = st.columns([1, 2, 1])
        with btn_col2:
            submit = st.button(
                "Submit",
                key="submit_departments",
                type="primary",
                use_container_width=True
            )

        # Save selection ONLY when submit pressed
        if submit:
            st.session_state.submitted_departments = selected.copy()
            st.session_state.show_bundle = True

    # ================= RIGHT PANEL =================
    with right:

        st.markdown('<div class="bundle-title">Bundle Recommendation</div>', unsafe_allow_html=True)
        st.markdown('<div class="bundle-anchor"></div>', unsafe_allow_html=True)

        # Mock recommendation data 
        recommend_map = {
            "beverages": ["Banana","Milk","Bread","Egg","Apple","Cheese","Rice","Yogurt"],
            "breakfast": ["Coffee","Sugar","Milk","Bread","Butter","Jam","Egg"],
            "alcohol": ["Soda","Ice","Lemon","Snack","Peanut","Chips"],
            "bakery": ["Butter","Milk","Jam","Egg","Flour"],
            "babies": ["Diaper","Wipes","Milk Powder","Baby Lotion"]
        }

        # Use only submitted departments (prevents rerun reset)
        selected = st.session_state.submitted_departments

        # Render recommendations 
        if st.session_state.show_bundle and selected:

            display_bundles = []

            for dept in selected:

                # Normalize key for matching dictionary
                dept_key = dept.strip().lower()
                items = recommend_map.get(dept_key, [])

                # Skip departments without recommendation
                if not items:
                    continue

                # Pretty display name
                pretty_dept = dept.title()

                bundle = [pretty_dept] + items
                display_bundles.append(bundle)

            # No recommendations found
            if not display_bundles:
                st.warning("No bundle recommendation found for selected department(s)")
                return

            # Render bundle rows 
            for bundle in display_bundles:

                html = '<div class="bundle-row">'

                for i, item in enumerate(bundle):

                    card_class = "bundle-card"

                    # First card = department context
                    if i == 0:
                        card_class += " bundle-dept"

                    # Second card = strongest recommendation
                    elif i == 1:
                        card_class += " best-item"

                    html += f'<div class="{card_class}">{item}</div>'

                html += '</div>'
                st.markdown(html, unsafe_allow_html=True)

        else:
            st.info("Select department(s) and click Submit")







