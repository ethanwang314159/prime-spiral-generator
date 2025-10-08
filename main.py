from gen_scripts.ps_plt_gen import gen_ps_plt
from gen_scripts.rand_settings_gen import gen_random_settings
from gen_scripts.next_fp_gen import gen_next_filepath
from gen_scripts.grid_gen import grid_gen

START = gen_next_filepath("sample_images").removesuffix('.png')
REPEAT = 16
for i in range(REPEAT):
    FILEPATH = gen_next_filepath("rand_images")
    settings = gen_random_settings()
    plt = gen_ps_plt(settings)
    plt.savefig(FILEPATH, dpi=300, bbox_inches='tight', facecolor=settings[4])
grid_gen(startnum=START)