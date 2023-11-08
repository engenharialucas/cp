class ReutilizacaoMateriais:
    def __init__(self):
        self.materiais = {
            "Tijolos": {
                "quantidades": [1000, 500, 200, 100],
                "reutilizacoes": [
                    "Construir uma parede de divisória.",
                    "Construir uma churrasqueira.",
                    "Fazer um caminho no jardim.",
                    "Construir uma lareira."
                ],
                "doacao": "Você pode doar tijolos usados para organizações de construção de casas ou projetos de restauração histórica."
            },
            "Vigas de Madeira": {
                "quantidades": [20, 10, 5, 2],
                "reutilizacoes": [
                    "Construir prateleiras.",
                    "Construir uma mesa de trabalho.",
                    "Construir um banco de jardim.",
                    "Construir uma estante."
                ],
                "doacao": "Você pode doar vigas de madeira usadas para projetos de construção, como construção de casas ou instalação de cercas."
            },
            "Telhas de Cerâmica": {
                "quantidades": [500, 250, 100, 50],
                "reutilizacoes": [
                    "Criar um piso decorativo.",
                    "Construir uma mesa de jardim.",
                    "Fazer um mosaico de parede.",
                    "Construir uma cascata no jardim."
                ],
                "doacao": "Você pode doar telhas de cerâmica usadas para organizações de construção ou projetos de arte e artesanato."
            },
            "Plástico": {
                "quantidades": [1000, 500, 200, 100],
                "reutilizacoes": [
                    "Criar itens de decoração.",
                    "Construir móveis de jardim.",
                    "Fazer artesanato criativo.",
                    "Construir estruturas leves."
                ],
                "doacao": "Você pode doar plástico usado para reciclagem ou projetos de arte sustentável."
            },
            "Cimento": {
                "quantidades": [1000, 500, 200, 100],
                "reutilizacoes": [
                    "Reforçar estruturas existentes.",
                    "Fazer esculturas de cimento.",
                    "Construir bases para postes.",
                    "Criar pequenas obras de arte."
                ],
                "doacao": "Você pode doar cimento usado para organizações de construção ou projetos de arte e escultura."
            },
            "Metal": {
                "quantidades": [1000, 500, 200, 100],
                "reutilizacoes": [
                    "Fabricar móveis de metal.",
                    "Construir estruturas metálicas.",
                    "Criar esculturas de metal.",
                    "Reparar equipamentos."
                ],
                "doacao": "Você pode doar metal usado para reciclagem ou projetos de fabricação."
            },
            "Tubos de PVC": {
                "quantidades": [1000, 500, 200, 100],
                "reutilizacoes": [
                    "Criar estruturas leves.",
                    "Fazer sistemas de irrigação.",
                    "Construir móveis modulares.",
                    "Fazer brinquedos e jogos."
                ],
                "doacao": "Você pode doar tubos de PVC usados para projetos de construção e organização sem fins lucrativos."
            }
        }

    def mostrar_reutilizacao(self):
        for material, info in self.materiais.items():
            print(f"{material}:")
            for i in range(len(info["quantidades"])):
                print(f"Quantidade disponível ({i+1}): {info['quantidades'][i]} unidades.")
                print(f"Forma de reutilização ({i+1}): {info['reutilizacoes'][i]}")
            print(f"Forma de doação: {info['doacao']}")
            print()

    def reutilizar_material(self, material, quantidade):
        if material in self.materiais:
            info_material = self.materiais[material]
            quantidade_disponivel = info_material["quantidades"]

            for i in range(len(quantidade_disponivel)):
                if quantidade <= quantidade_disponivel[i]:
                    print(f"Você escolheu reutilizar {quantidade} unidades do material: {material}")
                    print(f"Quantidade disponível: {quantidade_disponivel[i]} unidades")
                    print(f"Você pode reutilizar da seguinte forma:")
                    for j in range(quantidade):
                        print(f"- {info_material['reutilizacoes'][i]}")
                    break
            else:
                print(f"Não há quantidade suficiente disponível para reutilizar {quantidade} unidades de {material}.")
            print(f"Forma de reutilização: {info_material['reutilizacoes'][i]}")
        else:
            print("Material não encontrado.")

    def doar_material(self, material):
        if material in self.materiais:
            info_material = self.materiais[material]
            print(f"Você escolheu doar o material: {material}")
            print(f"Forma de doação: {info_material['doacao']}")
        else:
            print("Material não encontrado.")

reutilizacao = ReutilizacaoMateriais()

while True:
    print("Opções:")
    print("1. Reutilizar material")
    print("2. Doar material")
    print("3. Sair")
    escolha = input("Escolha uma opção (1/2/3): ")

    if escolha == "1":
        material = input("Digite o nome do material que deseja reutilizar: ")
        quantidade = int(input(f"Quantas unidades de {material} deseja reutilizar: "))
        reutilizacao.reutilizar_material(material, quantidade)
    elif escolha == "2":
        material = input("Digite o nome do material que deseja doar: ")
        reutilizacao.doar_material(material)
    elif escolha == "3":
        print("Saindo do programa. Adeus!")
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
