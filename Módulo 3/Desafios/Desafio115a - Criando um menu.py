# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from time import sleep

def menu():
    while True:
        try:
            print('-'*30)
            print(f"{'MENU PRINCIPAL':^30}")
            print('-'*30)
            print('\033[33m1\033[m - \033[36mVer pessoas cadastradas\033[m')
            print('\033[33m2\033[m - \033[36mCadastrar nova pessoa\033[m')
            print('\033[33m3\033[m - \033[36mSair do sistema\033[m')
            print('-'*30)
            opt = int(input('\033[33mSua opção: \033[m'))
            print('-'*30)
            sleep(0.5)
            if opt == 1:
                print('-'*30)
                print(f"{'Opção 1':^30}")
                print('-'*30)
            elif opt == 2:
                print('-'*30)
                print(f"{'Opção 2':^30}")
                print('-'*30)
            elif opt == 3:
                print('-'*30)
                print(f"{'Saindo do sistema...':^30}")
                print('-'*30)
                break
            else:
                print('Opção inválida. Digite uma opção válida.')
        except:
            print('Opção inválida. Digite uma opção válida.')
            


menu()