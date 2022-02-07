import pandas as pd


def read_xlss(file_path):
    empdata = pd.read_excel(file_path)
    empdata.drop_duplicates()
    empdata['contrato'].fillna('default', inplace=True)
    return empdata.iterrows()

#print(read_xlss(r'C:\Users\centm\Desktop\Lista_tabular_APROVADO_REJEITADO_contrato.xlsx'))
