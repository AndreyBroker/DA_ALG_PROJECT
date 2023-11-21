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
            hora_str = hora_utc_str.replace(" UTC", "")

            data_referencia = datetime(2023, 1, 1)  
            data_hora_utc = datetime.strptime(hora_str, "%H%M").replace(year=data_referencia.year, month=data_referencia.month, day=data_referencia.day)

            fuso_horario_utc = timezone.utc
            data_hora_utc = data_hora_utc.replace(tzinfo=fuso_horario_utc)

            data_hora_local = data_hora_utc.astimezone(fuso_horario_local)
            
            return data_hora_local.strftime("%H:%M")
        except ValueError:
            return hora_utc_str
    
    def clean_dataframe(self):
        
        try:
            substituicoes = {
                ',': '.',
                '-9999': None,
                '-': '/'
            }
            
            self.df = self.df.replace(substituicoes, regex=True)
            self.df["TEMP_AR"] = self.df["TEMP_AR"].astype(float)
            self.df["DATA"] = pd.to_datetime(self.df['DATA'], format='%Y/%m/%d') 
            self.df["DIA"] = self.df["DATA"].dt.day
            fuso_horario_local = timezone(timedelta(hours=-3))  # GMT-3
            self.df['HORA'] = self.df['HORA'].apply(lambda x: self.converter_utc_para_local(x, fuso_horario_local) if 'UTC' in x else x)
            self.df = self.df.drop(columns=["Unnamed: 19"])
            return True
        except Exception as ex:
            print(f"Erro ao realizar as tratativas no dataframe.\n{ex}")
            input()
            return False
            
    def general_report(self):
        
        colunas = ", ".join(self.columuns())
        return f"Total de linhas: {len(self.df)}\nColunas: [{colunas}]"
    
    def isValidDate(self, date):
        
        try:
            datetime_obj = datetime.strptime(date, '%Y/%m/%d')
            return date
        except ValueError:
            return False
    
    def getTempByDate(self, date):
        df_f = self.df[self.df["DATA"] == date][["TEMP_AR", "HORA"]].sort_values(by='HORA')
        
        return df_f
    
        
        
        
        
            