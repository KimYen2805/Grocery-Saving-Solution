import streamlit as st
import pandas as pd

#SESSION STATE INITIALIZATION 
def init_state():
    defaults = {
        "aisle_show_all": False,
        "submitted_aisles": [],
        "show_aisle_bundle": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

# RENDER FUNCTION
def render_aisle():

    init_state()

    df = pd.read_csv("data/aisles.csv")
    aisles = df["aisle"].dropna().astype(str).tolist()

    left, right = st.columns([1, 1.2], gap="large")

    # ================= LEFT PANEL =================
    with left:

        st.markdown('<div class="department-aisle-title">List of Aisles</div>', unsafe_allow_html=True)
        st.markdown('<div class="department-aisle-anchor"></div>', unsafe_allow_html=True)

        # Search + Sort
        c1, c2 = st.columns([3,1])
        with c1:
            search = st.text_input("", placeholder="Search ...", label_visibility="collapsed", key="aisle_search")
        with c2:
            order = st.selectbox("", ["A → Z", "Z → A"], label_visibility="collapsed", key="aisle_sort")

        filtered = [a for a in aisles if search.lower() in a.lower()]
        filtered.sort(reverse=(order == "Z → A"))

        display_list = filtered if st.session_state.aisle_show_all else filtered[:5]

        selected = []

        # Checkbox list 
        for aisle in display_list:
            key = f"aisle_{aisle}"
            if st.checkbox(aisle.capitalize(), key=key):
                selected.append(aisle)

        # Expand list
        if len(filtered) > 5:
            if st.button("........", key="toggle_aisle_list"):
                st.session_state.aisle_show_all = not st.session_state.aisle_show_all
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        # Submit
        btn_col1, btn_col2, btn_col3 = st.columns([1,2,1])
        with btn_col2:
            submit = st.button(
                "Submit",
                key="submit_aisles",
                type="primary",
                use_container_width=True
            )

        if submit:
            st.session_state.submitted_aisles = selected.copy()
            st.session_state.show_aisle_bundle = True

    # ================= RIGHT PANEL =================
    with right:

        st.markdown('<div class="bundle-title">Bundle Recommendation</div>', unsafe_allow_html=True)
        st.markdown('<div class="bundle-anchor"></div>', unsafe_allow_html=True)

        # Mock recommendation dataset
        aisle_recommend_map = {
            "asian foods": ["Tomato","Onion","Garlic","Potato","Carrot"],
            "baby accessories": ["Banana","Apple","Orange","Grapes"],
            "air fresheners candles": ["Cereal","Coffee","Cookies","Chocolate"],
            "baby bath body care": ["Butter","Jam","Egg","Cheese"],
            "baby food formula": ["Soda","Dip Sauce","Peanut","Beer"]
        }

        selected = st.session_state.submitted_aisles

        if st.session_state.show_aisle_bundle and selected:

            display_bundles = []

            for aisle in selected:
                key = aisle.strip().lower()
                items = aisle_recommend_map.get(key, [])

                if not items:
                    continue

                pretty = aisle.title()
                bundle = [pretty] + items
                display_bundles.append(bundle)

            if not display_bundles:
                st.warning("No bundle recommendation found for selected aisle(s)")
                return

            # Render
            for bundle in display_bundles:

                html = '<div class="bundle-row">'

                for i, item in enumerate(bundle):

                    card_class = "bundle-card"

                    if i == 0:
                        card_class += " bundle-dept"

                    elif i == 1:
                        card_class += " best-item"

                    html += f'<div class="{card_class}">{item}</div>'

                html += '</div>'
                st.markdown(html, unsafe_allow_html=True)

        else:
            st.info("Select aisle(s) and click Submit")


