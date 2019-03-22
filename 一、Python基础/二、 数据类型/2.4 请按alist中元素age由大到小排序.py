alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]

def sort_alist(str):
    print(sorted(alist, key=lambda a: a['age'], reverse=True))

sort_alist(alist)