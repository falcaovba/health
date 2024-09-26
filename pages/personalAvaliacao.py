import streamlit as st
import pandas as pd
import altair as alt
import plotly.graph_objects as go

pg1, pg2, pg3 = st.columns([0.09,0.09,0.09], gap="small", vertical_alignment="top")
with pg1:
    st.page_link("streamlit_app.py", label="Home", icon="🏠")
with pg2:
    st.page_link("pages/planejamentoAlimentar.py", label="Planelamento Alimentar", icon="🥗")
with pg3:   
    st.page_link("pages/personalAvaliacao.py", label="Avaliação Personal", icon="💪")

st.header("💪 Avaliação Personal", divider="rainbow")


col1, col2, col3 = st.columns(3)

#with st.container(border=True):
with col1:
    with st.container(border=True):
        st.subheader("📐 Dados coletados", divider="rainbow")
        # Criar o DataFrame
        df_analise_geral = pd.DataFrame(
            {
                "Dados": ["Peso (kg)", "% Gordura", "Massa Magra (kg)", "Massa Gorda (kg)", "IMC", "Perimetria (cm)", "Antropometria (mm)", "RCQ"],
                "27/02/2024": [100, 21.68, 78.32, 21.68, 29.3, 710, 148.5, 98],
                "21/11/2023": [99, 23.29, 78.94, 23.06, 29.0, 698, 162, 96],
                "11/07/2023": [96, 26.39, 70.67, 25.33, 28.1, 691, 191.5, 97]
            }
        )

        df_analise_geral["Diferença"] = df_analise_geral["27/02/2024"] - df_analise_geral["11/07/2023"]
    
        st.dataframe(df_analise_geral, hide_index=True)

        # Remover a coluna "Diferença" se ela existir
        df_analise_geral = df_analise_geral.drop(columns=["Diferença"], errors="ignore")


    with col2:
        with st.container(border=True):
            st.subheader("📋 Protocolo: Pollock 7 Dobras", divider="rainbow")
            mtcol1, mtcol2, mtcol3 = st.columns(3)
            with mtcol1:
                st.metric(label="Idade", value="36 anos")
                st.metric(label="Peso kg", value="100kg", delta="96kg")
            with mtcol2:
                st.metric(label="Altura", value="1,86cm")
                st.metric(label="Massa Magra", value="78.32%", delta="73.61%")
            with mtcol3:
                st.metric(label="Ultima Avaliação", value="27/02/2024", delta="11/07/2023")
                st.metric(label="Gordura", value="21.68%", delta="26.39%")
                

with col3:
    with st.container(border=True):
        st.subheader("📈 Percentual de Gordura", divider="rainbow")
        # Dados
        labels = ['Gordura', 'Massa Magra']
        values = [21.68, 78.32]

        # Criar o gráfico de rosca
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5)])

        # Adicionar título ao gráfico
        fig.update_layout(
            #title_text='Percentual de Gordura',
            annotations=[dict(text='Gordura %', x=0.5, y=0.5, font_size=20, showarrow=False)])

        # Exibir o gráfico no Streamlit
        st.plotly_chart(fig)

with st.container(border=True):
    st.subheader("📊 Gráficos de Evolução",divider="rainbow")
    subcol1, subcol2, subcol3, subcol4  = st.columns([2,2,2,2])
    with subcol1: 
        # Filtrar apenas o valor do "Peso (kg)" e reorganizar os dados
        df_peso = df_analise_geral[df_analise_geral["Dados"] == "Peso (kg)"].melt(id_vars=["Dados"], var_name="Data", value_name="Peso (kg)")
        # Remover a coluna "Dados" já que agora estamos focados apenas no peso
        df_peso = df_peso.drop(columns=["Dados"])

        # Criar o gráfico usando Altair
        chart = alt.Chart(df_peso).mark_area().encode(
            x=alt.X('Data:O'), #title='Data'),
            y=alt.Y('Peso (kg):Q', title='Peso (kg)'),
            #color='Data:N',  # Define as cores por métrica
            tooltip=['Data:O', 'Peso (kg):N', 'Peso (kg):Q']
        ).properties(width=350,height=250,title='Peso (kg)').interactive()
        # Adiciona rótulos aos pontos no gráfico
        text = chart.mark_text(align='center', baseline='middle',dy=25,  # deslocamento vertical para cima
                            color='black', size=15  # cor dos rótulos de dados
        ).encode(text='Peso (kg):Q',x='Data:O',y='Peso (kg):Q')
        # Exibe o gráfico no Streamlit
        st.altair_chart(chart + text, use_container_width=False)
        
        #------------------------------------------------------------------------------------------------------------------------------------------------
        
        # Filtrar apenas o valor do "Peso (kg)" e reorganizar os dados
        df_peso = df_analise_geral[df_analise_geral["Dados"] == "% Gordura"].melt(id_vars=["Dados"], var_name="Data", value_name="% Gordura")
        # Remover a coluna "Dados" já que agora estamos focados apenas no peso
        df_peso = df_peso.drop(columns=["Dados"])

        # Criar o gráfico usando Altair
        chart = alt.Chart(df_peso).mark_area().encode(
            x=alt.X('Data:O'), #title='Data'),
            y=alt.Y('% Gordura:Q', title='% Gordura'),
            #color='Data:N',  # Define as cores por métrica
            tooltip=['Data:O', '% Gordura:N', '% Gordura:Q']
        ).properties(width=350,height=250,title='% Gordura').interactive()
        # Adiciona rótulos aos pontos no gráfico
        text = chart.mark_text(align='center', baseline='middle',dy=25,  # deslocamento vertical para cima
                            color='black', size=15  # cor dos rótulos de dados
        ).encode(text='% Gordura:Q',x='Data:O',y='% Gordura:Q')
        # Exibe o gráfico no Streamlit
        st.altair_chart(chart + text, use_container_width=False)
        
        #------------------------------------------------------------------------------------------------------------------------------------------------
   
    with subcol2: 
        # Filtrar apenas o valor do "Peso (kg)" e reorganizar os dados
        df_peso = df_analise_geral[df_analise_geral["Dados"] == "Massa Magra (kg)"].melt(id_vars=["Dados"], var_name="Data", value_name="Massa Magra (kg)")
        # Remover a coluna "Dados" já que agora estamos focados apenas no peso
        df_peso = df_peso.drop(columns=["Dados"])

        # Criar o gráfico usando Altair
        chart = alt.Chart(df_peso).mark_area().encode(
            x=alt.X('Data:O'), #title='Data'),
            y=alt.Y('Massa Magra (kg)', title='Massa Magra (kg)'),
            #color='Data:N',  # Define as cores por métrica
            tooltip=['Data:O', 'Massa Magra (kg):N', 'Massa Magra (kg):Q']
        ).properties(width=350,height=250,title='Massa Magra (kg)').interactive()
        # Adiciona rótulos aos pontos no gráfico
        text = chart.mark_text(align='center', baseline='middle',dy=25,  # deslocamento vertical para cima
                            color='black', size=15  # cor dos rótulos de dados
        ).encode(text='Massa Magra (kg):Q',x='Data:O',y='Massa Magra (kg)')
        # Exibe o gráfico no Streamlit
        st.altair_chart(chart + text, use_container_width=False)
        
        #------------------------------------------------------------------------------------------------------------------------------------------------
 
        # Filtrar apenas o valor do "Peso (kg)" e reorganizar os dados
        df_peso = df_analise_geral[df_analise_geral["Dados"] == "Massa Gorda (kg)"].melt(id_vars=["Dados"], var_name="Data", value_name="Massa Gorda (kg)")
        # Remover a coluna "Dados" já que agora estamos focados apenas no peso
        df_peso = df_peso.drop(columns=["Dados"])

        # Criar o gráfico usando Altair
        chart = alt.Chart(df_peso).mark_area().encode(
            x=alt.X('Data:O'), #title='Data'),
            y=alt.Y('Massa Gorda (kg)', title='Massa Gorda (kg)'),
            #color='Data:N',  # Define as cores por métrica
            tooltip=['Data:O', 'Massa Gorda (kg):N', 'Massa Gorda (kg):Q']
        ).properties(width=350,height=250,title='Massa Gorda (kg)').interactive()
        # Adiciona rótulos aos pontos no gráfico
        text = chart.mark_text(align='center', baseline='middle',dy=25,  # deslocamento vertical para cima
                            color='black', size=15  # cor dos rótulos de dados
        ).encode(text='Massa Gorda (kg):Q',x='Data:O',y='Massa Gorda (kg)')
        # Exibe o gráfico no Streamlit
        st.altair_chart(chart + text, use_container_width=False)
        
        #------------------------------------------------------------------------------------------------------------------------------------------------
    
    with subcol3: 
        # Filtrar apenas o valor do "Peso (kg)" e reorganizar os dados
        df_peso = df_analise_geral[df_analise_geral["Dados"] == "IMC"].melt(id_vars=["Dados"], var_name="Data", value_name="IMC")
        # Remover a coluna "Dados" já que agora estamos focados apenas no peso
        df_peso = df_peso.drop(columns=["Dados"])

        # Criar o gráfico usando Altair
        chart = alt.Chart(df_peso).mark_area().encode(
            x=alt.X('Data:O'), #title='Data'),
            y=alt.Y('IMC', title='IMC'),
            #color='Data:N',  # Define as cores por métrica
            tooltip=['Data:O', 'IMC:N', 'IMC:Q']
        ).properties(width=350,height=250,title='IMC').interactive()
        # Adiciona rótulos aos pontos no gráfico
        text = chart.mark_text(align='center', baseline='middle',dy=25,  # deslocamento vertical para cima
                            color='black', size=15  # cor dos rótulos de dados
        ).encode(text='IMC:Q',x='Data:O',y='IMC')
        # Exibe o gráfico no Streamlit
        st.altair_chart(chart + text, use_container_width=False)
        
        #------------------------------------------------------------------------------------------------------------------------------------------------

        # Filtrar apenas o valor do "Peso (kg)" e reorganizar os dados
        df_peso = df_analise_geral[df_analise_geral["Dados"] == "Perimetria (cm)"].melt(id_vars=["Dados"], var_name="Data", value_name="Perimetria (cm)")
        # Remover a coluna "Dados" já que agora estamos focados apenas no peso
        df_peso = df_peso.drop(columns=["Dados"])

        # Criar o gráfico usando Altair
        chart = alt.Chart(df_peso).mark_area().encode(
            x=alt.X('Data:O'), #title='Data'),
            y=alt.Y('Perimetria (cm)', title='Perimetria (cm)'),
            #color='Data:N',  # Define as cores por métrica
            tooltip=['Data:O', 'Perimetria (cm):N', 'Perimetria (cm):Q']
        ).properties(width=350,height=250,title='Perimetria (cm)').interactive()
        # Adiciona rótulos aos pontos no gráfico
        text = chart.mark_text(align='center', baseline='middle',dy=25,  # deslocamento vertical para cima
                            color='black', size=15  # cor dos rótulos de dados
        ).encode(text='Perimetria (cm):Q',x='Data:O',y='Perimetria (cm)')
        # Exibe o gráfico no Streamlit
        st.altair_chart(chart + text, use_container_width=False)
        
        #------------------------------------------------------------------------------------------------------------------------------------------------
   
    with subcol4: 
        # Filtrar apenas o valor do "Peso (kg)" e reorganizar os dados
        df_peso = df_analise_geral[df_analise_geral["Dados"] == "Antropometria (mm)"].melt(id_vars=["Dados"], var_name="Data", value_name="Antropometria (mm)")
        # Remover a coluna "Dados" já que agora estamos focados apenas no peso
        df_peso = df_peso.drop(columns=["Dados"])

        # Criar o gráfico usando Altair
        chart = alt.Chart(df_peso).mark_area().encode(
            x=alt.X('Data:O'), #title='Data'),
            y=alt.Y('Antropometria (mm)', title='Antropometria (mm)'),
            #color='Data:N',  # Define as cores por métrica
            tooltip=['Data:O', 'Antropometria (mm):N', 'Antropometria (mm):Q']
        ).properties(width=350,height=250,title='Antropometria (mm)').interactive()
        # Adiciona rótulos aos pontos no gráfico
        text = chart.mark_text(align='center', baseline='middle',dy=25,  # deslocamento vertical para cima
                            color='black', size=15  # cor dos rótulos de dados
        ).encode(text='Antropometria (mm):Q',x='Data:O',y='Antropometria (mm)')
        # Exibe o gráfico no Streamlit
        st.altair_chart(chart + text, use_container_width=False)
        
        #------------------------------------------------------------------------------------------------------------------------------------------------

        # Filtrar apenas o valor do "Peso (kg)" e reorganizar os dados
        df_peso = df_analise_geral[df_analise_geral["Dados"] == "RCQ"].melt(id_vars=["Dados"], var_name="Data", value_name="RCQ")
        # Remover a coluna "Dados" já que agora estamos focados apenas no peso
        df_peso = df_peso.drop(columns=["Dados"])

        # Criar o gráfico usando Altair
        chart = alt.Chart(df_peso).mark_area().encode(
            x=alt.X('Data:O'), #title='Data'),
            y=alt.Y('RCQ', title='RCQ'),
            #color='Data:N',  # Define as cores por métrica
            tooltip=['Data:O', 'RCQ:N', 'RCQ:Q']
        ).properties(width=350,height=250,title='RCQ').interactive()
        # Adiciona rótulos aos pontos no gráfico
        text = chart.mark_text(align='center', baseline='middle',dy=25,  # deslocamento vertical para cima
                            color='black', size=15  # cor dos rótulos de dados
        ).encode(text='RCQ:Q',x='Data:O',y='RCQ')
        # Exibe o gráfico no Streamlit
        st.altair_chart(chart + text, use_container_width=False)
