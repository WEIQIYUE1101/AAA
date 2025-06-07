import streamlit as st
import interactive

def main():
    st.markdown('''
    <div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    Professional Experience
    </div>''', unsafe_allow_html=True)
    
    with st.expander("**Marketing Intern** *(:red[Nissan (China) Investment Co., LTD.] | :green[November 2023 - April 2024])*", True):
        st.markdown(
        """
         - Established a financial model based on established data from market research and reasonable assumptions to predict the platform's operating profit for the next decade.
         - Utilized tools such as PivotTables to analyze backend operation data, and after proposing optimization suggestions, the weekly order cancellation rate decreased by 18%.
         - Participated in the production and review of advertisements on various platforms, collaborated with Xiaohongshu influencers to generate UGC, and tracked traffic and push effectiveness.
        """)
        
    with st.expander("**Audit Intern** *(:red[Suya Jincheng CPA LLP.] | :green[Janurary 2023 - March 2023])*", True):
        st.markdown(
        """
         - Participated in the year - end audits of various companies in 2022. Using the VLOOKUP function and PivotTable function in Excel, sorted out nearly 8,000 account data by time and subject, and completed the initial draft of the expense audit.
        """)
    
    
    col = st.columns(2, border=True)
    
    with col[0]:
        st.markdown("""
        ##### Technical Skills
        - **Programming Languages:** Python, R
        """)
        
    with col[1]:
        st.markdown("""
        ##### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)