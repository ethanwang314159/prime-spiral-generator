import os, bisect
from gen_scripts.prime_gen.primes_cacher import save_primes

primes_cache = []

def get_primes_cache(n): # O(N) I think because it has to iterate through each line when reading the file
    global primes_cache
    if not primes_cache:
        filename = "gen_scripts/prime_gen/primes_cache.rs"
        if not os.path.exists(filename):
            print(f"Cache file '{filename}' not found. Running prime_cacher.py")
            save_primes()
            return get_primes_cache()
        with open(filename, "r") as f:
            primes_cache = [int(line.strip()) for line in f.readlines()]

    idx = bisect.bisect_right(primes_cache, n)
    primes = primes_cache[:idx]
    return (primes, str(len(primes)), primes[-1])
    