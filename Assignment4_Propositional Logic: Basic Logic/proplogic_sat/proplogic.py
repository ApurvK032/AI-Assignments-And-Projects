import sat_interface

def _entailed_value(kb, symbol):
    sat_with = kb.test_literal(symbol)
    sat_without = kb.test_literal("~" + symbol)
    if not sat_with and sat_without:
        return False
    if sat_with and not sat_without:
        return True
    return None


def tt2():
    clauses = []

    clauses.append("~A C")
    clauses.append("~B ~C")
    clauses.append("B C")
    clauses.append("~C B ~A")
    clauses.append("C ~B")
    clauses.append("C A")

    kb = sat_interface.KB(clauses)

    A = _entailed_value(kb, "A")
    B = _entailed_value(kb, "B")
    C = _entailed_value(kb, "C")

    print("Truth-tellers II")
    print("----------------")
    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("----------------")

    return (A, B, C)


def tt3():
    clauses = []

    clauses.append("~A ~C")
    clauses.append("A C")
    clauses.append("~B A")
    clauses.append("~B C")
    clauses.append("B ~A ~C")
    clauses.append("~C A")

    kb = sat_interface.KB(clauses)

    A = _entailed_value(kb, "A")
    B = _entailed_value(kb, "B")
    C = _entailed_value(kb, "C")

    print("Truth-tellers III")
    print("-----------------")
    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("-----------------")

    return (A, B, C)


def salt():
    clauses = []

    clauses.append("SP SB SC")
    clauses.append("~SP ~SB")
    clauses.append("~SP ~SC")
    clauses.append("~SB ~SC")

    clauses.append("~P SB")
    clauses.append("P ~SB")

    clauses.append("~B SB")
    clauses.append("B ~SB")

    clauses.append("~C ~SC")
    clauses.append("C SC")

    clauses.append("P B C")
    clauses.append("~P ~B ~C")

    kb = sat_interface.KB(clauses)

    symbols = ["P", "B", "C", "SP", "SB", "SC"]
    result = {}

    print("Robbery and a Salt")
    print("------------------")
    for s in symbols:
        v = _entailed_value(kb, s)
        result[s] = v
        print(s + ":", v)
    print("------------------")

    return result


def golf():
    clauses = []

    for p in ["T", "D", "H"]:
        F = p + "_F"
        M = p + "_M"
        L = p + "_L"
        clauses.append(f"{F} {M} {L}")
        clauses.append(f"~{F} ~{M}")
        clauses.append(f"~{F} ~{L}")
        clauses.append(f"~{M} ~{L}")

    for pos in ["F", "M", "L"]:
        t = "T_" + pos
        d = "D_" + pos
        h = "H_" + pos
        clauses.append(f"{t} {d} {h}")
        clauses.append(f"~{t} ~{d}")
        clauses.append(f"~{t} ~{h}")
        clauses.append(f"~{d} ~{h}")

    clauses.append("~T_F H_M")
    clauses.append("~H_F ~H_M")

    clauses.append("~T_M D_M")
    clauses.append("~H_M ~D_M")

    clauses.append("~T_L T_M")
    clauses.append("~H_L ~T_M")

    kb = sat_interface.KB(clauses)

    symbols = [
        "T_F", "T_M", "T_L",
        "D_F", "D_M", "D_L",
        "H_F", "H_M", "H_L"
    ]

    result = {}

    print("An honest name (golfers)")
    print("------------------------")
    for s in symbols:
        v = _entailed_value(kb, s)
        result[s] = v
        print(s + ":", v)
    print("------------------------")

    return result


if __name__ == "__main__":
    print(tt2())
    print(tt3())
    print(salt())
    print(golf())
