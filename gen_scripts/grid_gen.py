from PIL import Image
from gen_scripts.next_fp_gen import gen_next_filepath
import os

def grid_gen(inpath: str="rand_images", outpath: str="grid_images", side=4, startnum=0, max_size=(3000, 3000), open=True):
    filepath = gen_next_filepath(outpath, False, "grid")[0]
    images = []
    
    for i in range(startnum, startnum + side**2, 1):
        img_path = os.path.join(inpath, f'{i}.png')
        img = Image.open(img_path)
        
        img.thumbnail((max_size[0] // side, max_size[1] // side))
        
        images.append(img)

    img_width, img_height = images[0].size

    grid_width = side * img_width
    grid_height = side * img_height

    if grid_width > max_size[0] or grid_height > max_size[1]:
        scaling_factor = min(max_size[0] / grid_width, max_size[1] / grid_height)
        grid_width = int(grid_width * scaling_factor)
        grid_height = int(grid_height * scaling_factor)

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
