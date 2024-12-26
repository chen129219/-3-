import random

# 生成一个指定范围内的素数列表
def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes

# 检查某个数是否是原根
def is_primitive_root(g, p):
    required_set = set(num for num in range(1, p) if gcd(num, p) == 1)
    actual_set = set(pow(g, powers, p) for powers in range(1, p))
    return required_set == actual_set

# 计算最大公约数 (用于判断原根)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 主程序
def diffie_hellman():
    # 1. 选择素数和原根
    primes = generate_primes(100, 255)
    p = random.choice(primes)
    print(f"Selected prime (p): {p}")

    # 找到一个原根
    for g in range(2, p):
        if is_primitive_root(g, p):
            print(f"Found primitive root (g): {g}")
            break

    # 2. 成员 A 和 B 选择私钥
    a = random.randint(2, p - 2)  # A 的私钥
    b = random.randint(2, p - 2)  # B 的私钥
    print(f"A's private key (a): {a}")
    print(f"B's private key (b): {b}")

    # 3. 计算公钥
    A_pub = pow(g, a, p)  # A 的公钥
    B_pub = pow(g, b, p)  # B 的公钥
    print(f"A's public key: {A_pub}")
    print(f"B's public key: {B_pub}")

    # 4. 计算共享密钥
    S_A = pow(B_pub, a, p)  # A 计算的共享密钥
    S_B = pow(A_pub, b, p)  # B 计算的共享密钥
    print(f"Shared key computed by A: {S_A}")
    print(f"Shared key computed by B: {S_B}")

    # 验证共享密钥是否一致
    if S_A == S_B:
        print(f"Diffie-Hellman Key Exchange Successful! Shared key: {S_A}")
    else:
        print("Diffie-Hellman Key Exchange Failed.")

# 运行程序
if __name__ == "__main__":
    diffie_hellman()
