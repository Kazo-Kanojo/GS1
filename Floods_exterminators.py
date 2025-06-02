# nome: MUrilo Mendes Marques RM:564193
# Nome: Enzo Ramos Condomitti RM:565832
# Nome: lucca Fernandes Dos Santos RM:563961
def obriga_ser_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    num = int(num)
    return num

#garante que o usuario coloque a senha e o usuario certo.
def checa_credenciais(dados):
     while True:
         usuario = input("Coloque o seu usuário: ")
         senha = input("Coloque a sua senha: ")

         if usuario in dados and dados[usuario] == senha:
             print("Login bem-sucedido! Bem-vindo,", usuario)
             return usuario
         else:
             print("Erro! Usuário ou senha incorretos. Tente novamente.")

def cadastro_area(dados, nova_area):
    if nova_area not in dados:
        dados.append(nova_area)
        print(f"A área '{nova_area}' foi adicionada com sucesso.")
    else:
        print(f"A área '{nova_area}' já está cadastrada.")


def loop_cadastro_areas():
    while True:
        continuar = input("Deseja continuar adicionando novas áreas? (sim/não): ").lower()
        if continuar == "sim":
            nova = input("Digite a nova área: ")
            cadastro_area(banco_de_dados_areas_cadastradas, nova)
        elif continuar == "não":
            print("Encerrando o cadastro de áreas.")
            break
        else:
            print("Digite uma resposta válida: sim ou não.")


def remover_area(dados):
    if not dados:
        print("Não há áreas cadastradas para remover.")
        return

    print("Áreas cadastradas:", ", ".join(dados))
    area_remover = input("Digite o nome da área que deseja remover: ")

    if area_remover in dados:
        dados.remove(area_remover)
        print(f"A área '{area_remover}' foi removida com sucesso.")
    else:
        print(f"A área '{area_remover}' não está cadastrada.")


banco_de_dados = {
    'Murilo': '1234@senha',
    'Enzo': 'kazoperdido5',
    'Suricato': 'ohomemperdido39'
}
banco_de_dados_areas_cadastradas = ['paulista',]

login = checa_credenciais(banco_de_dados)

volume_da_agua_paulista = 63
saturacao_do_solo_paulista = 20
nivel_da_agua_palista = 'medio'

print(volume_da_agua_paulista,"%\n",saturacao_do_solo_paulista,"%\n", nivel_da_agua_palista)

#adiciona a possibilidade do usuario cadastrar uma nova area
cadastro_area(banco_de_dados_areas_cadastradas, input("Digite uma nova área para cadastrar: "))
loop_cadastro_areas()

resposta_remover = input("Deseja remover alguma área? (sim/não): ").lower()
if resposta_remover == "sim":
    remover_area(banco_de_dados_areas_cadastradas)
else:
    print("Nenhuma área será removida.")

