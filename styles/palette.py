#!/usr/bin/env python3.10
"""Normalize colors to be used for the Shishkin palette."""
import itertools as it
import sys

import colour
import more_itertools as mit


colors = {
    "cyan": "#4cc9f0",
    "green": "#4895ef",
    "blue": "#3a0ca3",
    "purple": "#7209b7",
    "red": "#DD2B6E",
    "orange": "#F5B719",
    "yellow": "#F5F219",
}


gray_hues = {
    "white": 0.95,
    "very-light-gray": 0.4,
    "light-gray": 0.3,
    "gray": 0.225,
    "dark-gray": 0.125,
    "very-dark-gray": 0.075,
}

base_gray = list(colour.hex2hsl("#171626"))


def main(argv) -> None:
    with open("colors.less", "w") as file:
        for name, color in colors.items():
            hsl = list(colour.hex2hsl(color))
            hsl[1] = 0.7
            hsl[2] = 0.5
            file.write(f"@{name}: {colour.hsl2hex(hsl)};\n")

        for hue_name, lightness in gray_hues.items():
            hsl = base_gray.copy()
            hsl[0] -= (lightness * 0.1)
            hsl[1] += (lightness * 0.1)
            hsl[2] = lightness
            file.write(f"@{hue_name}: {colour.hsl2hex(hsl)};\n")


if __name__ == '__main__':
    main(sys.argv)
