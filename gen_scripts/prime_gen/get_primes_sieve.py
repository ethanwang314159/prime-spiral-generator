def get_primes_sieve(n): # O(N log (log N)) https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
        p += 1
    primes = [i for i, prime_status in enumerate(is_prime) if prime_status]
    return (primes, str(len(primes)), primes[-1])