from gen_scripts.ps_plt_gen import gen_ps_plt
from gen_scripts.rand_settings_gen import gen_random_settings
from gen_scripts.next_fp_gen import gen_next_filepath
from gen_scripts.grid_gen import grid_gen
from gen_scripts.empty_folder_gen import clear_folder

def grid_gen_final(side=4, outpath="grid_images", temploc="rand_images", keep=True):
    START = gen_next_filepath(outpath)[1]
    SIDE = side
    AREA = SIDE**2

    for i in range(AREA):
        FILEPATH = gen_next_filepath(temploc)[0]
        settings = gen_random_settings()
        plt = gen_ps_plt(settings)
        plt.savefig(FILEPATH, dpi=300, bbox_inches='tight', facecolor=settings[4])
        plt.close()

    grid_gen(startnum=int(START), side=SIDE, inpath=temploc)
    if not keep:
        clear_folder(temploc)

grid_gen_final()