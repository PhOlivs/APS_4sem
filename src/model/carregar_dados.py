import pandas as pd

class CarregarDados:
    def __init__(self, path):
        self.path = path
        
    def carregar_csv(self):
        try:
            df = pd.read_csv(self.path)
            return df
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {self.path}")
            return None
