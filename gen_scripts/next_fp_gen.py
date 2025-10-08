import os

def gen_next_filepath(directory, logging=False):
    if not os.path.exists(directory):
        os.makedirs(directory)
    existing_files = os.listdir(directory)
    numbers = []
    for filepath in existing_files:
        if filepath.endswith(".png"):
            try:
                num = int(filepath.split('.')[0])
                numbers.append(num)
            except ValueError:
                pass
    next_number = 0
    while next_number in numbers:
        next_number += 1
    if logging:
        print("Found filepath at", os.path.join(directory, f"{next_number}.png"))
    return os.path.join(directory, f"{next_number}.png")

if __name__ != "__main__":
    print("imported module gen_next_filepath")
else:
    gen_next_filepath("rand_images", True)