# nome: Murilo Mendes Marques RM:564193
# Nome: Enzo Ramos Condomitti RM:565832
# Nome: Lucca Fernandes Dos Santos RM:563961

# Função que valida usuário e senha
def checa_credenciais(dados):
    while True:
        usuario = input("Coloque o seu usuário: ")
        senha = input("Coloque a sua senha: ")

        # Verifica se o usuário existe e se a senha está correta
        if usuario in dados and dados[usuario] == senha:
            print("Login bem-sucedido! Bem-vindo,", usuario)
            return usuario
        else:
            print("Erro! Usuário ou senha incorretos. Tente novamente.")

# Função que cadastra uma nova área se ela ainda não estiver cadastrada
def cadastro_area(dados, nova_area):
    if nova_area not in dados:
        dados.append(nova_area)
        print(f"A área '{nova_area}' foi adicionada com sucesso.")
    else:
        print(f"A área '{nova_area}' já está cadastrada.")

# Loop para cadastrar várias áreas com confirmação do usuário
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

# Função para remover uma área cadastrada
def remover_area(dados):
    if not dados:  # Verifica se a lista está vazia
        print("Não há áreas cadastradas para remover.")
        return

    # Mostra áreas cadastradas e solicita qual deve ser removida
    print("Áreas cadastradas:", ", ".join(dados))
    area_remover = input("Digite o nome da área que deseja remover: ")

    if area_remover in dados:
        dados.remove(area_remover)
        print(f"A área '{area_remover}' foi removida com sucesso.")
    else:
        print(f"A área '{area_remover}' não está cadastrada.")

# Dicionário com usuários e senhas
banco_de_dados = {
    'Murilo': '1234@senha',
    'Enzo': 'kazoperdido5',
    'Suricato': 'ohomemperdido39'
}

# Lista com áreas cadastradas
banco_de_dados_areas_cadastradas = ['paulista',]

# Início do login
login = checa_credenciais(banco_de_dados)

# Dados fixos da região "paulista"
volume_da_agua_paulista = 63
saturacao_do_solo_paulista = 20
nivel_da_agua_palista = 'medio'

# Mostra os dados da região "paulista"
print(volume_da_agua_paulista,"%\n",saturacao_do_solo_paulista,"%\n", nivel_da_agua_palista)

# Solicita o cadastro de uma nova área
cadastro_area(banco_de_dados_areas_cadastradas, input("Digite uma nova área para cadastrar: "))

# Permite cadastrar várias áreas em sequência
loop_cadastro_areas()

# Pergunta se o usuário deseja remover alguma área
resposta_remover = input("Deseja remover alguma área? (sim/não): ").lower()
if resposta_remover == "sim":
    remover_area(banco_de_dados_areas_cadastradas)
else:
    print("Nenhuma área será removida.")
