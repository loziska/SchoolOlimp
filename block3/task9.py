def count_valid_splits(n, C, k, S):
    mod = 10 ** k
    dp = [0] * (n + 1)
    dp[0] = 1

    max_len = len(str(C))

    for i in range(1, n + 1):
        for l in range(1, max_len + 1):
            j = i - l
            if j < 0:
                break
            num_str = S[j:i]
            if num_str[0] == '0' and len(num_str) > 1:
                continue
            if int(num_str) <= C:
                dp[i] = (dp[i] + dp[j]) % mod

    return str(dp[n]).zfill(k)  # добавляем ведущие нули, если нужно


# Ввод
n, C, k = map(int, input().split())
S = input().strip()

print(count_valid_splits(n, C, k, S))

# 3 11 2
# 111

# 10 9 1
# 0123456789876543210

# 1 8 3
# 9
