import streamlit as st

def main():
    st.markdown('''
    <div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    Concat Me & Send Me a Message
    </div>''', unsafe_allow_html=True)
    
    with st.form("contact_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            name = st.text_input("Name: WEI Qiyue")
            
        with col3:
            subject = st.text_input("Email: 1155218683@link.cuhk.edu.hk")
            
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            st.success("Thanks for your message! I'll get back to you soon.")
            # In a real application, you would process the form data here
            # For example, send an email or store in a database
    
    st.markdown("---")
    
    st.info("""
    **Office Hours:** I'm generally available for virtual meetings Monday through Friday, 9 AM to 5 PM Eastern Time.
    Please email me to schedule a call or video conference.
    """)