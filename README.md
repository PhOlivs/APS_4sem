## Desenvolvedor

-> Nome: Paulo Henrique Oliveira da Silva | RA: R0767J6
- GitHub: https://github.com/PhOlivs
Responsável pela estruturação da arquitetura do projeto, revisão, organização de commits do repositório Git e desenvolvimento no geral.

# APS - Desenvolvimento de um Sistema para Análise de Performance de Algoritmos de detecção

## Índice
+ [Sobre](#sobre)
+ [Primeiros Passos](#primeiros_passos)
+ [Uso](#uso)
+ [Bibliografia](#bibliografias-do-sistema)

## Sobre <a name = "sobre"></a>
Este projeto foi desenvolvido como parte da disciplina de **Estrutura de Dados** e consiste em um sistema para **analisar a performance de algoritmos de detecção de desmatamento na Amazônia e no Cerrado** aplicados a dados extraídos de **Arquivos CSV's** de estados e biomas brasileiros.

O projeto segue o padrão **MC** (Model-Controller) e programação **orientada a objetos**.

## Começando <a name = "comecando"></a>
Estas intruçōes te darão uma cópia funcional do projeto na sua máquina local para desenvolvimento e testes. Veja [deployment](#deployment) para uma descrição de como realizar o deployment deste projeto online.

### Pré-requisitos

Descreva o que é necessário para instalar este software e como instalá-lo.

```
Python - versão 3.13.1
Executar no terminal: pip install -r requirements.txt
```

### Features

1) Painel interativo em Streamlit com filtros por ano e estado.
2) Indicadores principais (KPIs) de desmatamento.
3) Gráficos interativos:
4) Linha temporal por estado
- Barras comparativas
- Heatmap de desmatamento
- Previsão de desmatamento usando Random Forest.

5) Estrutura organizada em MVC + design pattern, separando:
- Model → modelagem e ML
- View → interface do usuário
- Controller → lógica de negócio e manipulação de dados

6) Suporte a caminhos relativos para facilitar execução em qualquer máquina.
7) Gráficos e KPIs responsivos e visualmente limpos, com possibilidade de agrupar estados e visualizar “outros”.

### Instalação
Passo-a-passo com exemplos que reproduzam um estágio de desenvolvimento funcional.

1) Clone o repositório:

```
git clone https://github.com/seu-usuario/APS_4sem.git
cd APS_4sem
```

2) Instale as dependências:

```
pip install -r requirements.txt
```

3) Garanta que os arquivos CSV e modelos estejam na pasta correta:

```
data/dematamento_tratado.csv
data/datamodelo_random_forest.pkl
data/datascaler.pkl
```
4) Como rodar:

```
streamlit run app.py
```


## Tecnologias Utilizadas

-> Plataforma de Hospedagem: GitHub – Plataforma de hospedagem de repositórios Git, usada para versionamento, colaboração e controle de histórico do projeto.  
-> Ambiente de desenvolvimento: Visual Studio Code – Editor de código usado para desenvolver, depurar e organizar o projeto.  
-> Sistema de versionamento Git: versão 2.49.0 – Sistema de controle de versionamento e colaboração no projeto.  
-> Linguagem Python: versão 3.13.1 – Linguagem de programação utilizada no projeto.
-> Plataforma de desenvolvimento: Jupyter Notebook: versão 2025.9.0 - Editor de código usado para desenvolver, depurar e organizar o projeto.   
- Biblioteca NumPy: versão 2.2.2 – Biblioteca para manipulação de arrays e cálculos matemáticos.
- Biblioteca Pandas: versão 2.2.3 – Biblioteca para análise e manipulação de dados.
- Biblioteca Matplotlib: versão 3.10.0 – Biblioteca para criação e visualização de dados.
- Biblioteca Scikit-Learn: versão 1.7.1 – Biblioteca para ferramentas simples e eficientes para análise preditiva de dados.
- Biblioteca Seaborn: versão 0.13.2 - Biblioteca para visualização de dados Python baseada em matplotlib.
- Biblioteca Streamlit: versão 1.48.1 - Biblioteca para criar e compartilhar aplicativos e visualizações dinâmicas.
- Biblioteca Scipy:  versão 1.16.1 - É uma biblioteca científica, serve para cálculos matemáticos avançados, estatística e análise científica.
- Biblioteca Joblib: versão 1.5.1 - É uma biblioteca para salvar e carregar objetos do Python de forma eficiente.

## Bibliografias do Sistema

Visual Studio Code
https://code.visualstudio.com/  
Python
https://www.python.org/  
Git
https://git-scm.com/  
NumPy
https://numpy.org/  
GitHub
https://github.com/  
Pandas
https://pandas.pydata.org/  
Matplotlib
https://matplotlib.org/  
Scikit-Learn
https://scikit-learn.org/stable/  
Seaborn
https://seaborn.pydata.org/  
Streamlit
https://streamlit.io/  
Scipy
https://scipy.org/  
joblib
https://joblib.readthedocs.io/en/stable/  
Base de Dados - Kaggle
https://www.kaggle.com/datasets/fidelissauro/desmatamento-brasil  
Jupyter
https://jupyter.org/