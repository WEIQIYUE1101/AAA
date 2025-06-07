import streamlit as st

def main():
    st.markdown('''
    <div style="text-align: center; font-size: 26px; font-weight: bold; color: black; background: transparent; border-radius: 0rem; margin-bottom: 15px; border-bottom: 1px solid black;">
    Home Page
    </div>''', unsafe_allow_html=True)
    
    with st.expander("**About Me**", True):
        st.markdown(
        """
        Master of Science in Marketing (Big Data Track) from The Chinese University of Hong Kong (QS 36) with a strong academic record. Proven ability to translate insights into actionable strategies, demonstrated at Nissan China: reduced order cancellation rate by 18% through data analysis and proposed optimizations. Expertise spans integrated marketing campaigns (IMC design for HBAF), digital channel analysis (SEM/SMM for Jellycat), and consumer behavior modeling (Conjoint analysis for Freshippo predicting 30%+ market share gains). Equipped with advanced analytical skills (Python, R, Excel modeling) and fluency in cross-platform marketing (Weibo, Xiaohongshu, O2O). Award-winning learner with exceptional quantitative acumen, seeking to leverage technical marketing expertise to solve complex business challenges and drive measurable ROI. 
        """)

    with st.expander("**Skills**", True):
        st.markdown(
        """
        - Programming Languages: Python, R
        - Data Analysis: Pandas, NumPy, Matplotlib, Seaborn
        - Machine Learning: Scikit-learn, TensorFlow, Keras
        - Database: SQL, MongoDB
        - Data Visualization: Tableau, Power BI
        - Statistical Analysis: Hypothesis Testing, Regression Analysis
        - Communication: Presentation Skills, Technical Writing
        """)