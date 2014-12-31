

def read_data():
    with open("codeabbey.txt", "r") as f_in:
        raw_data = list(f_in.readlines())
    raw_data = map(lambda s: s.strip(), raw_data)
    n = int(raw_data[0])
    clean_data = []
    for i in range(1, len(raw_data)):
        clean_data.append([int(x) for x in raw_data[i].split(" ")])
    return n, clean_data


def read_data_alpha():
    with open("codeabbey.txt", "r") as f_in:
        raw_data = list(f_in.readlines())
    raw_data = map(lambda s: s.strip(), raw_data)
    answer = raw_data[0]
    clean_data = []
    for i in range(1, len(raw_data)):
        clean_data.append([x for x in raw_data[i].split(" ")])
    return answer, clean_data


def read_one_line():
    with open("codeabbey.txt", "r") as f_in:
        raw_data = list(f_in.readlines())[0].split(" ")
    return [int(x) for x in raw_data]


def f_to_c(data):
    data = data[1:]
    data = [int(round((x-32)/1.8, 0)) for x in data]
    return data


def count_vowels(data):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    counts = []
    for line in data:
        line = list("".join(line))
        counts.append(len([x for x in line if x in vowels]))
    return counts


def min_of_three(data):
    return [x for line in data for x in line
            if not x == min(line) and not x == max(line)]


def min_of_three_swap(data):
    results = []
    for line in data:
        a, b, c = line
        if a > b:
            a, b = b, c
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        results.append(b)
    return results


def neumann_loop(data):
    values = []
    while data not in values:
        values.append(data)
        data = str(data ** 2)
        while len(data) < 8:
            data = "0" + data
        data = int(data[2:6])
    return values, len(values)


def linear_con_gen(data):
    pass


answer, data = read_data()
print data
results = " ".join(map(lambda x: str(x), linear_con_gen(data)))
print results
