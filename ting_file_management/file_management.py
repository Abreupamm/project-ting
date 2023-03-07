import sys


def txt_importer(path_file):
    if '.txt' not in path_file:
        return sys.stderr.write('Formato inválido')
    try:
        with open(path_file, 'r') as file:
            result = file.read().splitlines()
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
    else:
        return result
