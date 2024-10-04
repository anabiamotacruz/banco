saldo = 0
clientes = {
    '12345678910' : {'user': 'Beatriz Cruz', 'senha': 1000},
    '12345678911' : {'user': 'Taylor Swift', 'senha': 1001},
    '12345678912' : {'user': 'Lana Del Rey', 'senha': 1002},
    '12345678913' : {'user': 'Ariana Grande', 'senha': 1003},
    '12345678914' : {'user': 'Rihanna', 'senha': 1004}
}
inicio = 0
opcao = 0
while inicio==0:
    cpf = input('Digite o seu CPF: \f')
    senha = int(input('Digite a sua senha: \f'))
    if cpf in clientes:
        user = clientes[cpf]['user']
        print(f'Seja bem-vindo(a), {user} \f')
        if senha == clientes[cpf]['senha']:
            print('Você é nosso cliente! Atendimento iniciado \f')
            inicio = 1
            opcao = 1
        else:
            print('Senha incorreta, tente novamente \f')
    else:
        cadastro = input(('Você não é nosso cliente. Deseja fazer o cadastro? \f'))
        if cadastro == 'Sim':
            add_cpf = input('Digite o seu CPF: \f')
            add_user = input('Digite o seu nome: \f')
            definir_senha = int(input('Digite uma senha (apenas números de 4 dígitos): \f'))
            clientes[add_cpf] = {'user':add_user, 'senha':definir_senha}
            print('Você foi cadastrado com sucesso! \f')
        else:
            inicio = 1
            opcao = 0
def sacar_dinheiro():
    global saldo
    dinheiro_sacar = float(input('Digite o valor que você quer sacar: \f'))
    if saldo>=dinheiro_sacar:
        print(f'Seu saldo atual é R${saldo-dinheiro_sacar} \f')
        saldo = saldo-dinheiro_sacar
    else:
        print('Saldo indisponível. \f')
def depositar_dinheiro():
    global saldo
    deposito = float(input('Digite o valor do depósito: \f'))
    print(f'Seu saldo é R${saldo+deposito} \f')
    saldo = saldo+deposito
def saldo_atual():
    global saldo
    print(f'Seu saldo é de R${saldo} \f')
def emprestimo():
    global saldo
    emprestimo = float(input('Digite o valor do empréstimo: \f'))
    saldo += emprestimo
    if emprestimo<=10000:
        print(f'Seu saldo atual é R${saldo}, você terá juros de 5% e poderá pagar em até 24 parcelas de R${(emprestimo*0.05)/24} \f')
    elif emprestimo<=50000:
        print(f'Seu saldo atual é R${saldo}, você terá juros de 10% e poderá pagar em até 36 parcelas de R${(emprestimo*0.1)/36} \f')
    elif emprestimo<=100000:
        print(f'Seu saldo atual é R${saldo}, você terá juros de 15% e poderá pagar em até 48 parcelas de R${(emprestimo*0.15)/48} \f')
    elif emprestimo<=200000:
        print(f'Seu saldo atual é R${saldo}, você terá juros de 20% e poderá pagar em até 60 parcelas de R${(emprestimo*0.2)/60} \f')
    else:
        print(f'Seu saldo atual é R${saldo}, você terá juros de 25% e poderá pagar em até 72 parcelas de R${(emprestimo*0.25)/72} \f')
def listar_clientes():
    print('Clientes: \f')
    for x,y in clientes.items():
        for i,j in y.items():
            if i == 'user':
                print(j)
while opcao == 1:
    print('\f 1. Sacar dinheiro \f 2. Depositar dinheiro \f 3. Verificar saldo \f 4. Falar com o gerente \f 5. Empréstimo \f 6. Listar clientes \f 7. Encerrar atendimento \f')
    operacao = int(input('Digite a operação que deseja fazer: \f'))
    match operacao:
        case 1:
            sacar_dinheiro()
        case 2:
            depositar_dinheiro()
        case 3:
            saldo_atual()
        case 4:
            print('Por favor, entre em contato com o número de celular (12) 34567-8910 \f')
        case 5:
            emprestimo()
        case 6:
            listar_clientes()
        case 7:
            opcao = 2
print('Atendimento encerrado! \f')