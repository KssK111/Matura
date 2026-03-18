from collections import defaultdict

with open("telefony.txt") as f:
    telefony = [t.strip() for t in f]

print(f"a)\n{len(list(filter(lambda t: t == "504669045", telefony)))}")

numer_ile = defaultdict(int)
for t in telefony:
    numer_ile[t] += 1
print(f"b)")
maks_t = max(numer_ile.keys(), key=lambda t: numer_ile[t])
print(maks_t)
print(numer_ile[maks_t])

print(f"c)\n{len(list(filter(lambda t: t.startswith("511"), telefony)))}")

def suma_cyfr_parz_w_od_42(tel: str) -> bool:
    parz = lambda x: x % 2 == 0
    return sum(filter(parz, map(int, tel))) > 42
print(f"d)\n{len(list(filter(suma_cyfr_parz_w_od_42, telefony)))}")

def min_4_1(tel: str) -> bool:
    return len(list(filter(lambda l: l == "1", tel))) >= 4


