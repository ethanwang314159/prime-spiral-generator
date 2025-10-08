import random, math

def random_colour(): 
    return (random.random(), random.random(), random.random())

def random_cmap():
    positions = [random.random()]
    if positions[0] > 0: positions = [0] + positions
    if positions[-1] < 1: positions = positions + [1]
    return [(pos, random_colour()) for pos in positions]

def random_marker():
    markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h', 'v', '^', '<', '>', '1', '2', '3', '4', '|', '_']
    return random.choice(markers)

def random_size(start=0.2, stop=4, factor=1.5):
    values = []
    value = start
    while value <= stop:
        values.append(value)
        value *= factor
    return random.choice(values)

def random_bigness(min_bigness=10000, max_bigness=1000000):
    scale_factor = random.random() 
    bigness = min_bigness * math.exp(scale_factor * (math.log(max_bigness) - math.log(min_bigness)))
    return int(bigness)

def gen_random_settings(log=False):
    CMAP = random_cmap()
    BIGNESS = random_bigness()
    SIZE = random_size()
    MARKER = random_marker()
    BG = "black"
    settings = (CMAP, BIGNESS, SIZE, MARKER, BG)
    if log == True:
        print(settings)
    return settings

if __name__ != "__main__":
    print("imported module rand_settings_gen")
else:
    settings = gen_random_settings(True)