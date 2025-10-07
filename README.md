🍦 Projeto Gelato Mágico: Previsão de Vendas com Machine Learning
Este repositório contém um projeto completo de Data Science, cujo objetivo é desenvolver um modelo de Machine Learning de alta performance para prever as vendas diárias da sorveteria fictícia "Gelato Mágico".

🎯 1. Objetivo de Negócio
A "Gelato Mágico" enfrenta um desafio comum no varejo: como prever a demanda de sorvetes para otimizar a produção? Produzir demais gera desperdício e prejuízo; produzir de menos resulta em perda de vendas e clientes insatisfeitos.

A solução proposta é um modelo preditivo que utiliza dados históricos e fatores externos (como clima e feriados) para prever as vendas diárias, permitindo um planejamento de estoque e produção muito mais eficiente.

🛠️ 2. Ferramentas Utilizadas
Categoria	Ferramentas
Linguagem	Python 3.11
Análise e Modelagem	Pandas, Scikit-learn, NumPy
Visualização de Dados	Matplotlib, Seaborn
Experiment Tracking (MLOps)	MLflow
Ambiente de Desenvolvimento	Jupyter Notebook, VS Code

Exportar para as Planilhas
📂 3. Estrutura do Projeto
O projeto foi organizado em uma estrutura modular para garantir a reprodutibilidade e a clareza do código, seguindo as melhores práticas de projetos de Data Science.

gelato-magico-predict/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/            # Datasets originais
│   └── processed/      # Datasets processados
│
├── notebooks/          # Notebooks de análise exploratória e experimentação
│
├── src/
│   ├── data/
│   │   └── make_dataset.py       # Script para gerar o dataset sintético
│   ├── features/
│   │   └── build_features.py     # Script para criar novas features
│   └── models/
│       └── train_model.py        # Script final para treinar e registrar o modelo
│
└── mlruns/             # Pasta gerada pelo MLflow para salvar os experimentos
📊 4. Análise Exploratória de Dados (EDA) - Contando a História dos Dados
Antes da modelagem, foi realizada uma profunda análise exploratória para entender os padrões que governam as vendas.

Sazonalidade e Tendência Anual: A análise da série temporal revela a forte sazonalidade do negócio, com picos claros no verão e um vale no inverno. A média móvel de 7 dias suaviza o ruído diário e destaca a tendência.
Substitua pelo link da sua imagem no GitHub

O Ritmo da Semana: O fluxo de clientes tem um ritmo semanal previsível, crescendo a partir de quinta-feira e atingindo seu pico absoluto no Sábado.
Substitua pelo link da sua imagem no GitHub

A Interação entre Temperatura e Chuva: A temperatura é o principal fator, mas a chuva tem um poder de veto. O gráfico abaixo mostra que, para uma mesma temperatura, as vendas são sistematicamente menores em dias chuvosos.
Substitua pelo link da sua imagem no GitHub

🧠 5. A Jornada de Modelagem - Da Simplicidade à Otimização
A busca pelo melhor modelo foi um processo iterativo, onde cada etapa foi registrada com MLflow para comparação e análise.

Modelo Baseline (Regressão Linear): Com o dataset realista, o modelo linear alcançou um R² de 0.90, mas com um erro médio (MAE) ainda alto de 22.35 sorvetes. Isso indicou que o modelo capturava a tendência, mas não as complexas interações não-lineares.

Evolução (Random Forest): Ao trocar para um RandomForestRegressor, a performance melhorou drasticamente. O R² subiu para 0.93 e o MAE caiu para 16.77 sorvetes.

Tabela Comparativa dos Experimentos (Resultados do MLflow)
Modelo / Features	R² Score	MAE (Erro Médio)
Regressão Linear (6 Features)	0.90	22.35
Random Forest (5 Features)	0.93	16.77
Random Forest (4 Features - Antigo)	0.93	16.44

Exportar para as Planilhas
🏆 6. O Modelo Campeão e Resultados Finais
Após um ciclo completo de experimentação, o modelo final foi definido.

Modelo Final: RandomForestRegressor (com parâmetros padrão do Scikit-learn).

Features Utilizadas: ['Temperatura_C', 'Precipitacao_mm', 'Feriado', 'Ferias_Escolares', 'Dia_da_Semana'].

Performance Final:

R² Score: 0.93 (O modelo explica 93% da variabilidade das vendas).

Erro Médio Absoluto (MAE): 16.77 sorvetes (Uma margem de erro excelente para o planejamento de produção).

🚀 7. Como Executar o Projeto
Instrução: Siga os passos abaixo para rodar o pipeline de Machine Learning.

Clone o repositório:

Bash

git clone https://github.com/seu-usuario/gelato-magico-predict.git
cd gelato-magico-predict
Crie um ambiente virtual e instale as dependências:

Bash

python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
Execute o pipeline de treinamento:

Primeiro, gere o dataset: python src\data\make_dataset.py

Em seguida, treine o modelo: python -m src.models.train_model

Visualize os experimentos:

Bash

mlflow ui
Abra http://127.0.0.1:5000 no seu navegador.

✒️ 8. Autor
Mariana Ferreira Faria

LinkedIn: [link-do-seu-linkedin]
GitHub: [link-do-seu-github] 
