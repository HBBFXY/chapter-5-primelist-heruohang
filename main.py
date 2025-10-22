
    def PrimeList(N):
    # 处理边界情况：N<=2时，没有小于N的质数
    if N <= 2:
        return ""
    
    primes = []
    for num in range(2, N):
        is_prime = True
        # 优化：只需检查到num的平方根
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    
    # 将质数列表转换为空格分隔的字符串
    return " ".join(primes)
