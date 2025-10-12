import pandas as pd
import plotly.express as px
from joblib import load
import os

class DesmatamentoModel:
    def __init__(self):
        base_dir = "data"
        self.df_tratado_path = os.path.join(base_dir, "desmatamento_tratado.csv")
        self.df_resumo_path = os.path.join(base_dir, "datadesmatamento_resumo.csv")
        self.model_path = os.path.join(base_dir, "datamodelo_random_forest.pkl")
        self.scaler_path = os.path.join(base_dir, "datascaler.pkl")

        self.df_tratado = None
        self.df_resumo = None
        self.model = None
        self.scaler = None

    # Normalizar e renomear colunas
    def normalize_columns(self, df, rename_dict=None):
        df.columns = df.columns.str.strip().str.lower()
        if rename_dict:
            df.rename(columns=rename_dict, inplace=True)
        return df

    # Carregar CSVs
    def load_data(self):
        self.df_tratado = pd.read_csv(self.df_tratado_path)
        self.df_resumo = pd.read_csv(self.df_resumo_path)

        # Renomear colunas para padrão do dashboard
        rename_map = {
            'year': 'ano',
            'uf': 'estado',
            'area': 'area_desmatada'
        }

        self.df_tratado = self.normalize_columns(self.df_tratado, rename_map)
        self.df_resumo = self.normalize_columns(self.df_resumo, rename_map)

        return self.df_tratado, self.df_resumo

    # Carregar modelo e scaler
    def load_model(self):
        self.model = load(self.model_path)
        self.scaler = load(self.scaler_path)

    # Filtrar dados
    def filter_data(self, ano=None, estado=None):
        df = self.df_tratado.copy()
        if 'ano' in df.columns and ano:
            df = df[df['ano'] == ano]
        if 'estado' in df.columns and estado:
            df = df[df['estado'] == estado]
        return df

    # Gráficos
    def create_line_plot(self, df=None):
        if df is None:
            df = self.df_resumo
        fig = px.line(df, x='ano', y='area_desmatada', color='estado',
                      title='Desmatamento por Estado ao longo dos anos')
        return fig

    def create_bar_plot(self, df=None):
        if df is None:
            df = self.df_resumo
        fig = px.bar(df, x='estado', y='area_desmatada', color='ano',
                     title='Desmatamento por Estado')
        return fig

    def create_heatmap(self, df=None):
        if df is None:
            df = self.df_resumo
        # Agrupar para evitar duplicatas
        df_grouped = df.groupby(['estado', 'ano'], as_index=False)['area_desmatada'].sum()
        pivot = df_grouped.pivot(index='estado', columns='ano', values='area_desmatada')
        fig = px.imshow(pivot, text_auto=True, aspect="auto", title="Mapa de Calor do Desmatamento")
        return fig

    # KPIs
    def get_kpis(self, df=None):
        if df is None:
            df = self.df_tratado
        if 'area_desmatada' not in df.columns:
            raise KeyError("Coluna 'area_desmatada' não encontrada")
        total = df['area_desmatada'].sum()
        media = df['area_desmatada'].mean()
        max_val = df['area_desmatada'].max()
        return {"total": total, "media": media, "max": max_val}

    # Previsão Random Forest
    def predict(self, input_data):
        input_scaled = self.scaler.transform(input_data)
        pred = self.model.predict(input_scaled)
        return pred
