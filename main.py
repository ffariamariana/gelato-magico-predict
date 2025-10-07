# 1. Imports necessários
import mlflow
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


# 2. Crie uma classe para validar os dados de entrada da API
#    Isso garante que a API sempre receberá os dados no formato correto
class InputFeatures(BaseModel):
    Temperatura_C: float
    Precipitacao_mm: float
    Feriado: int
    Ferias_Escolares: int
    Dia_da_Semana: int


# 3. Carregue o modelo treinado do MLflow
#    Use o Run ID do seu melhor modelo

logged_model_uri = 'runs:/ab137eac4c254ab18fbee91ebaf3950f/modelo_preditivo'

# Carrega o modelo como uma função genérica do Python
loaded_model = mlflow.pyfunc.load_model(logged_model_uri)

# 4. Crie a instância do aplicativo FastAPI
app = FastAPI()


# 5. Crie o endpoint de predição
@app.post("/predict")
def predict(features: InputFeatures):
    """
    Recebe as features como entrada e retorna a previsão de vendas de sorvete.
    """
    # Cria um DataFrame do Pandas com os dados recebidos
    # O modelo do MLflow espera um DataFrame como entrada
    data = pd.DataFrame([features.dict()])

    # Faz a predição usando o modelo carregado
    prediction = loaded_model.predict(data)

    # Extrai o resultado da predição (que vem em uma lista)
    output = int(prediction[0])

    # Retorna o resultado em formato JSON
    return {"previsao_vendas": output}


# Endpoint raiz para um simples "Olá, Mundo"
@app.get("/")
def home():
    return {"message": "API do Modelo de Previsão de Vendas - Gelato Mágico"}