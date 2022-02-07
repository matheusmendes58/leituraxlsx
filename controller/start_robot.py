from model.base import create_all
from model.tables import DataCorrectionDb
from utils.read_xls import read_xlss


def run():
    try:
        print('Criando tabela de dados do robo 005_auto_bko_approved_customers_in_data_correction')

        create_all()

    except Exception as error:
        raise print(error, 'Erro na criação de tabelas no banco de dados')

    try:
        print('Inserindo dados do pipefy para o banco de dados')
        file_path = r'C:\Users\centm\Desktop\Lista_tabular_APROVADO_REJEITADO_contrato.xlsx'

        DataCorrectionDb.insert_all_lines(read_xlss(file_path))

    except Exception as error:
        raise print(error, 'Erro na inserção de dados do pipefy')


if __name__ == '__main__':
    run()