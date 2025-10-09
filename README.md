# Prime spiral generator

Inspired by [3b1b's video](https://www.youtube.com/watch?v=EK32jo7i5LQ) on prime spirals and more.
Generates unique prime spirals with Python and `matplotlib`.
The script plots prime numbers with a random colour map onto a grid using polar coordinates.

---

## Sample images

Sample outputs (from `sample_images/`):

| ![Sample 1](sample_images/1.png) | ![Sample 2](sample_images/8.png) | ![Sample 3](sample_images/11.png) |
| :----------------------------: | :----------------------------: | :----------------------------: |
|        Random spiral #2        |        Random spiral #9        |        Random spiral #12        |

| ![Sample 4](sample_images/14.png) | ![Sample 5](sample_images/16.png) | ![Sample 6](sample_images/18.png) |
| :----------------------------: | :----------------------------: | :----------------------------: |
|        Random spiral #15        |        Random spiral #17        |        Random spiral #19        |

`sample_images/` includes 20 sample images

Sample grid outputs (from `grid_images/`):

![Grid 1](grid_images/grid0.png/)
4 by 4 grid

![Grid 2](grid_images/grid1.png)
33 by 33 grid

`sample_images/` includes 2 sample grids

---

## Installation

### Requirements

* **Python 3.10+**
* The following libraries:

  ```
  matplotlib
  random
  math
  ```

### Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/ethanwang314159/prime-spiral-generator.git
   cd prime-spiral-generator
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

```bash
python main.py
```
Generates 16 unique spirals and then a 4 by 4 grid with those spirals into `rand_images` and `grid_images`.

---

## File Structure

```
prime-spiral-generator/
│
├── gen_scripts/
│   ├── next_fp_gen.py         # Finds next available file path in folder
│   ├── ps_plt_gen.py          # Generates prime spiral plot (returns plt)
│   └── rand_settings_gen.py   # Creates random settings
│   └── grid_gen.py            # Generates a grid of spirals
│
├── rand_images/               # Empty (for now)
│
├── sample_images/
│   └── 0.png ... 19.png       # Sample images
│
├── grid_images/
│   └── grid0.png              # 4x4 Sample grid image
│   └── grid1.png              # 33x33 Sample grid image
│
└── main.py                    # Main script for spiral generation
```

---

## Todo

*** Animation:** visualise the spirals forming like the primes getting loaded in (maybe gifs).  
*** Interactive:** adjustable spiral settings in a good ui. like change the size by dragging/clicking not typing a number.  
*** Vote:** a website where you vote between two spirals and using an algorithm like the elo system find the perfect spiral with a leaderboard etc  

---

## License

MIT license.