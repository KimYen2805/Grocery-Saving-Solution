import streamlit as st

# Render function for Page about us
def render_about():

    # Page title and subtitle
    st.markdown('<h1 class="about-title">🤝 About Grocery Saving Solution</h1>', unsafe_allow_html=True)
    st.markdown('<p class="about-subtitle">Turning Grocery Data Into Smart Savings</p>', unsafe_allow_html=True)

    st.markdown("---")

    # Our Vision
    st.header("💡 Our Vision")
    st.write("""
    Grocery Saving Solution is a data-driven platform designed to help customers 
    optimize their grocery spending through intelligent insights and analytics.

    Our goal is to transform raw grocery data into meaningful recommendations 
    that support smarter purchasing decisions.
    """)

    # What We Do
    st.header("📊 What We Do")
    st.write("""
    Using machine learning techniques and clustering analysis, we:
    - Analyze customer purchasing behavior
    - Identify spending patterns
    - Provide strategic insights for cost-saving opportunities
    - Support data-driven decision making
    """)

    st.markdown("---")

    # Meet Our Team
    st.markdown('<h2 class="team-title">👩‍💻 Meet Our Team</h2>', unsafe_allow_html=True)
    st.markdown('<p class="team-subtitle">We are a multidisciplinary team of Master Students from DSTI.</p>', unsafe_allow_html=True)

    # Team Members
    team = [
        {"name": "Nona Shamila SALLAY", "role": "Data Science", "img": "images/shamila.png"},
        {"name": "Dinh Duy TRAN", "role": "Software Engineering", "img": "images/duy.png"},
        {"name": "Viet Linh VU", "role": "Software Engineering", "img": "images/linh.png"},
        {"name": "Kim Yen LE", "role": "Data Analytics", "img": "images/kim.png"}, 
        {"name": "Myat Noe WAI", "role": "Data Analytics", "img": "images/nora.png"},
        {"name": "Doreen Chepkoech KOSKE", "role": "Data Analytics", "img": "images/doren.png"},
        {"name": "Leonardo Mariano HERNANDEZ ECHENIQUE", "role": "Data Analytics", "img": "images/leo.png"},
    ]

    # Display team members (3 per row)
    for i in range(0, len(team), 3):
        cols = st.columns(3)
        for idx, col in enumerate(cols):
            if i + idx < len(team):
                member = team[i + idx]
                with col:
                    st.markdown(f'<div class="team-card">', unsafe_allow_html=True)
                    st.image(member["img"], width=90)
                    st.markdown(f'<h3 class="team-name">{member["name"]}</h3>', unsafe_allow_html=True)
                    st.markdown(f'<p class="team-role">{member["role"]}</p>', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.success("Thank you for visiting Grocery Saving Solution 🚀")