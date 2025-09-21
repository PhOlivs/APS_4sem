from src.model.carregar_dados import CarregarDados
from src.model.desmatamento import desmatamento

class controle:
    def __init__ (self, path):
        self.path = path
        
    def analisar_dados(self):
        carregar = CarregarDados(self.path)
        df = carregar.carregar_csv()
        
        if df is None:
            return None
        
        model = desmatamento(df)
        resultados = model.train()
        
        return resultados
