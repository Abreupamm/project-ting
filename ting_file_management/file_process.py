from ting_file_management.file_management import txt_importer


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


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
