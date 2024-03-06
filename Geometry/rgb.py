from typing import Iterable, Callable, Tuple
from custom_types import *
from random import random

def random_rgb(exemption_list: RGBS|None = None) -> RGB:
    """
    Generates random RGB float values between 0.0 and 1.0 for OpenGL.GL.
    Ensures the generated RGB tuple is unique in the buffer_colors.

    Args:
        exemption_list (List[Tuple[float, float, float]]): List of rgb tuples to avoid

    Returns:
        Tuple: A Tuple containing three random float values between 0.0 and 1.0 representing RGB color.
    """
    color: Callable = lambda: round(random(), 2)
    new_rgb: Callable = lambda: tuple(color() for _ in range(3))

    new_color = new_rgb()

    if exemption_list:
        while new_color in exemption_list:
            new_color = new_rgb()

    return new_color

def process_rgb(rgb_argument: Iterable[int|float]) -> RGB:
    """
    Processes the passed rgb argument.

    Args:
        An Iterable of rgb values

    Raises:
        TypeError: If the rgb_argument is not an Iterable
        TypeError: If the length of the rgb_argument is not equal to 3
        TypeError: If one of the elements is an integer not within 0-255
        TypeError: If one of the elements is a float not within 0-1.0

    Returns:
        The rgb_argument in tuple where each element is a float between 0-1.00
    """
    if not isinstance(rgb_argument, Iterable):
        raise TypeError("RGB argument must be an Iterable")

    clean_rgb: Tuple[float, ...] = tuple(rgb_argument)

    if len(clean_rgb) != 3:
        raise TypeError("Length of rgb argument must be equal to 3")

    if not isinstance(clean_rgb, (list, tuple, set, dict)):
        raise TypeError("Rgb argument is not iterable")

    for element in clean_rgb:
        if isinstance(element, int) and element > 255 or element < 0:
            raise TypeError("An integer element is greater than 255 or less than 0")

    for element in clean_rgb:
        if isinstance(element, float) and (element > 1.0 or element < 0):
            raise TypeError("A float element is greater than 1.0 or less than 0")

    to_float: Callable = lambda color: round(color / 255, 2) if isinstance(color, int) else round(color, 2)

    red: float = to_float(clean_rgb[0])
    green: float = to_float(clean_rgb[1])
    blue: float = to_float(clean_rgb[2])

    return (red, green, blue)