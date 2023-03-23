def serilize_list(data, description):
    items = []
    for i in data:
        items.append(serilize(i, description))
    return items

def serilize(data, description):
    """
    Returns a dictionary
    data: tuple of data
    description: names of the columns from psycog2 cursor.description
    """
    item = {}
    for k, v in zip(description, data):
            item[k[0]] = v
    return item