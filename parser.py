

path = "../contrail/controller/src/ifmap/ifmap_agent_sandesh.cc"

with open(path, "r") as f:
    lines = f.read().splitlines()

l2 = []

i = 0
while i < len(lines):
    oi = i
    if "list_of" in lines[i] and "#include" not in lines[i]:
        l2.append("#if __cplusplus >= 201103L")
        pos = lines[i].find("list_of")
        temp = lines[i][0:pos]
        temp += "{"
        p2 = pos + 8
        while True:
            p3 = lines[i][p2:].find(")")
            temp += lines[i][p2:p2+p3]
            p2 += p3 + 2
            if len(lines[i]) == p2 - 1:
                i += 1
                temp += ","
                l2.append(temp)
                p2 = lines[i].find("(") + 1
                temp = lines[i][:p2-1]
            elif len(lines[i]) == p2 and lines[i][p2-1] == ";":
                break
            else:
                temp += ", "
        temp += "};"
        l2.append(temp)
        l2.append("#else")
        while oi <= i:
            l2.append(lines[oi])
            oi += 1
        l2.append("#endif")
    else:
        l2.append(lines[i])
    i += 1

with open(path, "w") as f:
    for line in l2:
        f.write(line + "\n")
