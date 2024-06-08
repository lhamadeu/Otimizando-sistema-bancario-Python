
def menu():
    menu = """
#########################################################################
#    Bem vindo ao banco Esquina, escolha e digite a opção:              #
#        d = Depósito                                                   #
#        s = Saque                                                      #
#        e = Extrato                                                    #
#        nu = Novo Usuário                                              #
#        nc = Nova Conta                                                #
#        lc = Lista de Contas                                           #
#        q = Encerrar                                                   #
#########################################################################
      Digite a Opção: """
    return (menu)


def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        print(f"Depósito de R$ {
              valor} realizado. Saldo em banco: R$ {saldo:7.2f}")
        extrato += f" Depósito de R$ {valor:7.2f}\n"
        return saldo, extrato

    else:
        print()
        print("Valor não permitido. Refaça a operação")
        print()


def saque(*, saldo, extrato, valor, qtd_saque, limite_saque, qtd_max_saque):
    if qtd_saque >= qtd_max_saque:
        print(" Limite de saques permitidos extrapolados. Realize novo saque amanhã")
    elif saldo-valor < 0:
        print("Não há saldo suficiente para retirada")
    elif valor > limite_saque:
        print(" Valor de saque maior que o permitido")
    elif valor < 0:
        print(" Valor não permitido ou incorreto")
    else:
        saldo -= valor
        qtd_saque += 1
        print(f"Saque de R$ {
              valor:7.2f} realizado. Saldo atual de:R$ {saldo:7.2f} ")
        extrato += f" Saque de R$ {valor:7.2f}\n"
    return saldo, extrato, qtd_saque


def extrato_geral(saldo, extrato):
    print(f" O saldo atual é de R$: {saldo}")
    print(extrato)


def check_CPF(CPF, usuarios):
    usu = [usuario for usuario in usuarios if usuario["CPF"] == CPF]
    return usu[0] if usu else None


def novo_usuario(CPF, usuario):
    existe = check_CPF(CPF, usuario)
    if existe:
        print("Usuário ja cadastrado")
        return
    nome = input("Digite o nome do cliente:")
    nascimento = input("Digite a data de nascimento no formato dd/mm/aaaa")
    endereço = input(
        "Digite o endereço conforme o padrão (Logradouro, n° - bairro - cidade/sigla estado)")
    usuario.append({"nome": nome, "nascimento": nascimento,
                   "CPF": CPF, "endereço": endereço}, )


def nova_conta(CPF, conta, usuario):
    agencia = "0001"
    existe = check_CPF(CPF, usuario)
    if not existe:
        print("Cliente não cadastrado. Cadastre o usuário antes de abrir a conta")
        return None
    nr_conta = len(conta)+1
    print(agencia, nr_conta)
    conta.append({"Agência": agencia, "Conta": nr_conta, "Cliente": existe},)
    return


def lista_conta(conta):
    for i in conta:
        print(f" Agência: 0001, Conta: {
              i["Conta"]}, Cliente: {i["Cliente"]["nome"]}")
        print("====================================================\n")


def main():
    saldo = 0
    qtd_saque = 0
    valor_max_saque = 500
    qtd_max_saque = 3
    usuarios = []
    extrato = ""
    conta = []

    while True:
        x = input(menu())
        if x == "d":
            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = deposito(valor, saldo, extrato)

        elif x == "s":
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, qtd_saque = saque(saldo=saldo, extrato=extrato, qtd_saque=qtd_saque,
                                              limite_saque=valor_max_saque, qtd_max_saque=qtd_max_saque, valor=valor)

        elif x == "e":
            extrato_geral(saldo, extrato=extrato)

        elif x == "nu":
            print(usuarios)
            CPF = input("Digite o CPF do usuário:")
            if len(CPF) != 11:
                print("CPF inválido. Verifique se possui 11 digitos")
            else:
                novo_usuario(CPF, usuarios)
        elif x == "nc":
            CPF = input("Digite o CPF do usuário:")
            nova_conta(CPF, conta, usuarios)
        elif x == "lc":
            print("Lista de contas cadastradas no nosso banco:\n")
            lista_conta(conta)
        elif x == "q":
            break
        else:
            print("Opção inválida. Tente novamente com as opções da tela")


main()
