import os
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from gen_scripts.prime_gen.get_primes_sieve import get_primes_sieve
from gen_scripts.prime_gen.get_primes_cache import get_primes_cache

DEFAULT_SETTINGS = ([(0, (0.03286600111091176, 0.9976179605209301, 0.9845250497488386)), (0.4299406771403493, (0.06465992780789409, 0.7582066062461121, 0.6683053114060715)), (1, (0.8171504997567098, 0.03270786797985625, 0.2416026008392388))], 500000, 1, 'o', 'black')

def gen_ps_plt(settings=DEFAULT_SETTINGS, log=False, prime_gen_method="sieve"):
    CMAP, BIGNESS, SIZE, MARKER, BG = settings
    match prime_gen_method:
        case "sieve":
            primes = get_primes_sieve(BIGNESS)
        case "cache":
            primes = get_primes_cache(BIGNESS)
        case _:
            raise ValueError("incorrect prime_gen_method parameter")
    if log:
        print(primes[1], "primes")
    r = primes[0]
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