import os
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
#inst = {(w := ln.split(" -> "))[1].strip(): w[0] for ln in open("input.txt")}
inst = {}
with open("input.txt", "r") as f:
    for line in f:
        w = line.split(" -> ")
        key = w[1].strip()
        value = w[0]
        inst[key] = value

OPERATIONS = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "NOT": lambda x: ~x,
    "LSHIFT": lambda x, y: x << y,
    "RSHIFT": lambda x, y: x >> y
}


def get_value(wire, d):
    if wire.isdigit():
        return int(wire)

    if isinstance(d[wire], int):
        return d[wire]

    w = d[wire].split()
    if len(w) == 1:
        d[wire] = get_value(w[0], d)
        return d[wire]
    elif "NOT" in d[wire]:
        d[wire] = OPERATIONS["NOT"](get_value(w[1], d))
        return d[wire]
    else:
        d[wire] = OPERATIONS[w[1]](get_value(w[0], d), get_value(w[2], d))
        return d[wire]


print(sig := get_value("a", dict(inst)))  # part 1 - 46065

inst["b"] = sig
print(get_value("a", dict(inst)))  # part 2 - 14134