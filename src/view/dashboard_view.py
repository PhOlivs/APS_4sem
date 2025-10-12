import streamlit as st
import pandas as pd
import plotly.express as px

class DashboardView:
    def __init__(self, controller):
        self.controller = controller

    def render(self):
        st.set_page_config(
            page_title="Dashboard Desmatamento",
            layout="wide",
            initial_sidebar_state="expanded"
        )

        # --- Cabeçalho ---
        st.markdown("""
        <div style="background-color:#4CAF50;padding:15px;border-radius:10px">
            <h1 style="color:white;text-align:center;">🌳 Dashboard de Desmatamento da Amazônia</h1>
        </div>
        """, unsafe_allow_html=True)

        # --- Carregar dados ---
        df_tratado = self.controller.get_tratado()

        # --- Sidebar filtros ---
        st.sidebar.header("Filtros")
        selected_year = st.sidebar.selectbox("Ano", [None] + sorted(df_tratado['year'].unique()))
        selected_uf = st.sidebar.selectbox("Estado", [None] + sorted(df_tratado['uf'].unique()))
        selected_class = st.sidebar.selectbox("Classe", [None] + sorted(df_tratado['classname'].unique()))

        df_filtrado = df_tratado.copy()
        if selected_year: df_filtrado = df_filtrado[df_filtrado['year']==selected_year]
        if selected_uf: df_filtrado = df_filtrado[df_filtrado['uf']==selected_uf]
        if selected_class: df_filtrado = df_filtrado[df_filtrado['classname']==selected_class]

        # --- KPIs em cards ---
        kpis = self.controller.get_kpis(df_filtrado)
        st.markdown("### 📊 Indicadores")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Desmatado (ha)", f"{kpis['total']:.2f}")
        col2.metric("Média Anual (ha)", f"{kpis['media']:.2f}")
        col3.metric("Máximo em um Ano (ha)", f"{kpis['max']:.2f}")

        # --- Gráficos ---
        st.markdown("### 📈 Gráficos Interativos")

        # --- Linha: Top 5 + Outros ---
        df_top5 = df_filtrado.groupby("uf")["area"].sum().nlargest(5).index
        df_filtrado['uf_group'] = df_filtrado['uf'].apply(lambda x: x if x in df_top5 else 'Outros')
        line_fig = px.line(
            df_filtrado.groupby(['year','uf_group'])['area'].sum().reset_index(),
            x='year', y='area', color='uf_group',
            markers=True,
            title="Desmatamento por Estado ao longo dos anos",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(line_fig, use_container_width=True)

        # --- Barras horizontais ---
        bar_df = df_filtrado.groupby('uf_group')['area'].sum().reset_index().sort_values('area', ascending=False)
        bar_fig = px.bar(
            bar_df, x='area', y='uf_group', orientation='h', text='area',
            title="Total de Desmatamento por Estado",
            color='area', color_continuous_scale='Viridis'
        )
        st.plotly_chart(bar_fig, use_container_width=True)

        # --- Heatmap ---
        heat_df = df_filtrado.groupby(['uf_group','year'])['area'].sum().reset_index()
        heat_fig = px.density_heatmap(
            heat_df, x='year', y='uf_group', z='area',
            color_continuous_scale='Viridis',
            title="Heatmap de Desmatamento por Estado e Ano"
        )
        st.plotly_chart(heat_fig, use_container_width=True)

        # --- Previsão ---
        st.markdown("### 🤖 Previsão de Desmatamento")
        with st.form("predict_form"):
            st.subheader("Insira os parâmetros para previsão:")
            pred_year = st.number_input("Ano", min_value=int(df_tratado['year'].min()), max_value=int(df_tratado['year'].max()), value=int(df_tratado['year'].max()))
            pred_month = st.number_input("Mês", min_value=1, max_value=12, value=1)
            pred_uf = st.selectbox("Estado", df_tratado['uf'].unique())
            pred_class = st.selectbox("Classe", df_tratado['classname'].unique())
            pred_numpol = st.number_input("Número de polígonos", min_value=0, value=1)

            submit = st.form_submit_button("Prever")

        if submit:
            df_input = pd.DataFrame([{
                'year': pred_year,
                'month': pred_month,
                'uf': pred_uf,
                'classname': pred_class,
                'numpol': pred_numpol
            }])
            prediction = self.controller.predict(df_input)
            st.success(f"🔹 Previsão de desmatamento: {prediction[0]:.2f} ha")
