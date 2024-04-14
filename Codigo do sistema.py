#Sistema bancario com operações de sacar, depositar, extrato.



LIMITE_SAQUE = 3
LIMITE_VALOR = 500
saldo = 0
extrato = ""
numero_saque = 0
escolha = 0
deposito = 0

menu = """

============== BEM VINDO ==============

  [1] Depósiro
  [2] Saque
  [3] Extrato
  [0] Sair

============ BANCO DIGITAL =============

"""

while True:
    print(menu)
    escolha = int(input("Escolha uma das opções: "))

    if escolha == 1:
        deposito = int(input("Digite o valor que deseja depósitar: "))
        if deposito >0:
            print(f"Depósito no valor de {deposito} foi realizado com sucesso!")
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Valor digitado está incorreto!")

    elif escolha == 2:
        valor_saque = float(input(f"Digite o valor que deseja sacar: "))
        if valor_saque <= saldo and numero_saque <= LIMITE_SAQUE and valor_saque <= LIMITE_VALOR and valor_saque > 0:
            print(f"Saque no valor de {valor_saque} foi realizado com sucesso!")
            saldo -= valor_saque
            numero_saque += 1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
        elif valor_saque > saldo:
            print(f"""

============ ERRO ============
                  
Saldo insuficiente!
Confira seu extrato digitando [3].

       """)

        elif valor_saque <= 0:
            print("Valor digitado está incorreto")          
        elif numero_saque > LIMITE_SAQUE:
            print("Você alcançou o limite diário de saques!")
        elif valor_saque > LIMITE_VALOR:
            print(f"Seu limite diário é de R$ 500.00, não foi possível realizar o saque de {valor_saque}")
    
    elif escolha == 3:
        print("\n================== EXTRATO ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif escolha == 0:
        print("Obrigado por utilizar nossos serviços!")
        break