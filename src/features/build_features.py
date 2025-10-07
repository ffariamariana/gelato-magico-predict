# -*- coding: utf-8 -*-
import pandas as pd


def criar_features_de_data(df):
    """
    Cria features de data (Mês e Dia da Semana) a partir de uma coluna 'Data'.

    Args:
        df (pd.DataFrame): DataFrame que contém uma coluna 'Data'.

    Returns:
        pd.DataFrame: O DataFrame com as novas colunas 'Mes' e 'Dia_da_Semana'.
    """
    if 'Data' not in df.columns:
        raise ValueError("O DataFrame precisa ter uma coluna 'Data'.")

    # Garante que a coluna 'Data' é do tipo datetime para manipulação
    df['Data'] = pd.to_datetime(df['Data'])

    # Criando as features a partir da data
    df['Mes'] = df['Data'].dt.month
    df['Dia_da_Semana'] = df['Data'].dt.dayofweek  # Segunda=0, Domingo=6

    print("Features 'Mes' e 'Dia_da_Semana' criadas/atualizadas.")

    return df


# --- Bloco de Execução para Teste ---
# Este bloco só é executado quando você roda o script diretamente.
# Ex: python src/features/build_features.py
# Ele serve para testar a função 'criar_features_de_data' de forma isolada.
if __name__ == '__main__':
    # Simula o carregamento do dataset para um teste rápido
    try:
        caminho_dados = 'data/raw/dados_sorveteria.csv'
        df_teste = pd.read_csv(caminho_dados)

        print("DataFrame de teste carregado (antes das features):")
        print(df_teste.head())
        print("\n------------------------------------------------\n")

        # Aplica a função para criar as features
        df_com_features = criar_features_de_data(df_teste)

        print("\nDataFrame com as novas features:")
        print(df_com_features.head())

    except FileNotFoundError:
        print("\nArquivo 'data/raw/dados_sorveteria.csv' não encontrado.")
        print("Execute o script 'src/data/make_dataset.py' primeiro para gerar os dados.")