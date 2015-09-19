from wand.image import Image
from wand.color import Color
from wand.drawing import Drawing
from wand.compat import nested
import random
import time
import os
import math
import linecache

baseImage = Image(width=150, height=32, background=Color('rgb('+str(189)+','+str(191)+','+str(251)+')'))

draw = Drawing()
draw.fill_color = Color('white')
draw.font_size = 40

# ---------------word pattern---------------------------
wenli = Image(filename="./1.jpg")
wenli_width = wenli.size[0]
wenli_height = wenli.size[1]

print(wenli_width)
print(wenli_height)

draw.push_pattern("check", 0, 0, wenli_width, wenli_height)
# operations:
# wand.image.COMPOSITE_OPERATORS = ('undefined', 'no', 'add', 'atop', 'blend', 'bumpmap', 'change_mask', 'clear', 'color_burn', 'color_dodge', 'colorize', 'copy_black', 'copy_blue', 'copy', 'copy_cyan', 'copy_green', 'copy_magenta', 'copy_opacity', 'copy_red', 'copy_yellow', 'darken', 'dst_atop', 'dst', 'dst_in', 'dst_out', 'dst_over', 'difference', 'displace', 'dissolve', 'exclusion', 'hard_light', 'hue', 'in', 'lighten', 'linear_light', 'luminize', 'minus', 'modulate', 'multiply', 'out', 'over', 'overlay', 'plus', 'replace', 'saturate', 'screen', 'soft_light', 'src_atop', 'src', 'src_in', 'src_out', 'src_over', 'subtract', 'threshold', 'xor', 'divide')
draw.composite('overlay', 0, 0, 0, 0, wenli)
draw.pop_pattern()
draw.set_fill_pattern_url("#check")
# ------------------------------------------------------

draw.text(x=50, y=19, body="Lorem ipsum")
draw.draw(baseImage)
baseImage.save(filename='./_testImg.jpg')