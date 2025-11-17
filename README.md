# Future Skills Lab – Orientação de Carreiras

Este projeto é a solução proposta para a *Global Solution 2025.2* da disciplina
**Pensamento Computacional e Automação com Python**, ministrada pelo professor
Alexandre Russi Junior. O objetivo é criar uma aplicação em Python que auxilie
estudantes e profissionais a descobrir caminhos para o **trabalho do
futuro**, analisando competências técnicas e comportamentais e sugerindo
carreiras e trilhas de aprimoramento.

## Descrição do projeto

O **Future Skills Lab** é um sistema orientado a objetos que organiza
informações sobre competências, perfis de usuários e carreiras emergentes.
Utilizando estruturas como listas, tuplas e dicionários, a aplicação coleta
informações do usuário por meio de uma interface de linha de comando (CLI),
calcula pontuações de compatibilidade e apresenta recomendações de carreira e
atividades de estudo. A proposta está alinhada ao tema **“Future at Work”**,
explorando como a lógica de programação e a automação podem apoiar o
desenvolvimento humano e profissional.

### Funcionalidades principais

- **Cadastro de perfis:** o usuário informa seu nome e avalia seu nível em
  diversas competências (de 1 a 5).
- **Listagem de perfis:** visualiza os perfis já cadastrados na sessão.
- **Recomendações de carreira:** com base nos níveis informados, o sistema
  calcula uma pontuação de compatibilidade e sugere as carreiras mais
  adequadas.
- **Trilhas de aprimoramento:** identifica as competências com notas baixas e
  apresenta sugestões de cursos e atividades para evolução.

## Estrutura do código

A solução foi organizada em módulos para facilitar a manutenção e a legibilidade:

| Arquivo            | Descrição                                                                 |
|-------------------|----------------------------------------------------------------------------|
| `models.py`       | Define as classes **Competencia**, **Carreira**, **Perfil** e **SistemaOrientacao**, encapsulando dados e lógica do sistema. |
| `main.py`         | Ponto de entrada da aplicação. Instancia `SistemaOrientacao` e inicia o menu interativo. |
| `README.md`       | Este documento com a descrição, instruções de uso e demonstração.          |
| `integrantes.txt` | Arquivo contendo os nomes e RMs dos integrantes, além do link do repositório. |

### Classes principais

- **Competencia** – representa uma habilidade técnica ou comportamental (nome,
  categoria e descrição).
- **Carreira** – agrupa competências requeridas com pesos e oferece uma trilha
  de aprendizado específica. Possui método para calcular a pontuação de
  compatibilidade com o perfil do usuário.
- **Perfil** – armazena o nome do usuário e suas competências avaliadas.
- **SistemaOrientacao** – gerencia as coleções de competências, carreiras e
  perfis, oferecendo métodos para cadastrar novos perfis, gerar recomendações
  de carreira, sugerir trilhas de aprimoramento e executar o menu principal.

## Como executar

1. Certifique‑se de ter o **Python 3.10** (ou superior) instalado em seu ambiente.
2. Clone ou baixe este repositório para sua máquina.
3. No terminal, navegue até a pasta `future_skills_lab` e execute:

```bash
python3 main.py
