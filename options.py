from tools import print_center, default_interface, plot_two, list_choices_interface
from dataset import Dataset
from labels import *

dataset = Dataset() ## Abrindo dataset
dataset.clean_dataframe() ## Realiza os tratamentos do df

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
            text = statisticDataLabel({
                "Mediana": df.median(numeric_only=True).to_string(),
                "Desvio Padrão": df.std(numeric_only=True).to_string(),
                "Média": df.mean(numeric_only=True).to_string(),
                "Moda": df.mode(numeric_only=True).loc[0].transpose().to_string()
            }),
            page_title = "Dados Estátisticos"
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
            getTempbyDateLabel, page_title="Buscar Data")
            
            
            if response:
                
                if dataset.isValidDate(response):    
                    temp = dataset.getTempByDate(response)
                    
                    if not temp.empty:
                        default_interface(temp.to_string(index=False))
                    else:
                        default_interface("Nenhum dado encontrado.")
                else:
                    default_interface(getTempbyDateErrorLabel(response), page_title="Formato Inválido")
            else:
                break
            
        except Exception as ex:
            print(ex)
            input()
            default_interface(getTempbyDateErrorLabel(response + f"   {ex}"), page_title="Erro")

def temp_grafics():
    df = dataset.df
    
    df22 = df[(df["DATA"].dt.year == 2022)]
    df10 = df[(df["DATA"].dt.year == 2010)]
    
    while True:
        
        plot_two(df10, "2010", df22, "2022", "Gráficos de Temperatura")
        
        response = default_interface("[1] Ver gráfico\n" , page_title="Gráficos Temporais")
        
        match response:
            case "":
                break
            case "1":
                continue
            case _:
                continue

def general_description():
    while True:
        df = dataset.df.describe()
        response = default_interface(general_description_label, page_title= "Descrição Geral")
        
        match response:
            case "":
                break
            case "1":
                default_interface(df.to_string(index=False), page_title= "Descrição Geral")
            case "2":
                try:
                    df.to_csv("Resumo.csv")
                    default_interface("Arquivo gerado com sucesso!", page_title= "Descrição Geral")
                except Exception as ex:
                    default_interface(f"Erro ao gerar arquivo.\n{ex}", "Erro")
            case _:
                continue

def parcial_file():
    df = dataset.df
    while True:
        
        response = default_interface("[1] Criar Arquivo Parcial\n[2] Como usar?")
        
        match response:
            case "":
                break
            case "1":
                pass
            case "2":
                default_interface(parcial_file_how_use_label)
                continue
        
        columns = df.select_dtypes(include=['number']).columns
        col = list_choices_interface(list_choices=columns, page_title="Relatório Parcial")
        
        match col:
            
            case "":
                break
            case a if col:
                list_op = ["==", ">", "<", "!="]
                op = list_choices_interface(list_choices=list_op, page_title="Relatório Parcial")
                
                match op:
                    
                    case "":
                        break
                    case a if op:
                        
                        value = default_interface("O valor informado só pode ser numérico.\n\n"+col+f"\n {op} ", page_title="Relatório Parcial")
                        
                        if value == "":
                            break
                        
                        try:
                            value = float(value)
                            
                            match op:
                                case "==":
                                    df_f = df[df[col] == value]
                                case ">":
                                    df_f = df[df[col] > value]
                                case "<":
                                    df_f = df[df[col] < value]
                                case "!=":
                                    df_f = df[df[col] != value]
                                    
                            try:
                                file_name = default_interface("Insira um nome para o arquivo: ", page_title="Relatório Parcial")
                                df_f.to_csv(file_name+".csv")
                                default_interface(f"Arquivo '{file_name}.csv' gerado com sucesso!", page_title="Relatório Parcial")
                                
                            except Exception as ex:
                                default_interface(f"Erro ao gerar arquivo.\n{ex}", "Erro")
                            
                        except:
                            default_interface(f"Resposta {col} é inválida, o valor fornecido deve ser um numérico.", page_title="Resposta inválida")
                        
                    case _:
                        default_interface(f"Resposta {col} é inválida, tente novamente.", page_title="Resposta inválida")
                
            case _:
                default_interface(f"Resposta {col} é inválida, tente novamente.", page_title="Resposta inválida")

def nf_response(comand):
    while True:
        response = default_interface(f"Resposta '{comand}' é inválido.", page_title="Resposta Inválida.")
        
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
                parcial_file()
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
            
