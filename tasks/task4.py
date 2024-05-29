def name_triangle(name: str) -> str:
    result: str = ""

    for i in range(1, len(name) + 1):
        for j in range(i):
            result += name[j]
        result += "\n"

    return result

print(name_triangle("Anastasiya"))
