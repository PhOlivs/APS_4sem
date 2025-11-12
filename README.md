# APS - Desenvolvimento de um Sistema para Análise de Performance de Algoritmos de Detecção

## Desenvolvedores

**Nome:** Paulo Henrique Oliveira da Silva | **RA:** R0767J6  
- **GitHub:** [PhOlivs](https://github.com/PhOlivs)  
Responsável pela estruturação da arquitetura do projeto, revisão, organização de commits do repositório Git e desenvolvimento geral.

**Nome:** Kauê dos Santos Oliveira da Silva | **RA:** T478GB  
- **GitHub:** [Kaue-Oliveira19](https://github.com/Kaue-Oliveira19)  
Responsável pelo suporte no desenvolvimento, documentação e testes do sistema.

---

## Índice
+ [Sobre](#sobre)
+ [Como Executar](#como-executar)
+ [Features](#features)
+ [Instalação](#instalação)
+ [Tecnologias Utilizadas](#tecnologias-utilizadas)
+ [Bibliografias do Sistema](#bibliografias-do-sistema)

---

## Sobre <a name="sobre"></a>

Este projeto foi desenvolvido como parte da disciplina de **Estrutura de Dados** e consiste em um sistema para **analisar a performance de algoritmos de detecção de desmatamento na Amazônia e no Cerrado**, aplicados a dados extraídos de **arquivos CSV** contendo informações sobre diferentes estados e biomas brasileiros.

O projeto segue o padrão **MVC** (Model-View-Controller) e programação **orientada a objetos**, com foco em modularidade, organização e boas práticas de versionamento no Git.

---

## Como Executar <a name="como-executar"></a>

Estas instruções permitirão que você tenha uma cópia funcional do projeto na sua máquina local para desenvolvimento e testes.

### Pré-requisitos

- **Python** versão 3.13.1  
- Executar o comando abaixo no terminal para instalar as dependências:

```bash
pip install -r requirements.txt

Features <a name="features"></a>

Painel interativo em Streamlit com filtros por ano e estado.

Indicadores principais (KPIs) de desmatamento.

Gráficos interativos:

Linha temporal por estado

Barras comparativas

Heatmap de desmatamento

Previsão de desmatamento usando Random Forest

Estrutura organizada em MVC + design pattern, separando:

Model → modelagem e machine learning

View → interface do usuário

Controller → lógica de negócio e manipulação de dados

Suporte a caminhos relativos para execução em qualquer máquina.

Gráficos e KPIs responsivos e visualmente limpos, com agrupamento por estado e opção “outros”.

Instalação <a name="instalação"></a>

Passo a passo para executar o projeto:

Clone o repositório:
git clone https://github.com/PhOlivs/APS_4sem.git
cd APS_4sem

Instale as dependências:
pip install -r requirements.txt

Garanta que os arquivos CSV e modelos estejam na pasta correta:
data/desmatamento_tratado.csv
data/datamodelo_random_forest.pkl
data/datascaler.pkl

Execute o sistema:
streamlit run app.py

Tecnologias Utilizadas <a name="tecnologias-utilizadas"></a>

Plataforma de Hospedagem: GitHub – para versionamento, colaboração e controle de histórico.

Ambiente de Desenvolvimento: Visual Studio Code – editor de código usado para desenvolvimento e depuração.

Sistema de Versionamento: Git (versão 2.49.0).

Linguagem de Programação: Python (versão 3.13.1).

Plataforma de Desenvolvimento: Jupyter Notebook (versão 2025.9.0).

Bibliotecas

NumPy: 2.2.2 – manipulação de arrays e cálculos matemáticos.

Pandas: 2.2.3 – análise e manipulação de dados.

Matplotlib: 3.9.2 – visualização de dados.

Scikit-Learn: 1.7.1 – ferramentas para aprendizado de máquina e análise preditiva.

Seaborn: 0.13.2 – visualização estatística baseada em Matplotlib.

Streamlit: 1.48.1 – criação de aplicativos web interativos.

Scipy: 1.16.1 – cálculos científicos e estatísticos.

Joblib: 1.5.1 – serialização e carregamento eficiente de objetos Python.

Plotly: 5.24.1 – visualizações interativas avançadas.
