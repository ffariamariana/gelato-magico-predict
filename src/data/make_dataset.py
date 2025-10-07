# src/data/make_dataset.py
import pandas as pd
import numpy as np
import random
from datetime import date, timedelta
import os

# --- LÓGICA PARA ENCONTRAR A RAIZ DO PROJETO ---
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
project_root = os.path.dirname(os.path.dirname(script_dir))


# ------------------------------------------------

def gerar_dados_sorveteria(dias=365, data_inicial=date(2023, 1, 1)):
    """
    Gera um dataset sintético e realista de vendas de sorvete para o Brasil.
    """
    print("Iniciando a geração de dados realistas...")
    output_path = os.path.join(project_root, 'data', 'raw', 'dados_sorveteria.csv')

    # --- FERIADOS NACIONAIS E PONTOS FACULTATIVOS DE 2023 ---
    # Incluindo feriados móveis
    feriados_2023 = {
        date(2023, 1, 1),  # Confraternização Universal
        date(2023, 2, 20),  # Carnaval
        date(2023, 2, 21),  # Carnaval
        date(2023, 4, 7),  # Paixão de Cristo
        date(2023, 4, 21),  # Tiradentes
        date(2023, 5, 1),  # Dia do Trabalho
        date(2023, 6, 8),  # Corpus Christi
        date(2023, 9, 7),  # Independência
        date(2023, 10, 12),  # Nossa Sra. Aparecida
        date(2023, 11, 2),  # Finados
        date(2023, 11, 15),  # Proclamação da República
        date(2023, 12, 25),  # Natal
    }

    # Temperaturas por mês para o Sudeste (mais realistas)
    temp_ranges_por_mes = {
        1: (24, 38), 2: (24, 38), 3: (22, 34), 4: (20, 30), 5: (17, 26), 6: (15, 25),
        7: (15, 24), 8: (17, 27), 9: (19, 30), 10: (21, 32), 11: (22, 34), 12: (23, 36)
    }

    lista_de_dados = []
    for i in range(dias):
        data_atual = data_inicial + timedelta(days=i)
        mes_atual = data_atual.month
        dia_da_semana = data_atual.weekday()  # Segunda=0, Domingo=6

        # --- FEATURES GERADAS ---
        feriado = 1 if data_atual in feriados_2023 else 0

        # Lógica de férias escolares (Jan, últimas 2 semanas de Jul, segunda quinzena de Dez)
        ferias_escolares = 1 if (mes_atual == 1) or \
                                (mes_atual == 7 and data_atual.day > 15) or \
                                (mes_atual == 12 and data_atual.day > 15) else 0

        # Lógica de precipitação (chuva em mm)
        precipitacao_mm = 0
        if random.random() < (0.4 if mes_atual in [1, 2, 3, 11, 12] else 0.15):  # Maior chance de chuva no verão
            precipitacao_mm = random.uniform(5, 50)  # Pancadas de verão
        elif random.random() < 0.1:  # Chuva leve fora de época
            precipitacao_mm = random.uniform(1, 10)

        temperatura = round(random.uniform(*temp_ranges_por_mes[mes_atual]), 1)

        # --- LÓGICA DE VENDAS REFINADA ---
        vendas = 100  # Base de vendas

        # Influência da temperatura (muito forte)
        vendas += (temperatura - 20) * 15

        # Influência do dia da semana (aumento gradual até o fds)
        vendas += dia_da_semana * 10
        if dia_da_semana >= 5:  # Bônus extra para Sábado e Domingo
            vendas += 50

        # Bônus de Férias (principalmente em dias de semana)
        if ferias_escolares == 1 and dia_da_semana < 5:
            vendas += 60

        # Bônus de Feriado (muito forte, principalmente se estiver quente)
        if feriado == 1:
            vendas += 150
            if temperatura > 28:  # Interação: feriado quente vende ainda mais
                vendas += 100

        # Impacto negativo da chuva (não-linear)
        if precipitacao_mm > 0:
            # Redutor baseado na intensidade da chuva. Chuva forte (>25mm) impacta muito.
            redutor = 1 - (precipitacao_mm / (50 + precipitacao_mm))
            vendas *= redutor

        # Ruído final para simular outros fatores
        vendas += random.uniform(-20, 20)
        vendas = int(max(vendas, 20))  # Venda mínima

        lista_de_dados.append({
            "Data": data_atual,
            "Temperatura_C": temperatura,
            "Precipitacao_mm": round(precipitacao_mm, 1),
            "Feriado": feriado,
            "Ferias_Escolares": ferias_escolares,
            "Vendas_Sorvete": vendas
        })

    df_sorveteria = pd.DataFrame(lista_de_dados)

    # --- Salvando os Dados ---
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    df_sorveteria.to_csv(output_path, index=False)
    print(f"Arquivo de dados realista salvo em: '{output_path}'")

    return df_sorveteria


if __name__ == '__main__':
    gerar_dados_sorveteria()