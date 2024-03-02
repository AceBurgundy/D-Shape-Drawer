# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from frame.three_dimensional.canvas import Canvas
    from geometry.shapes import Shape

from typing import Dict, List
from tkinter import Event
from OpenGL.GLU import *
from OpenGL.GL import *

def __get_pressed_status(event: Event):
    """
    Filters data returned by CTk Key Press event

    Args:
        event (Event): A Tkinter event object representing the key press event.
    """
    result: Dict[str, List|str] = {}

    for part in str(event).split():

        if 'state=' in part:
            state_value: str = part.split('=')[1]
            state_value = state_value.rstrip('>')

            if '|' in state_value:
                result['state'] = state_value.split('|')

            elif state_value != '0x40000':
                result['state'] = [state_value]

        if 'keysym=' in part:
            key_value: str = part.split('=')[1]
            key_value = key_value.rstrip('>')
            result["key"] = key_value

    return result

def handle_key_pressed(canvas_instance: Canvas, event) -> None:
    """
    Handles key pressed events sent from main CTk frame
    """
    press_status: Dict[str, List[str]|str] = __get_pressed_status(event)
    key: List[str]|str = press_status['key']

    if type(key == 'str'):
        if key == 'Up':
            canvas_instance.camera_zoom_translate -= Shape.default_increment

        elif key == 'Down':
            canvas_instance.camera_zoom_translate += Shape.default_increment

        elif key == 'w':
            canvas_instance.__move_camera([0, 0, 1]) # forward_vector

        elif key == 's':
            canvas_instance.__move_camera([0, 0, -1]) # backward_vector

        elif key == 'a':
            canvas_instance.__move_camera([1, 0, 0]) # left_vector

        elif key == 'd':
            canvas_instance.__move_camera([-1, 0, 0]) # right_vector