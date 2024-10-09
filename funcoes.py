import datetime
saldo = 0
dia_hora = (datetime.datetime.now()).strftime('%d/%m/%Y às %H:%M:%S')
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

# Função para sacar dinheiro
def sacar_dinheiro():
    global saldo, dia_hora
    dinheiro_sacar = float(input('Digite o valor que você quer sacar: \f'))
    if saldo>=dinheiro_sacar:
        print(f'Saque de R${dinheiro_sacar} feito dia {dia_hora}. \nSeu saldo atual é de R${saldo-dinheiro_sacar} \f')
        saldo = saldo-dinheiro_sacar
    else:
        print(f'Saldo indisponível. Você não pode sacar R${dinheiro_sacar} pois você só tem R${saldo}\f')

# Função para depositar dinheiro 
def depositar_dinheiro():
    global saldo, dia_hora
    deposito = float(input('Digite o valor do depósito: \f'))
    print(f'Depósito de R${deposito} feito dia {dia_hora}. Seu saldo é de R${saldo+deposito} \f')
    saldo = saldo+deposito

# Função para cadastrar empregado
def cadastrar_empregado():
    add_cpf = input('Digite o CPF: \f')
    add_user = input('Digite o nome: \f')
    nome_lista = add_user.split()
    user_novo = nome_lista[0].capitalize()
    print(f'O nome de usuário é {user_novo}')
    definir_senha = int(input('Digite uma senha (apenas números de 4 dígitos): \f'))
    empregados[add_cpf] = {'user':user_novo, 'senha':definir_senha}
    print('Empregado foi cadastrado com sucesso! \f')

# Função para listar empregados
def listar_empregados():
    print('Empregados: \f')
    for x,y in empregados.items():
        for i,j in y.items():
            if i == 'user':
                print('Nome:', j, '\nCPF:', x)

# Função para verificar saldo
def saldo_atual():
    global saldo
    print(f'Seu saldo é de R${saldo} \f')

# Função para fazer empréstimo
def emprestimo():
    global saldo, dia_hora
    emprestimo = float(input('Digite o valor do empréstimo: \f'))
    saldo += emprestimo
    if emprestimo<=10000:
        print(f'Seu saldo atual é R${saldo}, você terá juros de 5% e poderá pagar em até 24 parcelas de R${(emprestimo*0.05)/24}. \nEmpréstimo de R${emprestimo} feito dia {dia_hora}\f')
    elif emprestimo<=50000:
        print(f'Seu saldo atual é R${saldo}, você terá juros de 10% e poderá pagar em até 36 parcelas de R${(emprestimo*0.1)/36}.\nEmpréstimo de R${emprestimo} feito dia {dia_hora} \f')
    elif emprestimo<=100000:
        print(f'Seu saldo atual é R${saldo}, você terá juros de 15% e poderá pagar em até 48 parcelas de R${(emprestimo*0.15)/48}. \nEmpréstimo de R${emprestimo} feito dia {dia_hora} \f')
    elif emprestimo<=200000:
        print(f'Seu saldo atual é R${saldo}, você terá juros de 20% e poderá pagar em até 60 parcelas de R${(emprestimo*0.2)/60}. \nEmpréstimo de R${emprestimo} feito dia {dia_hora} \f')
    else:
        print(f'Seu saldo atual é R${saldo}, você terá juros de 25% e poderá pagar em até 72 parcelas de R${(emprestimo*0.25)/72}. \nEmpréstimo de R${emprestimo} feito dia {dia_hora} \f')

# Função para listar clientes
def listar_clientes():
    print('Clientes: \f')
    for x,y in clientes.items():
        for i,j in y.items():
            if i == 'user':
                print('Nome:', j, '\nCPF:', x)

# Funções para remover cliente
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

# Função para remover empregado
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