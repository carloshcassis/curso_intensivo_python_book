mensagem = "digite sua idade ou 'quit' para sair: "

while True:
    idade = input(mensagem)
    if idade == 'quit':
        break
    idade = int(idade)    
    if idade < 3 :
            print('ingresso gratuito  =)')
    
    elif idade >= 3 and idade <= 12 :
            print('pague 10 dolares')

    else:
            print('pague 15 dolares')
    
