"""
Arquivo de entrada da aplicação Future Skills Lab.

Este módulo inicializa o sistema de orientação e executa o menu principal.
Ao rodar `python main.py`, o usuário poderá cadastrar perfis, visualizar
recomendações de carreiras e trilhas de aprendizado, de acordo com suas
competências e interesses.
"""
from models import SistemaOrientacao

def main() -> None:
    """Ponto de entrada principal da aplicação."""
    sistema = SistemaOrientacao()
    sistema.menu_principal()

if __name__ == "__main__":
    main()
