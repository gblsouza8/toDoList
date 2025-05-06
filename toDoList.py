import json

def adicionarTarefa(nome_tarefa):
    try:
        with open('tarefas.json', 'r') as arquivo:
            dados = json.load(arquivo)

        novaTarefa = {
            "id": len(dados["tarefas"]) + 1,
            "tarefa": nome_tarefa,
        }

        dados["tarefas"].append(novaTarefa)
    
        with open ("tarefas.json", 'w') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

        print(f"Tarefa '{nome_tarefa}', adicionada com sucesso!")

    except FileNotFoundError:
        print("Arquivo tarefas.json não foi encontrado.")


def removerTarefa(id_tarefa):
    try: 
        with open('tarefas.json', 'r') as arquivo:
            dados = json.load(arquivo)

        tarefa_a_remover = None
        for tarefa in dados["tarefas"]:
            if tarefa["id"] == id_tarefa:
                tarefa_a_remover = tarefa
                break

        if tarefa_a_remover:
            dados["tarefas"].remove(tarefa_a_remover)

            with open('tarefas.json', 'w') as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)

            print(f"Tarefa '{tarefa_a_remover}', removida com sucesso!")
        else:
            print(f"Tarefa com ID {id_tarefa} não encontrada.")
    except FileNotFoundError:
        print("Arquivo tarefas.json não foi encontrado.")

def visualizarTarefas():
    try: 
        with open('tarefas.json', 'r') as arquivo:
            dados = json.load(arquivo)

            for tarefa in dados["tarefas"]:
                print(f"ID: {tarefa['id']} | Tarefa: {tarefa['tarefa']}")

    except FileNotFoundError:
        print("Arquivo tarefas.json não foi encontrado.")



def console():
    escolha = int(input("O que você deseja fazer?\n1. Visualizar tarefas\n2. Adicionar tarefas\n3. Remover tarefas\n0. Sair\n"))
    if escolha == 1:
        visualizarTarefas()
    elif escolha == 2:
        tarefa = input("Qual tarefa você gostaria de adicionar? ")
        adicionarTarefa(tarefa)
    elif escolha == 3:
        tarefa = int(input("Digite o ID da tarefa que você gostaria de remover: "))
        removerTarefa(tarefa)
    elif escolha == 0:
        exit()
    else: 
        print("Escolha inválida.")
        console()


console()
    