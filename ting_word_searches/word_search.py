def exists_word(word, instance):
    result = []
    occurrences = []
    for item in range(instance.__len__()):
        file = instance.search(item)
        for index, value in enumerate(file['linhas_do_arquivo']):
            if word.lower() in value.lower():
                occurrences.append({'linha': index + 1})

    if len(occurrences) > 0:
        result.append({
            'palavra': word,
            'arquivo': file['nome_do_arquivo'],
            'ocorrencias': occurrences,
        })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
