def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Каждый символ — палиндром длины 1
    for i in range(n):
        dp[i][i] = 1

    # Заполняем для подстрок длины от 2 до n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]

# Пример использования:
s = "bbbbab"
print(longest_palindromic_subsequence(s))  # Вывод: 4 ("bbbb")

s = "муха цокотуха"
print(longest_palindromic_subsequence(s))  # Вывод: 5 ("уокоу" или "хокох")

# Определение подзадач:
# Пусть dp[i][j] — длина LPS для подстроки s[i..j].

# Если i == j, то dp[i][j] = 1 (один символ всегда палиндром).
# Если s[i] == s[j], то dp[i][j] = dp[i + 1][j - 1] + 2.
# Если s[i] != s[j], то dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]).

# Заполнение таблицы dp:
# Заполняем диагональ dp[i][i] = 1.
# Заполняем таблицу для подстрок длиной от 2 до n.
