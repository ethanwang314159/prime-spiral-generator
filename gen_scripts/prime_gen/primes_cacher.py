from gen_scripts.prime_gen.get_primes_sieve import get_primes_sieve
import os

def save_primes(limit=100000000, filename="gen_scripts/prime_gen/primes_cache.rs", log=False):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            f.readline()
            cached_primes = [int(line.strip()) for line in f.readlines()]
    else:
        cached_primes = []
    highest_cached_prime = cached_primes[-1] if cached_primes else 1
    primes = get_primes_sieve(limit)
    new_primes = [prime for prime in primes if prime > highest_cached_prime]
    if new_primes:
        with open(filename, "a") as file:
            for prime in new_primes:
                file.write(f"{prime}\n")
        if log:
            print(f"Primes up to {limit} saved to {filename}.")
    else:
        if log:
            print(f"All primes upt o {limit} already found in {filename}.")