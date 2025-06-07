import streamlit as st

def main():
    st.markdown('''
    <div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    Educition
    </div>''', unsafe_allow_html=True)
    
    with st.expander("**Master of Science in Marketing** *(:red[The Chinese University of Hong Kong] | :green[August 2024 - June 2025])*", True):
        st.markdown(
        """
        - :blue-background[ **GPA:** ] 3.5/4.0
        - :blue-background[ **Thesis:** ] "Applying Machine Learning Techniques to Predict Customer Behavior in E-commerce"
        - :blue-background[ **Relevant Coursework:** ]  Machine Learning, Social Media Analytics, Digital Marketing, Data Visualization,Marketing Research, Big Data Analytics
        """)
        
    with st.expander("**Bachelor of Manegementment in Accounting** *(:red[Soochow University] | :green[September 2020 - June 2024])*", True):
        st.markdown(
        """
        - :blue-background[ **GPA:** ] 3.6/4.0
        - :blue-background[ **Thesis:** ] "Graduated with Honors"
        - :blue-background[ **Relevant Coursework:** ] Advanced Financial Accounting, Tax Law, Microeconomics, Macroeconomics, Management Accounting
        """)
    
    st.markdown('''
    <div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    Certifications
    </div>''', unsafe_allow_html=True)
    
    col = st.columns(2, border=True)
    
    with col[0]:
        st.markdown("""
        ##### Second-Class Scholarship Awarded by Soochow University
        :red[**Amazon Web Services**] | :green[*June 2022*]
        Demonstrated exceptional learning agility and consistently high GPA.
        """)
        
    with col[1]:
        st.markdown("""
        ##### Third Prize of Na6onal English Compe66on for College Students
        :red[**Google**] | :green[*January 2022*]  
        Validated ability to use English in daily life.
        """)
        
    
    st.markdown('''
    <div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    Academic Projects
    </div>''', unsafe_allow_html=True)
    
    col = st.columns(2, border=True)
    
    with col[0]:
        st.markdown("""
        ##### IMG Design
        - Integrated multi - channels online (Weibo, mini - programs) and offline (subway advertisements, Buffer Bus activities) to cover the multi - scenario touch - points of target users.
        - Designed the script for life - themed advertising videos to meet the placement requirements of social platforms and offline media; designed the framework of the WeChat mini - program, planned the reward redemption process with points; developed the traffic - attracting logic for the offline "Buffer Bus" activity.
        - Developed a KPI system including GRP and brand awareness improvement based on the Ostrow model, and proposed AB testing to optimize advertising materials.
        """)
        
    with col[1]:
        st.markdown("""
        ##### Digital Marketing Analysis
        - Analyzed the user purchase journey using the funnel model to determine the corresponding digital marketing channels for subsequent analysis.
        - SEM: Conducted indicator analysis using Spy Fu and SEMrush to optimize SEO and paid search for enhanced target - positioning strategies.
        - SMM: Created word clouds, analyzed the repost, like, and comment situations of official accounts' content and UGC on various platforms, understood relevant marketing activities, and analyzed their effectiveness.
        """)