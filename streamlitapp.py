import streamlit as st
from menupages import homepage, educition, experience, resume, concat
from st_ant_menu import st_ant_menu

import base64

with open("static/image.png", "rb") as f:
    base64_str = str(base64.b64encode(f.read())).strip("b'").strip("'")

st.set_page_config(page_title=f"Personal resume site", layout="wide")

menu_data = [
    {
        "label": "<b>Home Page</b>",
        "key": "1",
        "icon": "fa-solid fa-drivers-license-o"
    },
    {
        "type": "divider"
    },
    {
        "label": "<b>Education Page</b>",
        "key": "2",
        "icon": "fa-solid fa-institution"
    },
    {
        "type": "divider"
    },
    {
        "label": "<b>Experience Page</b>",
        "key": "3",
        "icon": "fa-solid fa-book"
    },
    {
        "type": "divider"
    },
    {
        "label": "<b>Resume Page</b>",
        "key": "4",
        "icon": "fa-solid fa-cube"
    },
    {
        "type": "divider"
    },
    {
        "label": "<b>Contact Page</b>",
        "key": "5",
        "icon": "fa-solid fa-commenting-o"
    }
]

def display_footer():
    """Display a consistent footer across all pages"""
    footer = """
    <div class="footer">
        <p>© 2023 Sarah Johnson | <a href="mailto:sarah.johnson@example.com" style="color: #2C3E50; text-decoration: none;">Contact</a> | Last updated: May 2023</p>
    </div>
    
    <style>
    .footer {
        margin-top: 30px;
        padding-top: 10px;
        border-top: 1px solid #dee2e6;
        text-align: center;
        font-size: 0.8rem;
        color: #6c757d;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    """
    st.markdown(footer, unsafe_allow_html=True) 
 

with st.sidebar:
    st.markdown('''
    <div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    Personal Resume
    </div>''', unsafe_allow_html=True)
    
    selected_key = st_ant_menu(menu_data)
           
    st.html(
    f"""
    <div style="text-align: center;background-color:white;padding:20px;border-radius:10px;box-shadow: 0 0 10px #888;">
        <img src="data:image/png;base64,{base64_str}" alt="Profile Picture" style="border-radius: 50%;width:170px;box-shadow: 0 0 0 0;">
        <h4 style="margin: 2px;">Recent Master's Graduate in Marketing</h2>
        <div>Chinese University of Hong Kong</div>
        <div style="margin: 2px;">12 Chak Cheung St., Ma Liu Shui, HKSAR</div> 
        <hr>
        <div>Feel free to reach out to me through any of the following channels:</div>
        <div>Email<br><a href="sarah.johnson@example.com">mailto:sarah.johnson@example.com</a></div>
        <div>Phone<br><span style="color:blue;">(123)+1 456-7890</span></div>
        <div>LinkedIn<br><a href="linkedin.com/in/sarahjohnson">https://linkedin.com/in/sarahjohnson</a></div>
        <div>GitHub<br><a href="github.com/sarahjohnson">https://github.com/sarahjohnson</a></div>
    </div>
    """)

if selected_key=="1":
    homepage.main()
    display_footer()
elif selected_key=="2":
    educition.main()
    display_footer()
elif selected_key=="3":
    experience.main()
    display_footer()
elif selected_key=="4":
    resume.main()
    display_footer()
elif selected_key=="5":
    concat.main()
    display_footer()
else:
    homepage.main()
    display_footer()