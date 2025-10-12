import pandas as pd
import joblib
import numpy as np

class DashboardController:
    def __init__(self, model_path, scaler_path, feature_columns):
        # Carregar modelo e scaler
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        self.feature_columns = feature_columns  # ['year','month','uf','classname','numpol']

    # --- Obter bases ---
    def get_tratado(self):
        return pd.read_csv("data\desmatamento_tratado.csv")

    def get_resumo(self):
        return pd.read_csv("data\datadesmatamento_resumo.csv")

    # --- Filtragem ---
    def filter_data(self, selected_year=None, selected_uf=None):
        df = self.get_tratado()
        if selected_year is not None:
            df = df[df['year'] == selected_year]
        if selected_uf is not None:
            df = df[df['uf'] == selected_uf]
        return df

    # --- KPIs ---
    def get_kpis(self, df):
        return {
            "total": df['area'].sum(),
            "media": df['area'].mean(),
            "max": df['area'].max()
        }

    # --- Gráficos ---
    def get_line_plot(self, df):
        import plotly.express as px
        # Top 5 estados mais desmatados + "Outros"
        top_ufs = df.groupby("uf")["area"].sum().nlargest(5).index
        df_plot = df.copy()
        df_plot['uf_group'] = df_plot['uf'].apply(lambda x: x if x in top_ufs else 'Outros')
        df_plot = df_plot.groupby(['year','uf_group'])['area'].sum().reset_index()
        fig = px.line(df_plot, x='year', y='area', color='uf_group', markers=True)
        return fig

    def get_bar_plot(self, df):
        import plotly.express as px
        df_plot = df.groupby('uf')['area'].sum().reset_index().sort_values('area', ascending=False)
        fig = px.bar(df_plot, x='uf', y='area', color='area', text='area')
        fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        return fig

    def get_heatmap(self, df):
        import plotly.express as px
        df_plot = df.groupby(['year','uf'])['area'].sum().reset_index()
        df_pivot = df_plot.pivot(index='uf', columns='year', values='area').fillna(0)
        fig = px.imshow(df_pivot, text_auto=True, aspect="auto", color_continuous_scale='Viridis')
        return fig

    # --- Previsão ---
    def predict(self, df_input):
        df = df_input.copy()

        # Garantir colunas de treino
        missing_cols = [col for col in self.feature_columns if col not in df.columns]
        for col in missing_cols:
            df[col] = 0  # placeholder se faltar alguma coluna

        # One-hot encode categóricas presentes no treino
        cat_cols = ['uf','classname']
        df_encoded = pd.get_dummies(df, columns=cat_cols)
        # Alinhar com colunas do treino
        for col in self.feature_columns:
            if col not in df_encoded.columns:
                df_encoded[col] = 0
        df_encoded = df_encoded[self.feature_columns]

        # Escalar as colunas numéricas
        numeric_cols = df_encoded.select_dtypes(include=np.number).columns
        df_encoded[numeric_cols] = self.scaler.transform(df_encoded[numeric_cols])

        # Previsão
        prediction = self.model.predict(df_encoded)
        return prediction
