def is_palindromic(cadena: str) -> bool:
    return all(cadena[i] == cadena[~i] for i in range(len(cadena) // 2))

print(is_palindromic("racecar"))


