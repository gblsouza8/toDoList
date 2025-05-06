import json

def adicionarTarefa(nome_tarefa, status_tarefa):
    try:
        with open('tarefas.json', 'r') as arquivo:
            dados = json.load(arquivo)

        novaTarefa = {
            "id": len(dados["tarefas"]) + 1,
            "tarefa": nome_tarefa,
            "status": status_tarefa
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




