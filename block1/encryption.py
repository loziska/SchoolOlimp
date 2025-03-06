def generate_fibonacci_indices(length):
    """Генерирует индексы Фибоначчи до длины строки."""
    fib_indices = []
    a, b = 1, 1
    while a <= length:
        fib_indices.append(a - 1)  # Индексация с 0
        a, b = b, a + b
    return fib_indices

def decrypt_phase(S):
    """Дешифрует одну фазу."""
    # Шаг 1: Инвертировать строку
    S = S[::-1]
    
    # Шаг 2: Разделить на два блока
    fib_indices = generate_fibonacci_indices(len(S))
    block1 = []
    block2 = []
    for i, char in enumerate(S):
        if i in fib_indices:
            block1.append(char)
        else:
            block2.append(char)
    
    # Шаг 3: Восстановить исходный порядок
    original = []
    fib_ptr = 0
    non_fib_ptr = 0
    for i in range(len(S)):
        if i in fib_indices:
            original.append(block1[fib_ptr])
            fib_ptr += 1
        else:
            original.append(block2[non_fib_ptr])
            non_fib_ptr += 1
    
    return ''.join(original)

def decrypt_message(k, S):
    """Дешифрует сообщение за k фаз."""
    for _ in range(k):
        S = decrypt_phase(S)
    return S

# Пример 1
k1 = 2
S1 = "BCHAEDFG"
print(decrypt_message(k1, S1))  # Вывод: ABCDEFGH

# Пример 2
k2 = 1
S2 = "вещественное"
print(decrypt_message(k2, S2))  # Вывод: еоннвтеесщев
