import json

def load_candidates_from_json(path):
    """
    получаем список всех кандидатов
    :param path:
    :return:
    """
    with open(path, 'rt', encoding= 'UTF-8') as f:
        raw_data = f.read()
        data = json.loads(raw_data)
    return data


def get_candidate(candidate_id):
    """
    Возвращает одного кандидата по его id
    :param candidate_id:
    :return:
    """
    data = load_candidates_from_json('candidates.json')
    for i in range(len(data)):
        if data[i]['id'] == candidate_id:
            return data[i]

def get_candidates_by_name(candidate_name):
    """
    Возвращает кандидатов по имени
    :param candidate_name:
    :return:
    """
    li = load_candidates_from_json('candidates.json')
    cname = candidate_name.lower()
    print(cname)
    count = 0
    idres = []
    nameres = []
    for i in range(len(li)):
        li2 = li[i]['name'].lower().split(', ')

        for el in li2:
            el = ''.join(el)
            if cname in el.split(' '):
                idres.append(li[i]['id'])
                nameres.append(li[i]['name'])
                count += 1
        else:
            continue
    return(count, idres, nameres)


def get_candidates_by_skill(skill_name):
    """
    Возвращает кандидатов по навыку
    :param skill_name:
    :return:
    """
    li = load_candidates_from_json('candidates.json')
    print(type(li))
    count = 0
    idres = []
    nameres = []
    for i in range(len(li)):
        li2 = li[i]['skills'].lower().split(', ')
        if skill_name in li2:
            idres.append(li[i]['id'])
            nameres.append(li[i]['name'])
            count += 1
        else:
            continue

    return(count, idres, nameres)





