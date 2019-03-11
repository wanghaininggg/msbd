def process(e):
    pass


def get_lines():
    l = []
    with open('file.text', 'rb') as f:
        data = f.readlines(60000)
    l.append(data)
    yield l


if __name__ == '__main__':
    for e in get_lines():
        process(e)