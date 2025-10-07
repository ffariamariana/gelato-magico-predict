# Importando as bibliotecas necessárias
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor  # Importe o RandomForest aqui
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Importando nossa função de engenharia de features
from src.features.build_features import criar_features_de_data

print("Iniciando o script de treinamento...")

# Garantindo o caminho correto do MLflow
mlflow.set_tracking_uri("file:./mlruns")

# --- 1. Carregamento dos Dados ---
try:
    df = pd.read_csv('data/raw/dados_sorveteria.csv')
    print("Dados carregados com sucesso.")
except FileNotFoundError:
    print("Erro: Arquivo 'dados_sorveteria.csv' não encontrado.")
    exit()

# --- 2. Preparação e Engenharia de Features ---
df = criar_features_de_data(df)
df['Mes'] = df['Data'].dt.month
df['Dia_da_Semana'] = df['Data'].dt.dayofweek

# Selecionando as features (X) e o alvo (y)
features = ['Temperatura_C', 'Precipitacao_mm', 'Feriado', 'Ferias_Escolares', 'Dia_da_Semana']
target = 'Vendas_Sorvete'

X = df[features]
y = df[target]

# Dividindo os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Dados divididos em treino e teste.")

# --- 3. Treinamento com MLflow ---
mlflow.set_experiment("predicao_vendas_gelato_magico")

with mlflow.start_run():
    print("Iniciando uma run do MLflow...")

    # Logando o tipo de modelo que estamos usando
    mlflow.log_param("model_type", "RandomForestRegressor")

    # Criando e treinando o modelo RandomForest
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    print("Modelo treinado.")

    # Fazendo previsões com os dados de teste
    y_pred = model.predict(X_test)

    # --- 4. Avaliação do Modelo ---
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("-" * 30)
    print("Métricas de Avaliação do Modelo:")
    print(f"  MSE (Erro Quadrático Médio): {mse:.2f}")
    print(f"  MAE (Erro Absoluto Médio): {mae:.2f}")
    print(f"  R² Score: {r2:.2f}")
    print("-" * 30)

    # --- 5. Registro no MLflow ---
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("mae", mae)
    mlflow.log_metric("r2_score", r2)

    mlflow.sklearn.log_model(model, "modelo_preditivo")

    print("Métricas e modelo registrados no MLflow com sucesso.")
    print("Run do MLflow concluída.")

print("Treinamento finalizado.")