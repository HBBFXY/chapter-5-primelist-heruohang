def isPrime(num):
    """辅助函数：判断一个数是否为素数"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def PrimeList(N):
    """生成小于N的所有素数，以空格分隔输出"""
    primes = []
    for num in range(2, N):
        if isPrime(num):
            primes.append(str(num))
    # 将列表转为空格分隔的字符串（末尾无空格）
    return ' '.join(primes)

# 测试示例（可根据需要删除）
print(PrimeList(20))  # 输出：2 3 5 7 11 13 17 19