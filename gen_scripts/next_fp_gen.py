import os

def gen_next_filepath(directory):
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
    return os.path.join(directory, f"{next_number}.png")

if __name__ != "__main__":
    print("imported module gen_next_filepath")
else:
    pass