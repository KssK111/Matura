def ciag_keith_k(k: int) -> list[int]:
    ciag = list(map(int, str_k := str(k)))
    while (nastepny := sum(ciag[len(ciag) - len(str_k):])) <= k:
        ciag.append(nastepny)
    return ciag

def is_keith(k: int) -> bool:
    return k in ciag_keith_k(k)
    
list(map(lambda x: print(f"{x} - {is_keith(x)} - {ciag_keith_k(x)}"), [197, 12, 14, 109]))