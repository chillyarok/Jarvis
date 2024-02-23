def notab(lis):
    fff = []
    for s in lis:
        if"\n" in s:
            s = s[:-1]
            fff.append(s)
        else:
            fff.append(s)
    return fff


def table_to_list(file: str):
    with open(file,encoding="utf-8") as file:
        stph = file.readlines()
        stph = notab(stph)
        return stph