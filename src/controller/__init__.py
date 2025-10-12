class DashboardController:
    def __init__(self, model=None, scaler=None, feature_columns=None):
        self.model = model
        self.scaler = scaler
        self.feature_columns = feature_columns  # armazena as colunas
