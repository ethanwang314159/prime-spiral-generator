from gen_scripts.ps_plt_gen import gen_ps_plt
from gen_scripts.rand_settings_gen import gen_random_settings
from gen_scripts.next_fp_gen import gen_next_filepath
from gen_scripts.grid_gen import grid_gen

START = gen_next_filepath("rand_images")[1]
SIDE = 4
AREA = SIDE**2

for i in range(AREA):
    FILEPATH = gen_next_filepath("rand_images")[0]
    settings = gen_random_settings()
    plt = gen_ps_plt(settings)
    plt.savefig(FILEPATH, dpi=300, bbox_inches='tight', facecolor=settings[4])

grid_gen(startnum=int(START), side=SIDE)