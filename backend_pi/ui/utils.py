import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    limpar_tela()
    print("=" * 90)
    exibir_logo()
    print("=" * 90 + "\n")

def exibir_logo():

    print(r"""
    
__________         __      __               
\______   \___.__./  \    /  \_____  ___.__.
 |     ___<   |  |\   \/\/   /\__  \<   |  |
 |    |    \___  | \        /  / __ \\___  |
 |____|    / ____|  \__/\  /  (____  / ____|
           \/            \/        \/\/      
                                                  
                                                  
    """)