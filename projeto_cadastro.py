from datetime import datetime

encerrar = " "
while True:
    opções= print('''Escolha as opções :
                     [1]cadastro
                     [2]exclui cadastro
                         
                                     
                     ''')
    escolha= input("Escolha aqui sua opção: ")
    
    if escolha == "1":
            print("Olá, seja bem vindo!")
            nome = input("Por favor, digite seu nome? ")
            idade = input("Por favor digite sua idade: ")
            print("Seu nome é {} e sua idade {} anos.".format(nome, idade))
            data = datetime.now()
            print(" Cadastro feito em: {}".format(data.strftime("%Y-%m-%d %H:%M:%S")))
                
    elif escolha == "2":
            del escolha 
            print("Cadastro excluído!")
            break
    
                
    encerrar = input("Deseja encerrar o programa [s/n]")        
    if encerrar == 's':
            break
    else:
            continue
print(f'Obrigado {nome}!')
print("Cadastro Finalizado!")
            

            
        
         
        

            
        
