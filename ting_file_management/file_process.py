from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):

    for file in instance.queue:
        if file['nome_do_arquivo'] == path_file:
            return

    processed = dict()
    file_data = txt_importer(path_file)
    processed['nome_do_arquivo'] = path_file
    processed['qtd_linhas'] = len(file_data)
    processed['linhas_do_arquivo'] = file_data
    instance.enqueue(processed)
    sys.stdout.write(str(processed))


def remove(instance):
    result_removed = instance.dequeue()
    if result_removed is None:
        return sys.stdout.write('Não há elementos\n')
    paht = result_removed['nome_do_arquivo']
    return sys.stdout.write(f'Arquivo {paht} removido com sucesso\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
