menu = """

Olá, bem vindo ao Banco Digital
 Selecione a opcao desejada:

   [d] Depositar
   [s] Sacar
   [e] Extrato
   [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITES_SAQUE_DIARIO = 3


while True:

    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito:  "))

        if valor >0: 
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
           print("Operação falhou! O valor informado é inválido.")
           
               

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
    
        excedeu_saldo = valor > saldo
    
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_de_saques >= LIMITES_SAQUE_DIARIO
    
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Numero máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1

        else:
           print("Operação falhou! O valor informado não é válido")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nsaldo: R${saldo:.2f}")    
        print("=============================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operacao desejada.")