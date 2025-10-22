# 在此文件中实现 PrimeList 函数

def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    primes = []
    for num in range(2, N):
        # 假设当前数是质数
        is_prime = True
        # 检查是否能被2到sqrt(num)之间的数整除
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 用空格连接列表元素，末尾无空格
    return ' '.join(primes)

# 示例测试（可根据实际需求调用）
# print(PrimeList(10))  # 输出：2 3 5 7
