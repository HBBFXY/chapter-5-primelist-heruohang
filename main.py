def PrimeList(N):
    # 存储小于N的质数
    primes = []
    # 遍历2到N-1的所有数
    for num in range(2, N):
        # 假设当前数是质数
        is_prime = True
        # 检查是否能被2到sqrt(num)整除
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 用空格连接质数列表，空列表则返回空字符串
    return " ".join(primes)