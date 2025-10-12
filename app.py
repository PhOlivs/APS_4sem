from src.controller.dashboard_controller import DashboardController
from src.view.dashboard_view import DashboardView

# Caminhos
model_path = "data\datamodelo_random_forest.pkl"
scaler_path = "data\datascaler.pkl"
feature_columns = ['year','month','uf','classname','numpol']

# Instâncias
controller = DashboardController(model_path, scaler_path, feature_columns)
view = DashboardView(controller)
view.render()
