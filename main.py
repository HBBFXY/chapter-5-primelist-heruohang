
    def PrimeList(N):
    """
    生成所有小于N的质数，以空格分隔的字符串形式返回
    :param N: 整数，筛选质数的上限（不包含N）
    :return: 质数组成的字符串，无质数时返回空字符串
    """
    # 处理边界情况：N≤2时无质数，直接返回空字符串
    if N <= 2:
        return ""
    
    # 初始化布尔数组（埃氏筛法）：is_prime[i]表示i是否为质数
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False  # 0和1不是质数
    
    # 埃氏筛法核心：遍历并标记非质数
    for i in range(2, int(N ** 0.5) + 1):
        if is_prime[i]:  # 若i是质数，标记其所有倍数为非质数
            is_prime[i*i : N : i] = [False] * len(is_prime[i*i : N : i])
    
    # 筛选出所有质数，转换为字符串并拼接
    prime_str = " ".join(str(num) for num, is_p in enumerate(is_prime) if is_p)
    
    return prime_str