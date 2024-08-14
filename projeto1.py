from datetime import datetime

# Lista de meses em português para conversão de datas
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]


# Função para converter ano em formato por extenso
def ano_por_extenso(ano):
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    especiais = ["", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]

    if 2000 <= ano < 2100:
        ano_str = str(ano)
        milhar = ano_str[:2]
        resto = int(ano_str[2:])

        if resto < 10:
            resto_extenso = unidades[resto]
        elif 11 <= resto <= 19:
            resto_extenso = especiais[resto - 10]
        else:
            dez = resto // 10
            uni = resto % 10
            resto_extenso = dezenas[dez] + (" e " + unidades[uni] if uni > 0 else "")

        if milhar == "20":
            return f"dois mil e {resto_extenso}" if resto > 0 else "dois mil"
        elif milhar == "21":
            return f"dois mil e {resto_extenso}" if resto > 0 else "dois mil"
    return str(ano)  # Para anos fora do intervalo ou não mapeados


def converter_data(data_str):
    try:
        # Tenta converter a string para um objeto datetime
        data = datetime.strptime(data_str, "%d/%m/%Y")
        # Converte o ano para formato por extenso
        ano_extenso = ano_por_extenso(data.year)
        # Retorna a data formatada por extenso
        return f"{data.day} de {meses[data.month - 1]} de {ano_extenso}"
    except ValueError:
        # Retorna None se a data for inválida
        return None


def menu():
    # Lista para armazenar datas convertidas
    datas_convertidas = []

    while True:
        # Exibe o menu de opções
        print("\nMenu de Opções:")
        print("1 – Converter Data")
        print("2 – Listar Datas por extenso")
        print("3 – Sair")

        # Recebe a opção do usuário
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # Opção para converter uma data
            data_input = input("Digite uma data no formato DD/MM/AAAA: ")
            data_extenso = converter_data(data_input)
            if data_extenso:
                # Mostra a data convertida e adiciona à lista
                print(f"Data por extenso: {data_extenso}")
                datas_convertidas.append(data_extenso)
            else:
                # Mensagem de erro se a data for inválida
                print("Data inválida. Tente novamente.")

        elif opcao == '2':
            # Opção para listar todas as datas convertidas
            if datas_convertidas:
                print("\nDatas convertidas:")
                # Mostra todas as datas armazenadas na lista
                print("\n".join(datas_convertidas))
            else:
                # Mensagem se nenhuma data tiver sido convertida
                print("Nenhuma data foi convertida ainda.")

        elif opcao == '3':
            # Opção para sair do programa
            if datas_convertidas:
                # Salva as datas convertidas em um arquivo
                with open("datas_convertidas.txt", "w") as arquivo:
                    arquivo.write("\n".join(datas_convertidas) + "\n")
                print("As datas convertidas foram salvas no arquivo 'datas_convertidas.txt'.")
            print("Saindo do programa...")
            break  # Sai do loop e encerra o programa

        else:
            # Mensagem de erro para opções inválidas
            print("Opção inválida. Tente novamente.")


# Chama a função principal para iniciar o programa
menu()
