# APS - Desenvolvimento de um Sistema para Análise de Performance de Algoritmos de detecção.

# -------------------------
## Descrição
# -------------------------

Este projeto foi desenvolvido como parte da disciplina de **Estrutura de Dados** e consiste em um sistema para **analisar a performance de algoritmos de detecção de desmatamento na Amazônia e no Cerrado** aplicados a dados extraídos de **Arquivos CSV's** de estados e biomas brasileiros.

O projeto segue o padrão **MC** (Model-Controller) e programação **orientada a objetos**.

O sistema permite:

# ------------------------
## Desenvolvedores
# ------------------------

-> Nome: Paulo Henrique Oliveira da Silva | RA: R0767J6
- GitHub: https://github.com/PhOlivs
Responsável pela estruturação da arquitetura do projeto, revisão e organização de commits do repositório Git.

-> Kaue dos Santos Oliveira da Silva
-
Responsável pela
# -------------------------
## Estrutura do Projeto
# -------------------------

APS_4SEM/: Pasta principal do projeto.
│ requirements.txt: Esse arquivo contém todas as bibliotecas que o projeto precisa para funcionar.
│ README.md: Esse arquivo é um guia que explica do que se trata o projeto, como executar, estrutura, tecnologias e refêrencias.
│ .gitattributes: Esse arquivo define como a tecnologia Git deve tratar certos tipos de arquivos
│ .gitignore: Esse arquivo define outros arquivos e pastas que não devem ir para o Git.
│ LICENSE: Esse arquivo define os direitos de uso, distribuição e modificação do projeto por outras pessoas.
├── data: Pasta onde ficam os arquivos CSV usadas nos testes e os dados originais.
│
├── apps: Pasta principal do código-fonte.
│├── model: Pasta que guarda classes de algoritmos.
│
│├── view: Pasta que guarda a interface.
│
│├── controller: Pasta que guarda os recebimentos dos dados da interface, chamam os algoritmos e devolvem os resultado.

# -------------------------
## Tecnologias Utilizadas
# ------------------------

-> Plataforma de Hospedagem: GitHub – Plataforma de hospedagem de repositórios Git, usada para versionamento, colaboração e controle de histórico do projeto.
-> Ambiente de desenvolvimento: Visual Studio Code – Editor de código usado para desenvolver, depurar e organizar o projeto.
-> Sistema de versionamento Git: versão 2.49.0 – Sistema de controle de versionamento e colaboração no projeto.
-> Linguagem Python: versão 3.13.1 – Linguagem de programação utilizada no projeto.
- Biblioteca NumPy: versão 2.2.2 – Biblioteca para manipulação de arrays e cálculos matemáticos.
- Biblioteca Pandas: versão 2.2.3 – Biblioteca para análise e manipulação de dados.
- Biblioteca Matplotlib: versão 3.10.0 – Biblioteca para criação e visualização de dados.
- Biblioteca Scikit-Learn: versão 1.7.1 – Biblioteca para ferramentas simples e eficientes para análise preditiva de dados.
- Biblioteca Seaborn: versão 0.13.2 - Biblioteca para visualização de dados Python baseada em matplotlib.
- Biblioteca Streamlit: versão 1.48.1 - Biblioteca para criar e compartilhar aplicativos e visualizações dinâmicas.

# ------------------------
## Como Executar
# ------------------------

1. Clonar o repositório:
git clone: colocar o link.
cd colocar o caminho.

2. Criar ambiente virtual e instalar dependências:
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt

# ------------------------
## Bibliografias do Sistema
# ------------------------

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