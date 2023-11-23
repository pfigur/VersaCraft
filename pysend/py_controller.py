import utils


def pergunta_env():
    yes = {'yes', 'y', 's'}
    no = {'no', 'n'}

    choice = input('Deseja usar algum ambiente virtual? (S/N)').lower()

    if choice in yes:
        com_env()
    elif choice in no:
        print("Então não né")
    else:
        print("Inválido\n")
        pergunta_env()


def com_env():
    choice = input('Qual ambiente virtual deseja usar?\n'
                   '1 - VENV\n'
                   '2 - VirtualEnv\n')

    try:
        match int(choice):
            case 1:
                venv()
            case 2:
                virtualenv()
            case _:
                print('Inválido\n')
                com_env()
    except:
        com_env()


def venv():
    print('venv')


def virtualenv():
    print('viertualenv')
