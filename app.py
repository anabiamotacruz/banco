saldo = 0
empregados = {
    '10987654321' : {'user': 'Sabrina', 'senha': 1234},
    '11987654321' : {'user': 'Olivia', 'senha': 2345},
    '12987654321' : {'user': 'Camila', 'senha': 3456}
}

clientes = {
    '12345678910' : {'user': 'Beatriz', 'senha': 1000},
    '12345678911' : {'user': 'Taylor', 'senha': 1001},
    '12345678912' : {'user': 'Lana', 'senha': 1002},
    '12345678913' : {'user': 'Ariana', 'senha': 1003},
    '12345678914' : {'user': 'Rihanna', 'senha': 1004}
}

inicio = 1
opcao = 0
cliente_empregado = 0

while cliente_empregado == 0:
    status = int(input('Você deseja fazer login como: \n1. Sou cliente \n2. Trabalho no banco \f'))
    if status==1:
        cliente_empregado = 1
        inicio = 0
    elif status == 2:
        cliente_empregado = 1
        inicio = 2
    else:
        print('Opção inválida \f')

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
            nome_lista = add_user.split()
            user_novo = nome_lista[0].capitalize()
            print(f'Seu nome de usuário é {user_novo}')
            definir_senha = int(input('Digite uma senha (apenas números de 4 dígitos): \f'))
            clientes[add_cpf] = {'user':user_novo, 'senha':definir_senha}
            print('Você foi cadastrado com sucesso! \f')
        else:
            inicio = 1
            opcao = 0

while inicio == 2:
    cpf = input('Digite seu CPF: \f')
    senha = int(input('Digite a sua senha: \f'))
    if cpf in empregados:
        user = empregados[cpf]['user']
        print(f'Seja bem-vindo(a), {user} \f')
        if senha == empregados[cpf]['senha']:
            inicio = 1
            opcao = 2
        else:
            print('Senha incorreta, tente novamente \f')
    else: 
        print('Você não é nosso empregado. \f ')

def sacar_dinheiro():
    global saldo
    dinheiro_sacar = float(input('Digite o valor que você quer sacar: \f'))
    if saldo>=dinheiro_sacar:
        print(f'Seu saldo atual é R${saldo-dinheiro_sacar} \f')
        saldo = saldo-dinheiro_sacar
    else:
        print(f'Saldo indisponível. Você não pode sacar R${dinheiro_sacar} pois você só tem R${saldo}\f')

def depositar_dinheiro():
    global saldo
    deposito = float(input('Digite o valor do depósito: \f'))
    print(f'Seu saldo é R${saldo+deposito} \f')
    saldo = saldo+deposito

def cadastrar_empregado():
    add_cpf = input('Digite o CPF: \f')
    add_user = input('Digite o nome: \f')
    nome_lista = add_user.split()
    user_novo = nome_lista[0].capitalize()
    print(f'O nome de usuário é {user_novo}')
    definir_senha = int(input('Digite uma senha (apenas números de 4 dígitos): \f'))
    empregados[add_cpf] = {'user':user_novo, 'senha':definir_senha}
    print('Empregado foi cadastrado com sucesso! \f')

def listar_empregados():
    print('Empregados: \f')
    for x,y in empregados.items():
        for i,j in y.items():
            if i == 'user':
                print('Nome:', j, '\nCPF:', x)

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
                print('Nome:', j, '\nCPF:', x)

def remover_cliente():
    cliente_remov = (input('Digite o CPF do cliente que desejar remover: \f'))
    if cliente_remov in clientes:
        user_a_remover = clientes[cliente_remov]['user']
        certeza = int(input(f'Tem certeza que deseja remover {user_a_remover} do banco? \f 1. Sim \f 2. Não \f'))
        if certeza == 1:
            clientes.pop(cliente_remov)
            print('Cliente removido com sucesso! \f')
        else:
            print('Cliente não removido. \f')
    else:
        print('CPF não encontrado. \f')

def remover_empregado():
    empregado_remov = (input('Digite o CPF do empregado que desejar remover: \f'))
    if empregado_remov in empregados:
        user_a_remover = empregados[empregado_remov]['user']
        certeza = int(input(f'Tem certeza que deseja remover {user_a_remover} do banco? \f 1. Sim \f 2. Não \f'))
        if certeza == 1:
            empregados.pop(empregado_remov)
            print('Empregado removido com sucesso! \f')
        else:
            print('Empregado não removido. \f')
    else:
        print('CPF não encontrado. \f')

while opcao == 1:
    print('\f 1. Sacar dinheiro \f 2. Depositar dinheiro \f 3. Verificar saldo \f 4. Falar com o gerente \f 5. Empréstimo \f 6. Encerrar atendimento \f')
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
            opcao = 3

while opcao == 2:
    print('\f 1. Listar clientes \f 2. Listar empregados \f 3. Remover empregados \f 4. Remover clientes \f 5. Cadastrar empregado \f 6. Sair \f')
    operacao = int(input('Digite a operação que deseja fazer: \f'))
    match operacao:
        case 1:
            listar_clientes()
        case 2:
            listar_empregados()
        case 3:
            remover_empregado()
        case 4:
            remover_cliente()
        case 5:
            cadastrar_empregado()
        case 6:
            opcao = 3

print('Atendimento encerrado! \f')