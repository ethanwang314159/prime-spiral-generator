from PIL import Image
from gen_scripts.next_fp_gen import gen_next_filepath
import os

def grid_gen(inpath: str="rand_images", outpath: str="grid_images", side: int=4, startnum: int=0, open=True):
    filepath = gen_next_filepath(outpath, False, "grid")[0]
    images = []
    for i in range(startnum, startnum+side**2, 1):
        img_path = os.path.join(inpath, f'{i}.png')
        img = Image.open(img_path)
        images.append(img)

    img_width, img_height = images[0].size

    grid_width = side * img_width
    grid_height = side * img_height
    grid_image = Image.new('RGB', (grid_width, grid_height))

    for i, img in enumerate(images):
        row = i // side
        col = i % side
        grid_image.paste(img, (col * img_width, row * img_height))

    grid_image.save(filepath)
    if open:
        grid_image.show()

if __name__ != "__main__":
    print("imported module grid_gen")
else:
    grid_gen()