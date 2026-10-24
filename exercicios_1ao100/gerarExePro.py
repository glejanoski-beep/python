import subprocess
import sys
from pathlib import Path


# Pasta onde este script está
pasta = Path(__file__).parent

# Pastas de saída
pasta_executaveis = pasta / "executaveis"
pasta_temporarios = pasta / "temporarios"

# Cria as pastas caso não existam
pasta_executaveis.mkdir(exist_ok=True)
pasta_temporarios.mkdir(exist_ok=True)

# Solicita o intervalo de exercícios
inicio = int(input("Digite o exercício inicial: "))
fim = int(input("Digite o exercício final: "))

# Valida o intervalo
if inicio > fim:
    print("[ERRO] O exercício inicial não pode ser maior que o final.")

else:
    # Procura os arquivos .py da pasta
    arquivos_py = pasta.glob("exercicio*.py")

    for arquivo in arquivos_py:

        # Obtém o número do exercício
        numero = arquivo.stem.replace("exercicio", "")

        # Verifica se o nome contém um número válido
        if not numero.isdigit():
            continue

        numero = int(numero)

        # Ignora exercícios fora do intervalo
        if numero < inicio or numero > fim:
            continue

        print(f"\nGerando: {arquivo.name}")

        comando = [
            sys.executable,
            "-m",
            "PyInstaller",
            "--onefile",
            "--distpath",
            str(pasta_executaveis),
            "--workpath",
            str(pasta_temporarios),
            "--specpath",
            str(pasta_temporarios),
            str(arquivo)
        ]

        resultado = subprocess.run(comando)

        if resultado.returncode == 0:
            print(f"[OK] {arquivo.name} concluído!")
        else:
            print(f"[ERRO] Erro ao gerar {arquivo.name}")

print("\nProcesso concluído!")
input("Pressione ENTER para sair...")