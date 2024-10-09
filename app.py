import funcoes

# Variáveis deste arquivo (que não podem ser mudadas):
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
    if cpf in funcoes.clientes:
        user = funcoes.clientes[cpf]['user']
        print(f'Seja bem-vindo(a), {user} \f')
        if senha == funcoes.clientes[cpf]['senha']:
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
            funcoes.clientes[add_cpf] = {'user':user_novo, 'senha':definir_senha}
            print('Você foi cadastrado com sucesso! \f')
        else:
            inicio = 1
            opcao = 0

while inicio == 2:
    cpf = input('Digite seu CPF: \f')
    senha = int(input('Digite a sua senha: \f'))
    if cpf in funcoes.empregados:
        user = funcoes.empregados[cpf]['user']
        print(f'Seja bem-vindo(a), {user} \f')
        if senha == funcoes.empregados[cpf]['senha']:
            inicio = 1
            opcao = 2
        else:
            print('Senha incorreta, tente novamente \f')
    else: 
        print('Você não é nosso empregado. \f ')

while opcao == 1:
    print('\f 1. Sacar dinheiro \f 2. Depositar dinheiro \f 3. Verificar saldo \f 4. Falar com o gerente \f 5. Empréstimo \f 6. Encerrar atendimento \f')
    operacao = int(input('Digite a operação que deseja fazer: \f'))
    match operacao:
        case 1:
            funcoes.sacar_dinheiro()
        case 2:
            funcoes.depositar_dinheiro()
        case 3:
            funcoes.saldo_atual()
        case 4:
            print('Por favor, entre em contato com o número de celular (12) 34567-8910 \f')
        case 5:
            funcoes.emprestimo()
        case 6:
            opcao = 3

while opcao == 2:
    print('\f 1. Listar clientes \f 2. Listar empregados \f 3. Remover empregados \f 4. Remover clientes \f 5. Cadastrar empregado \f 6. Sair \f')
    operacao = int(input('Digite a operação que deseja fazer: \f'))
    match operacao:
        case 1:
            funcoes.listar_clientes()
        case 2:
            funcoes.listar_empregados()
        case 3:
            funcoes.remover_empregado()
        case 4:
            funcoes.remover_cliente()
        case 5:
            funcoes.cadastrar_empregado()
        case 6:
            opcao = 3

print('Atendimento encerrado! \f')