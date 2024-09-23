import streamlit as st
import pandas as pd

st.set_page_config(page_title='Health - Pedro Henrique', page_icon='🏋️‍♀️',layout="wide")

st.header("🥗 Planejamento Alimentar", divider="rainbow")

tab1, tab2, tab3 = st.tabs(["Manhã", "Tarde", "Noite"])

with tab1:
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.subheader("Café da manhã")

            df_cafe_manha = pd.DataFrame(
                {
                    "Alimento": ["Inhame/Cará cozido", "Ovo mexido", "Semente de chia", "Requeijão ligth"],
                    "Medida": ["150g", "2 unidades média - 70g", "1 colher de sobremesa 8g", "20g"]        
                }
            )
            st.dataframe(df_cafe_manha,hide_index=True)

            # opção 1
            st.write('''
            <h5> • Opções de substituição para Cará/inhame cozido: </h5>
            ''',unsafe_allow_html=True)
            st.write(''' 
            Cuscuz - 145g - ou - Banana da terra - 125g - ou - Pão de forma integral – 2 fatia(s) (50g) ou pão francês - 1 (50g)
            ''')
            st.warning(''' **OBS:** Caso coma o cuscuz, colocar a chia ou aveia em flocos na massa antes de cozinhar para diminuir o índice glicêmico
            ''', icon="⚠️")

            # opção 2
            st.write('''
            <h5> • Opções de substituição para Ovo de galinha mexido: </h5>
            ''',unsafe_allow_html=True)
            st.write(''' 
            Omelete com tomate e cebola - 2 Unidade(s) média(s) (100g) - ou - Atum em conserva em óleo - 3 Colher(es) de sopa cheia(s) (48g) - ou - Queijo coalho - 45g - ou - Queijo minas - 45g
            ''')
            st.warning(''' **OBS:** Usar o mínimo de manteiga/margarina/azeite para fazer o ovo mexido, tentar fazer com água em frigideira antiaderente, lavar bem o atum pra tirar o óleo antes de consumir
            ''', icon="⚠️")

            # opção 3
            st.write('''
            <h5> • Opções de substituição para Semente de chia: </h5>
            ''',unsafe_allow_html=True)
            st.write(''' 
            Aveia em flocos finos/grossos - 1 Colher(es) de sopa rasa(s) (15g) - ou - Semente de gergelim - 1 colher de sobremesa 8g
            ''')

            # opção 4
            st.write('''
            <h5> • Opções de substituição para Creme de ricota: </h5>
            ''',unsafe_allow_html=True)
            st.write(''' 
            Requeijão light - 20g
            ''')

            st.error(''' **Observações gerais:** Fazer a ingestão em jejum de 500 ml de água
            ''', icon="🚨")
    
    with col2:
        with st.container(border=True):
            st.subheader("Lanche da manhã")

            df_lanche_manha = pd.DataFrame(
                {
                    "Alimento": ["Maçã", "Pasta de Amendoin"],
                    "Medida": ["1 unidade média 100g", "1 colher de chá rasa 16g"]        
                }
            )
            st.dataframe(df_lanche_manha,hide_index=True)

            # opção 5
            st.write('''
            <h5> • Opções de substituição para Maçã: </h5>
            ''',unsafe_allow_html=True)
            st.write(''' 
            Maçã verde - 1 Unidade(s) média(s) (100g) - ou - Banana prata - 1 Unidade(s) média(s) (100g) - ou - Mamão papaia - 2 Fatia(s) média(s) (340g) - ou - Pera - 1 Unidade(s) grande(s) (190g) 
            ''')

            # opção 6
            st.write('''
            <h5> • Opções de substituição para Pasta de Amendoim: </h5>
            ''',unsafe_allow_html=True)
            st.write(''' 
            Amendoim - 10g - ou - Castanha de caju - 20g - ou - Castanha do Brasil - 2 Unidade(s) (8g)
            ''')
            st.warning(''' **OBS:** Caso não queira as opões de amendoim/pastas e afins, faça uma pequena salada de frutas com 3 opções de frutas (dê preferencia a frutas com mais liquido, adicione chia (3g) e granola (8g)
            ''', icon="⚠️")