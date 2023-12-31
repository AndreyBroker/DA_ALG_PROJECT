menu_reports = """
[1] Relatório Geral.\n
[2] Dados Estátisticos.\n
[3] Pesquisar Temperatura.\n
[4] Gráficos de Temperatura.\n
[5] Descrição Geral.\n
[6] Arquivo Parcial.
"""
menu = """
[1] Relatótios.\n
"""

getTempbyDateLabel = "Informe a data: (Ano/Mês/Dia)\nOBS: Lembrando que temos somente as datas de 2010 e 2022.\n"
def getTempbyDateErrorLabel(response):
    return f"Resposta invalida, por favor a data deve estar no formato: Ano/Mês/Dia\nEx: 2023/11/18"


def statisticDataLabel(fields):
    
    sep = lambda field: f"\n ----- {field} ----- \n"  
    
    listFields = [f"{sep(key) + fields[key]}" for key in fields]
    label = "".join(listFields)
    
    return label

general_description_label = '[1] Ver gráfico.\n[2] Gerar arquivo Resumo.'

parcial_file_label = """
Informe o mês desejado:
[1] Janeiro
[2] Fevereiro
[3] Março
[4] Abril
[5] Maio
[6] Junho
[7] Julho
[8] Agosto
[9] Setembro
[10] Outubro
[11] Novembro
[12] Dezembro

"""

parcial_file_how_use_label = """
Etapas:\n
1 - Você irá informar a coluna que deseja realizar a operação\n
2 - Você irá informar o tipo da operação sendo elas: '==', '>', '<', '!='\n
3 - Seguida você irá informar o valor para comparação.\n
4 - E por fim, você irá informar o nome do arquivo e ele será gerado!\n\n
OBS: As operações só podem ser realizas nas colunas apresentadas no momento da escolha. (Apenas numéricas).
"""