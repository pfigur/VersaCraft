from typer import Typer, Argument, Context, Option, Exit
import subprocess


def send_command(command):
    try:
        resultado = subprocess.run(command, check=True, text=True, capture_output=True)
        print("Saída padrão:")
        print(resultado.stdout)
        if resultado.stderr:
            print("Saída de erro:")
            print(resultado.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {e}")


def venv(dir):
    """ TODO: Criar um ambiente virtual VENV: 
           # python3 -m venv venv
     """
    com = ['ls', '-l']
    send_command(com)
    pass
