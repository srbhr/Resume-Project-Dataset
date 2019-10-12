

class Load:

    def __init__(self):
        self.data3 = []
        self.data_dict = {}
        self.person_list = {}
        self.df = None

    def get_data(self, df):
        for a in df.columns:
            self.data_dict[a] = str(df[a][0])
        return self.data_dict

    def imports(self, path):
        import pandas as pd
        if '.json' in path:
            self.df = pd.read_json(path)
        if '.csv' in path:
            self.df = pd.read_csv(path)
        return self.df

    def load_skills(self, path):
        self.data3 = []
        handle = open(path, encoding='utf-8')
        for a in handle:
            self.data3.append(a.rstrip('\n'))
        return self.data3


