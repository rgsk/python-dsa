
def sieve_of_eratosthenes(n):
    if n < 2:
        return []  # No primes below 2

    # Create a boolean array "is_prime" and initialize all entries as True
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes

    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            # Mark multiples of p as False starting from p^2
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    # Collect all numbers marked as prime
    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes
