def PrimeList(N):
    # 严格处理边界：N≤2时无质数
    if N <= 2:
        return ""
    
    # 埃氏筛法初始化：标记0~N-1是否为质数
    is_prime = [True] * N
    is_prime[0], is_prime[1] = False, False  # 0和1非质数
    
    # 筛法核心：遍历到√N，标记非质数
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:
            # 从i²开始标记，避免重复
            start = i * i
            is_prime[start:N:i] = [False] * len(is_prime[start:N:i])
    
    # 筛选质数并拼接为空格分隔的字符串
    primes = [str(num) for num, flag in enumerate(is_prime) if flag]
    return " ".join(primes)