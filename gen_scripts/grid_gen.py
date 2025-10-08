from PIL import Image
from gen_scripts.next_fp_gen import gen_next_filepath
import os

def grid_gen(inpath="rand_images", outpath="grid_images", side=4, startnum=0):
    filepath = gen_next_filepath(outpath, False, "grid")
    images = []
    for i in range(startnum, startnum+side**2, 1):
        img_path = os.path.join(inpath, f'{i}.png')
        img = Image.open(img_path)
        images.append(img)

    img_width, img_height = images[0].size

    grid_width = 4 * img_width
    grid_height = 4 * img_height
    grid_image = Image.new('RGB', (grid_width, grid_height))

    for i, img in enumerate(images):
        row = i // 4
        col = i % 4
        grid_image.paste(img, (col * img_width, row * img_height))

    grid_image.save(filepath)
    grid_image.show()

if __name__ != "__main__":
    print("imported module grid_gen")
else:
    grid_gen()