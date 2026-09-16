
l = input("Write me a sentance. ").split()
names = input("Write some names. ").split()

def dict_comprehension(words: list[str]) -> dict[str, int]:
    return {i: len(i) for i in l}

def set_comprehension(names: list[str]) -> set[str]:
    return {names[n][0].lower() for n in range(len(names))}
    
        

print(dict_comprehension(l))
print(set_comprehension(names))





