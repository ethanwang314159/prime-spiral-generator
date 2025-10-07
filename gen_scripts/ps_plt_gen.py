import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

DEFAULT_SETTINGS = ([(0, (0.03286600111091176, 0.9976179605209301, 0.9845250497488386)), (0.4299406771403493, (0.06465992780789409, 0.7582066062461121, 0.6683053114060715)), (1, (0.8171504997567098, 0.03270786797985625, 0.2416026008392388))], 500000, 1, 'o', 'black')

def get_primes(n):
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

def gen_ps_plt(settings=DEFAULT_SETTINGS, log=False):
    CMAP, BIGNESS, SIZE, MARKER, BG = settings
    primes = get_primes(BIGNESS)
    if log:
        print(primes[1], "primes")
    r = np.array(primes[0])
    plt.figure(figsize=(8, 8), facecolor=BG)
    ax = plt.subplot(projection='polar')
    ax.set_facecolor(BG)
    ax.grid(False)
    ax.set_xticks([])
    ax.set_rticks([])
    ax.spines['polar'].set_visible(False)
    norm = plt.Normalize(vmin=min(r), vmax=max(r))
    cmap = LinearSegmentedColormap.from_list(name="", colors=CMAP)
    ax.scatter(r, r, c=r, cmap=cmap, s=SIZE, norm=norm, marker=MARKER)
    ax.set_rmax(primes[2] + SIZE)
    return plt

if __name__ != "__main__":
    print("imported module gen_ps_plt")
else:
    plt = gen_ps_plt(log=True)
    plt.savefig("default.png", dpi=300, bbox_inches='tight', facecolor='black')
    os.startfile("default.png")