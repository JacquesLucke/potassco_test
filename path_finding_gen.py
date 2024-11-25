def generate(width, height):
    for x in range(width):
        for y in range(height):
            yield f"pos(p_{x}_{y}).\n"

            if y < height - 1:
                yield f"n(p_{x}_{y}, p_{x}_{y+1}).\n"
            if x < width - 1:
                yield f"n(p_{x}_{y}, p_{x+1}_{y}).\n"

    in_pos = "p_0_0"
    out_pos = f"p_{width-1}_{height-1}"

    yield f"input({in_pos}).\n"
    yield f"output({out_pos}).\n"
    yield f"on({in_pos}).\n"

    yield "n(X, Y) :- n(Y, X).\n"

    yield "blocked(p_0_2).\n"
    yield "blocked(p_1_2).\n"
    yield "blocked(p_2_2).\n"
    yield "blocked(p_3_2).\n"
    yield "blocked(p_4_2).\n"
    yield "blocked(p_5_2).\n"
    yield "blocked(p_9_5).\n"
    yield "blocked(p_8_5).\n"
    yield "blocked(p_7_5).\n"
    yield "blocked(p_6_5).\n"
    yield "blocked(p_5_5).\n"
    yield "blocked(p_4_5).\n"
    yield "blocked(p_3_5).\n"
    yield "blocked(p_2_5).\n"
    yield "blocked(p_1_5).\n"
    yield "blocked(p_0_7).\n"
    yield "blocked(p_2_6).\n"

    yield "{ "
    for x in range(width):
        for y in range(height):
            yield f"on(p_{x}_{y})"
            if x <width -1 or y < height - 1:
                yield ";"
    yield " }.\n"

    yield f"linked_to_input({in_pos}).\n"
    yield "linked_to_input(P) :- n(P, X), linked_to_input(X), on(X), on(P), not blocked(P).\n"
    yield f":- not linked_to_input({out_pos}).\n"
    yield "#minimize { 1@1, X : on(X) }.\n"
    yield "#show on/1.\n"


global_w = 10
global_h = 10

code = "".join(generate(global_w, global_h))
print(code)

with open("path_finding.lp", "w") as f:
    f.write(code)

def on_model(m):
    print("\n\n")
    symbols = m.symbols(atoms=True)
    lines =  [" " * global_w] * global_h
    # print(symbols)
    for s in symbols:
        if s.name == "on":
            x, y = map(int, s.arguments[0].name[2:].split("_"))
            l = lines[y]
            lines[y] = l[:x] + "X" + l[x+1:]
        if s.name == "blocked":
            x, y = map(int, s.arguments[0].name[2:].split("_"))
            l = lines[y]
            lines[y] = l[:x] + "B" + l[x+1:]
    print("\n".join(lines))


from clingo.control import Control
ctl = Control()
ctl.configuration.solve.models = 100
ctl.add("base", [], code)
ctl.ground([("base", [])])
ctl.solve(on_model=on_model)
