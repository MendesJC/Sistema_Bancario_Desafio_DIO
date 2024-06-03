menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.00
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        print("Por favor, informe o valor do depósito:")
        
        try: 
            valor_deposito = float(input())
        except ValueError:
            print("Desculpe, não foi possível realizar esta operação.")
            continue
    
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"\nDepósito de R$ {valor_deposito:.2f}."
            print("Depósito realizado com sucesso.")
        else:
            print("Desculpe, não foi possível realizar esta operação.")       

    elif opcao == "s":
        if (numero_saques < LIMITE_SAQUES):      
            print("Por favor, informe o valor do saque:")
            try: 
                valor_saque = float(input())
            except ValueError:
                print("Desculpe, não foi possível realizar esta operação.")
                continue            
            
            if (valor_saque<=saldo) and (valor_saque>0) and (valor_saque<=limite):
                saldo -= valor_saque
                extrato += f"\nSaque de R$ {valor_saque:.2f}."
                numero_saques += 1
                print("Saque realizado com sucesso.\nPor favor retire o dinheiro!")
            
            elif(valor_saque > limite):
                print("Desculpe, não foi possível realizar esta operação.\nO seu limite de saque é R$ 500.00!")
            
            elif(valor_saque > saldo):
                print(f"Desculpe, não foi possível realizar esta operação.\nO saque solicitado excede o seu saldo.\nO seu saldo atual é R$ {saldo:.2f}.")    
            
            else:
                print("Desculpe, não foi possível realizar esta operação.")
            
        else:
            print("Desculpe, não foi possível realizar esta operação.\nO limite diário de saques já foi realizado!")
        
    elif opcao == "e":
        print(f"""
Confira o seu extrado atual:

{extrato}

O saldo atual da sua conta é R$ {saldo:.2f}.
              """)
        
    elif opcao == "q":
        print("""
Obrigado por ser nosso client!
Tenha um ótimo dia!            
              """)
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")