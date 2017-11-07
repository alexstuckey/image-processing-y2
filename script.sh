#!/bin/bash

python erosion.py lena.png lena_erosion.png;
python dilation.py lena.png lena_dilation.png;
python closing.py lena.png lena_closing.png;
python opening.py lena.png lena_opening.png;
