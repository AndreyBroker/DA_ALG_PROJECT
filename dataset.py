import pandas as pd
from datetime import datetime, timezone, timedelta

class Dataset:
    
    def __init__(self, path = "datasets/Dataset.CSV"):
        
    
        self.df = pd.read_csv(path, encoding='latin1', sep=";")
        self.path = path
    
    def describe(self):
        return self.df.describe()
    
    def columuns(self) -> list:
        return self.df.columns
    
    def converter_utc_para_local(self, hora_utc_str, fuso_horario_local):
        try:
            # Extraindo a parte relevante (sem " UTC")
            hora_str = hora_utc_str.replace(" UTC", "")

            # Criando um objeto datetime com uma data de referência fixa
            data_referencia = datetime(2023, 1, 1)  # Utilizando o ano, mês e dia desejados
            data_hora_utc = datetime.strptime(hora_str, "%H%M").replace(year=data_referencia.year, month=data_referencia.month, day=data_referencia.day)

            # Adicionando o fuso horário UTC
            fuso_horario_utc = timezone.utc
            data_hora_utc = data_hora_utc.replace(tzinfo=fuso_horario_utc)

            # Convertendo para a hora local
            data_hora_local = data_hora_utc.astimezone(fuso_horario_local)
            
            # Retornando apenas a hora e o minuto
            return data_hora_local.strftime("%H:%M")
        except ValueError:
            # Se ocorrer um erro ao converter, retorna o valor original
            return hora_utc_str

    
    def clean_dataframe(self):
        
        try:
            self.df = self.df.replace(',', '.', regex=True)
            self.df["TEMP_AR"] = self.df["TEMP_AR"].astype(float)
            self.df["DATA"] = pd.to_datetime(self.df['DATA'].str.replace("-", "/"), format='%Y/%m/%d') 
                    
            fuso_horario_local = timezone(timedelta(hours=-3))  # Exemplo: GMT-3
            self.df['HORA'] = self.df['HORA'].apply(lambda x: self.converter_utc_para_local(x, fuso_horario_local) if 'UTC' in x else x)
            return True
        except Exception as ex:
            print(f"Erro ao realizar as tratativas no dataframe.\n{ex}")
            return False
            
    def general_report(self):
        
        colunas = ", ".join(self.columuns())
        return f"Total de linhas: {len(self.df)}\nColunas: [{colunas}]"
    
    def getTempByDate(self, date):
        
        df_f = self.df[self.df["DATA"] == date][["TEMP_AR", "HORA"]].sort_values(by='HORA')
        
        print(df_f)
    
        
        
        
        
            