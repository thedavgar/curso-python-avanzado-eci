import pandas as pd

class grupo2:
    path_input = 'datainput/'
    divisiones = 'divisiones'
    departamentos = 'departamentos'
    centro_provincia = 'centro_provincia'

    def __init__(self):
        self.divisiones = self.read_csv(self.divisiones)
        self.departamentos = self.read_csv(self.departamentos)
        self.centro_provincia = self.read_csv(self.centro_provincia)

    def read_csv(self, entidad):
        try:
            df = pd.read_csv(
                self.path_input + f'{entidad}.csv',
                dtype=str 
            )
            return df
        except FileNotFoundError:
            return -1
        except Exception as e:
            return 99