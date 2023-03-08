def search_ocorrencias(word, instance, content):
    occurrences = []
    for item in range(instance.__len__()):
        file = instance.search(item)
        for index, value in enumerate(file['linhas_do_arquivo']):
            if word.lower() in value.lower():
                if content is True:
                    occurrences.append({'conteudo': value, 'linha': index + 1})
                else:
                    occurrences.append({'linha': index + 1})
    return {'occurrences': occurrences, 'file': file}


def exists_word(word, instance):   
    result = []
    search = search_ocorrencias(word, instance, False)
    if len(search['occurrences']) > 0:
        result.append({
            'palavra': word,
            'arquivo': search['file']['nome_do_arquivo'],
            'ocorrencias': search['occurrences'],
        })
    return result


def search_by_word(word, instance):
    result = []
    search = search_ocorrencias(word, instance, True)
    if len(search['occurrences']) > 0:
        result.append({
            'palavra': word,
            'arquivo': search['file']['nome_do_arquivo'],
            'ocorrencias': search['occurrences']
        })
    return result
