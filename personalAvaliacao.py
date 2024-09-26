import streamlit as st

pg1, pg2, pg3 = st.columns([0.09,0.09,0.09], gap="small", vertical_alignment="top")
with pg1:
    st.page_link("streamlit_app.py", label="Home", icon="🏠")
with pg2:
    st.page_link("pages/planejamentoAlimentar.py", label="Planelamento Alimentar", icon="🥗")
with pg3:   
    st.page_link("pages/planejamentoAlimentar.py", label="Avaliação Personal", icon="💪")

st.header("💪 Avaliação Personal", divider="rainbow")