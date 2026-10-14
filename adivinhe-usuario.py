import random
import time
from colorama import Fore, Style, init

# Inicializa a biblioteca colorama (necessário no Windows/VS Code)
init(autoreset=True)

# Definição dos estilos visuais usando Tons de Azul e Verde
C_AZUL = Fore.LIGHTBLUE_EX
C_VERDE = Fore.LIGHTGREEN_EX
C_AZUL_ESCURO = Fore.BLUE
C_VERDE_ESCURO = Fore.GREEN
C_TEXTO = Fore.CYAN
NEGRITO = Style.BRIGHT

def exibir_cabecalho():
    print(f"{C_AZUL}{NEGRITO}=" * 55)
    print(f"{C_VERDE}{NEGRITO}  🎮 JOGO: ADIVINHE O NÚMERO (EDIÇÃO AZUL & VERDE) 🎯")
    print(f"{C_AZUL}{NEGRITO}=" * 55)
    print(f"{C_TEXTO} Tente adivinhar o número secreto entre {C_VERDE}1{C_TEXTO} e {C_VERDE}100{C_TEXTO}!\n")

def jogar():
    exibir_cabecalho()
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print(f"{C_AZUL}[INFO] {C_TEXTO}O computador já escolheu um número...")
    time.sleep(1)
    print(f"{C_VERDE}[PRONTO] {C_TEXTO}Boa sorte! Vamos começar.\n")

    while not acertou:
        try:
            palpite_str = input(f"{C_AZUL}{NEGRITO}👉 Digite o seu palpite: {C_VERDE}")
            palpite = int(palpite_str)
            tentativas += 1

            if palpite < 1 or palpite > 100:
                print(f"{C_AZUL}⚠️  Por favor, digite um número entre 1 e 100!\n")
                continue

            if palpite == numero_secreto:
                acertou = True
                print(f"\n{C_VERDE}{NEGRITO}=" * 55)
                print(f"{C_VERDE}{NEGRITO} 🎉 PARABÉNS! VOCÊ ACERTOU! 🎉")
                print(f"{C_AZUL} 🔢 Número secreto: {C_VERDE}{NEGRITO}{numero_secreto}")
                print(f"{C_AZUL} 🎯 Total de tentativas: {C_VERDE}{NEGRITO}{tentativas}")
                print(f"{C_VERDE}{NEGRITO}=" * 55)
            elif palpite < numero_secreto:
                print(f"{C_AZUL}⬆️  O número secreto é {NEGRITO}MAIOR{Style.RESET_ALL}{C_AZUL} que {palpite}.\n")
            else:
                print(f"{C_VERDE_ESCURO}⬇️  O número secreto é {NEGRITO}MENOR{Style.RESET_ALL}{C_VERDE_ESCURO} que {palpite}.\n")

        except ValueError:
            print(f"{C_AZUL}❌ Entrada inválida! Digite apenas números inteiros.\n")

if __name__ == "__main__":
    jogar()