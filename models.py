"""
Modelos de dados para a aplicação Future Skills Lab.

Este módulo contém as classes que representam competências, perfis de usuários e
carreiras. Cada classe encapsula os atributos e comportamentos necessários
para organizar as informações utilizadas no sistema de orientação de
carreiras.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Competencia:
    """Representa uma competência técnica ou comportamental.

    Attributes:
        nome: Nome descritivo da competência.
        categoria: Categoria da competência (por exemplo, 'Técnica' ou
            'Comportamental').
        descricao: Breve descrição da competência.
    """
    nome: str
    categoria: str
    descricao: str

@dataclass
class Carreira:
    """Representa uma carreira ou função profissional.

    Cada carreira define um conjunto de competências requeridas com pesos
    associados, além de uma trilha de aprendizado recomendada para quem
    deseja se aprimorar nessa área.

    Attributes:
        nome: Nome da carreira (ex.: 'Cientista de Dados').
        competencias_requeridas: Dicionário que mapeia o nome da competência
            para um peso entre 0 e 1, indicando sua importância.
        trilha: Lista de sugestões de cursos ou atividades para evoluir na
            carreira.
    """
    nome: str
    competencias_requeridas: Dict[str, float]
    trilha: List[str] = field(default_factory=list)

    def calcular_pontuacao(self, competencias_perfil: Dict[str, int]) -> float:
        """Calcula uma pontuação de compatibilidade com base nas competências do perfil."""
        soma_pesos = sum(self.competencias_requeridas.values())
        if soma_pesos == 0:
            return 0.0
        total = 0.0
        for comp, peso in self.competencias_requeridas.items():
            nivel = competencias_perfil.get(comp, 0)
            total += (nivel / 5) * peso  # normaliza nota (1–5) para 0–1
        return (total / soma_pesos) * 100  # retorna porcentagem

@dataclass
class Perfil:
    """Representa um perfil de usuário que será analisado pelo sistema."""
    nome: str
    competencias: Dict[str, int] = field(default_factory=dict)

    def adicionar_competencia(self, competencia: str, nivel: int) -> None:
        """Adiciona ou atualiza o nível de uma competência no perfil."""
        self.competencias[competencia] = nivel

class SistemaOrientacao:
    """Gerencia perfis, competências e carreiras, fornecendo recomendações."""
    def __init__(self) -> None:
        self.competencias: Dict[str, Competencia] = {}
        self.carreiras: List[Carreira] = []
        self.perfis: List[Perfil] = []
        self.trilhas_competencias: Dict[str, List[str]] = {}
        self._carregar_dados_padrao()

    def _carregar_dados_padrao(self) -> None:
        """Inicializa competências, carreiras e trilhas padrão."""
        competencias_definidas = [
            Competencia("Lógica de Programação", "Técnica",
                        "Capacidade de entender algoritmos e estruturas lógicas"),
            Competencia("Criatividade", "Comportamental",
                        "Habilidade de propor soluções inovadoras e originais"),
            Competencia("Colaboração", "Comportamental",
                        "Trabalhar bem em equipe e compartilhar conhecimento"),
            Competencia("Adaptabilidade", "Comportamental",
                        "Capacidade de se ajustar rapidamente a mudanças"),
            Competencia("Pensamento Analítico", "Técnica",
                        "Analisar dados e problemas de forma estruturada"),
            Competencia("Inteligência Artificial", "Técnica",
                        "Conhecimento em algoritmos e ferramentas de IA"),
            Competencia("Comunicação", "Comportamental",
                        "Expressar ideias de forma clara e objetiva"),
            Competencia("Resolução de Problemas", "Comportamental",
                        "Diagnosticar e resolver problemas de forma eficaz"),
            Competencia("Curiosidade", "Comportamental",
                        "Desejo contínuo de aprender coisas novas"),
            Competencia("Liderança", "Comportamental",
                        "Influenciar e motivar pessoas para atingir objetivos"),
        ]
        for comp in competencias_definidas:
            self.competencias[comp.nome] = comp

        # Trilhas por competência
        self.trilhas_competencias = {
            "Lógica de Programação": [
                "Curso introdutório de lógica no Codecademy",
                "Resolver desafios em plataformas como HackerRank ou LeetCode",
            ],
            "Criatividade": [
                "Praticar brainstormings e design thinking",
                "Participar de workshops de inovação",
            ],
            "Colaboração": [
                "Trabalhar em projetos em equipe",
                "Estudar metodologias ágeis",
            ],
            "Adaptabilidade": [
                "Participar de cursos sobre gestão de mudanças",
                "Exercitar flexibilidade em projetos multidisciplinares",
            ],
            "Pensamento Analítico": [
                "Aprender estatística básica e análise de dados",
                "Praticar interpretação de dashboards e gráficos",
            ],
            "Inteligência Artificial": [
                "Fazer um curso de introdução ao Machine Learning",
                "Explorar bibliotecas de IA como TensorFlow ou PyTorch",
            ],
            "Comunicação": [
                "Participar de debates e apresentações",
                "Estudar técnicas de storytelling",
            ],
            "Resolução de Problemas": [
                "Praticar lógica e quebra-cabeças",
                "Aplicar metodologias como Design Thinking",
            ],
            "Curiosidade": [
                "Ler artigos de diferentes áreas regularmente",
                "Explorar novos hobbies e ferramentas",
            ],
            "Liderança": [
                "Participar de cursos de gestão de equipes",
                "Ler biografias de líderes inspiradores",
            ],
        }

        # Carreiras e seus pesos de competências
        self.carreiras = [
            Carreira(
                nome="Cientista de Dados",
                competencias_requeridas={
                    "Lógica de Programação": 0.25,
                    "Pensamento Analítico": 0.30,
                    "Curiosidade": 0.10,
                    "Colaboração": 0.10,
                    "Resolução de Problemas": 0.25,
                },
                trilha=[
                    "Curso de programação em Python",
                    "Especialização em ciência de dados e estatística",
                    "Projetos práticos de análise de dados",
                ],
            ),
            Carreira(
                nome="Engenheiro de Software",
                competencias_requeridas={
                    "Lógica de Programação": 0.30,
                    "Resolução de Problemas": 0.25,
                    "Colaboração": 0.15,
                    "Adaptabilidade": 0.15,
                    "Comunicação": 0.15,
                },
                trilha=[
                    "Curso avançado de programação orientada a objetos",
                    "Prática de versionamento com Git e GitHub",
                    "Contribuição para projetos open source",
                ],
            ),
            Carreira(
                nome="Designer de UX",
                competencias_requeridas={
                    "Criatividade": 0.30,
                    "Comunicação": 0.20,
                    "Curiosidade": 0.10,
                    "Colaboração": 0.20,
                    "Adaptabilidade": 0.20,
                },
                trilha=[
                    "Cursos de design de interface e experiência do usuário",
                    "Estudos de usabilidade e comportamento do usuário",
                    "Construção de portfólio com projetos de design",
                ],
            ),
            Carreira(
                nome="Especialista em Cibersegurança",
                competencias_requeridas={
                    "Lógica de Programação": 0.20,
                    "Pensamento Analítico": 0.30,
                    "Resolução de Problemas": 0.30,
                    "Adaptabilidade": 0.20,
                },
                trilha=[
                    "Formação em segurança da informação",
                    "Certificações como CEH ou CompTIA Security+",
                    "Prática em ambientes de captura a bandeira (CTF)",
                ],
            ),
            Carreira(
                nome="Engenheiro de Machine Learning",
                competencias_requeridas={
                    "Lógica de Programação": 0.20,
                    "Inteligência Artificial": 0.40,
                    "Pensamento Analítico": 0.25,
                    "Curiosidade": 0.15,
                },
                trilha=[
                    "Curso intensivo de Machine Learning",
                    "Projetos de IA aplicados a problemas reais",
                    "Estudo de algoritmos avançados de aprendizado",
                ],
            ),
            Carreira(
                nome="Empreendedor Tecnológico",
                competencias_requeridas={
                    "Criatividade": 0.30,
                    "Liderança": 0.30,
                    "Adaptabilidade": 0.20,
                    "Comunicação": 0.20,
                },
                trilha=[
                    "Cursos de empreendedorismo e inovação",
                    "Participação em hackathons e incubadoras",
                    "Leitura sobre modelos de negócio e startups",
                ],
            ),
        ]

    def cadastrar_perfil(self, nome: str) -> Perfil:
        """Cria um novo perfil solicitando os níveis de cada competência."""
        perfil = Perfil(nome)
        print(f"\nCadastro de competências para {nome}:")
        for comp_nome in self.competencias.keys():
            while True:
                try:
                    valor_str = input(
                        f"Informe seu nível em '{comp_nome}' (1-5): "
                    ).strip()
                    valor = int(valor_str)
                    if 1 <= valor <= 5:
                        perfil.adicionar_competencia(comp_nome, valor)
                        break
                except ValueError:
                    pass
                print("Entrada inválida. Por favor, insira um número entre 1 e 5.")
        self.perfis.append(perfil)
        print(f"\nPerfil '{nome}' cadastrado com sucesso!\n")
        return perfil

    def listar_perfis(self) -> None:
        """Exibe todos os perfis cadastrados no sistema."""
        if not self.perfis:
            print("Nenhum perfil cadastrado até o momento.\n")
            return
        print("\nPerfis cadastrados:")
        for idx, perfil in enumerate(self.perfis, start=1):
            print(f"{idx}. {perfil.nome}")
        print("")

    def recomendar_carreiras(self, perfil: Perfil, limite: int = 3) -> List[str]:
        """Gera recomendações de carreiras mais compatíveis com o perfil."""
        resultados = []
        for carreira in self.carreiras:
            pontuacao = carreira.calcular_pontuacao(perfil.competencias)
            resultados.append((pontuacao, carreira))
        resultados.sort(reverse=True, key=lambda item: item[0])  # ordena decrescente
        mensagens = []
        for pontuacao, carreira in resultados[:limite]:
            mensagens.append(
                f"{carreira.nome} - Compatibilidade: {pontuacao:.1f}%"
            )
        return mensagens

    def recomendar_trilhas_aprimoramento(self, perfil: Perfil) -> List[str]:
        """Sugere trilhas de aprendizado para as competências mais baixas do perfil."""
        recomendacoes = []
        for comp_nome, nivel in perfil.competencias.items():
            if nivel < 3:
                trilhas = self.trilhas_competencias.get(comp_nome, [])
                if trilhas:
                    recomendacoes.append(
                        f"Para melhorar em '{comp_nome}', considere: " +
                        ", ".join(trilhas)
                    )
        return recomendacoes

    def menu_principal(self) -> None:
        """Exibe o menu principal e executa as operações escolhidas pelo usuário."""
        while True:
            print("""
========= Future Skills Lab =========
1. Cadastrar novo perfil
2. Listar perfis cadastrados
3. Gerar recomendações de carreira
4. Gerar trilhas de aprimoramento
5. Sair
""")
            escolha = input("Escolha uma opção: ").strip()
            if escolha == "1":
                nome = input("Digite seu nome: ").strip()
                if nome:
                    self.cadastrar_perfil(nome)
            elif escolha == "2":
                self.listar_perfis()
            elif escolha == "3":
                if not self.perfis:
                    print("Cadastre um perfil antes de gerar recomendações.\n")
                    continue
                self.listar_perfis()
                try:
                    idx = int(
                        input(
                            "Informe o número do perfil para ver as recomendações: "
                        ).strip()
                    )
                    perfil = self.perfis[idx - 1]
                except (ValueError, IndexError):
                    print("Perfil inválido.\n")
                    continue
                mensagens = self.recomendar_carreiras(perfil)
                print(f"\nRecomendações de carreira para {perfil.nome}:")
                for msg in mensagens:
                    print(f"- {msg}")
                print("")
            elif escolha == "4":
                if not self.perfis:
                    print("Cadastre um perfil antes de gerar trilhas de aprimoramento.\n")
                    continue
                self.listar_perfis()
                try:
                    idx = int(
                        input(
                            "Informe o número do perfil para ver as trilhas de aprimoramento: "
                        ).strip()
                    )
                    perfil = self.perfis[idx - 1]
                except (ValueError, IndexError):
                    print("Perfil inválido.\n")
                    continue
                recomendacoes = self.recomendar_trilhas_aprimoramento(perfil)
                if not recomendacoes:
                    print(
                        f"{perfil.nome} não possui competências com nota baixa. Parabéns!\n"
                    )
                else:
                    print(f"\nTrilhas de aprimoramento para {perfil.nome}:")
                    for rec in recomendacoes:
                        print(f"- {rec}")
                    print("")
            elif escolha == "5":
                print("Saindo... obrigado por utilizar o Future Skills Lab!")
                break
            else:
                print("Opção inválida. Tente novamente.\n")
