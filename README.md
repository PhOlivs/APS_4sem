# APS - Desenvolvimento de um Sistema para Análise de Performance de Algoritmos de Ordenação de Dados

# -------------------------
## Descrição
# -------------------------

Este projeto foi desenvolvido como parte da disciplina de **Estrutura de Dados** e consiste em um sistema para **analisar a performance de algoritmos de ordenação** aplicados a dados extraídos de **imagens de satélite** de estados e biomas brasileiros.

O sistema permite:

O projeto segue o padrão **MVC** (Model-View-Controller) e programação **orientada a objetos**.

# ------------------------
## Desenvolvedores
# ------------------------

-> Nome: Paulo Henrique Oliveira da Silva | RA: R0767J6
- GitHub: https://github.com/PhOlivs
Responsável pela estruturação da arquitetura do projeto, revisão e organização de commits do repositório Git.

# -------------------------
## Estrutura do Projeto
# -------------------------

APS_4SEM/: Pasta principal do projeto.
│ requirements.txt: Esse arquivo contém todas as bibliotecas que o projeto precisa para funcionar.
│ README.md: Esse arquivo é um guia que explica do que se trata o projeto, como executar, estrutura, tecnologias e refêrencias.
│ .gitattributes: Esse arquivo define como a tecnologia Git deve tratar certos tipos de arquivos
│ .gitignore: Esse arquivo define outros arquivos e pastas que não devem ir para o Git.
│ LICENSE: Esse arquivo define os direitos de uso, distribuição e modificação do projeto por outras pessoas.
├── imagens: Pasta onde ficam as imagens de satélite usadas nos testes.
│
├── apps: Pasta principal do código-fonte.
│├── model: Pasta que guarda classes de algoritmos de ordenação.
│
│├── view: Pasta que guarda a interface.
│
│├── controller: Pasta que guarda os recebimentos dos dados da interface, chamam os algoritmos e devolvem os resultado.

# -------------------------
## Tecnologias Utilizadas
# ------------------------

-> Plataforma de Hospedagem: GitHub
-> Ambiente de desenvolvimento: Visual Studio Code
-> Sistema de versionamento Git: versão 2.49.0

-> Linguagem Python: versão 3.13.1
- Biblioteca NumPy: versão 2.2.2

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

Visual Studio Code – Editor de código usado para desenvolver, depurar e organizar o projeto.
https://code.visualstudio.com/
Python – Linguagem de programação utilizada no projeto.
https://www.python.org/
Git – Sistema de controle de versão distribuído utilizado para versionamento e colaboração no projeto.
https://git-scm.com/
NumPy – Biblioteca para manipulação de arrays e cálculos matemáticos.
https://numpy.org/
GitHub – Plataforma de hospedagem de repositórios Git, usada para versionamento, colaboração e controle de histórico do projeto.
https://github.com/