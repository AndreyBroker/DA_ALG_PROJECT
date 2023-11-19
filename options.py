from tools import print_center, default_interface, plot_two
from dataset import Dataset
from labels import menu_reports, menu

dataset = Dataset()
dataset.clean_dataframe()

def general_report():
    while True:
        response = default_interface(dataset.general_report(), page_title="Relatório Geral")
        
        match response:
            case "":
                break
            case _:
                continue

def statistic_data():
    
    while True:
        
        df = dataset.df
        response = default_interface(
            "\n ----- Mediana ----- \n" + 
            str(df.median(numeric_only=True))+ 
            "\n ----- Desvio Padrão ----- \n" +
            str(df.std(numeric_only=True)) +
            "\n ----- Média ----- \n" +
            str(df.mean(numeric_only=True)) +
            "\n ----- Moda ----- " +
            str(df.mode(numeric_only=True).transpose()),
            page_title= "Dados Estátisticos"
        )
        
        match response:
            case "":
                break
            case _:
                continue
            
def getTempByDate():
    
    while True:
        try:
            response = default_interface(
            "Informe a data: (Ano/Mês/Dia)\nOBS: Lembrando que temos somente as datas de 2010 e 2022.\n", page_title="Buscar Data")
            
            if response:
            
                temp = dataset.getTempByDate(response)
                if temp:
                    default_interface(str(temp))
                else:
                    default_interface("Nenhum dado encontrado.")
            else:
                break
            
        except Exception as ex:
            default_interface(f"Resposta invalida, por favor a data deve estar no formato: Ano/Mês/Dia\nEx: 2023/11/18", page_title="Erro")

def temp_grafics():
    df = dataset.df
    
    df22 = df[(df["DATA"].dt.year == 2022)]
    df10 = df[(df["DATA"].dt.year == 2010)]
    
    while True:
        
        plot_two(df10, "2010", df22, "2022", "Gráficos de Temperatura")
        
        response = default_interface(page_title="Gráficos Temporais")
        
        match response:
            case "":
                break
            case _:
                continue

def general_description():
    while True:
        response = default_interface(dataset.df.describe(), page_title= "Descrição Geral")
        
        match response:
            case "":
                break
            case _:
                continue

def nf_response(comand):
    while True:
        response = default_interface(f"Comando '{comand}' não mapeado", page_title="Erro")
        
        match response:
            case "":
                break
            case _:
                continue
        

def reports():
    
    while True:
        response = default_interface(menu_reports, page_title="Relatórios")
        
        match response:
            case "":
                break
            case "1":
                general_report()
            case "2":
                statistic_data()
            case "3":
                getTempByDate()
            case "4":
                temp_grafics()
            case "5":
                general_description()
            case "6":
                pass
            case _:
                nf_response(response)
                
            
def inicial():
    
    while True:
        response = default_interface(menu, menu=True, page_title="Menu Principal")
        
        match response:
            case "1":
                reports()
            case "0":
                print_center("Saindo...")
                break
            case _:
                continue
            
