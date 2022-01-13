# Faça um mini-sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

#Resolução

def pyhelp():
   while True:
        print('-' * 30)
        print('\033[0;30;41mSistema de ajuda PyHELP')
        print('-'* 30)
        f = str(input('\033[0;31;42mFunção ou biblioteca: ')).strip().lower()
        if f in 'fim':
            print('Até logo!')
            break
        f'\033[0;30;41m{help(f)}'

        
pyhelp()