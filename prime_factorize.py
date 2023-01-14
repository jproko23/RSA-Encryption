import time

num = int(input("Enter a large number: "))


def is_prime(num):
    end = num//2
    for i in range(2, int(end + 1)) :
        if num % i == 0: return False
    return True

def prime_factorize(num):
    ts = time.time()
    if is_prime(num):
        return (1, num)

    prime_facts = []
    fact_pairs = []

    for i in range(2, ((num//2) + 1)) :
        if i not in prime_facts: 
            if is_prime(i) and num%i == 0 : 
                prime_facts.append(i)

                if is_prime(num/i):
                    fact_pairs.append((i, int(num/i)))
                    prime_facts.append(num/i)
    print(f"runtime{ts-time.time()}")
    return fact_pairs

print(prime_factorize(num))
