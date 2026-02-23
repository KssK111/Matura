with open("slowa.txt") as f:
    slowa = list(map(str.strip, f.readlines()))

palindromy = list(filter(lambda s: s == "".join(reversed(s)), slowa))
print(f"4.1\nIlość palindromów: {len(palindromy)}")

print(f"4.2\nIlość rodzin: {len(set(map(len, palindromy)))}")

from collections import defaultdict
rodziny = defaultdict(list[str])
[rodziny[len(x)].append(x) for x in palindromy]

with open("rodziny.txt", "w") as f:
    f.write("\n".join(map(lambda r: " ".join(sorted(r)), rodziny.values())))