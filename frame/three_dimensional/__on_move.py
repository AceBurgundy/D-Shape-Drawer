# for type checking purposes.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from frame.three_dimensional.canvas import Canvas

from geometry.shapes import Shape
from tkinter import Event

def on_mouse_move(canvas_instance: Canvas, event: Event):
    """
    Handles mouse move event

    Args:
        canvas_instance (Canvas): The current instance of the canvas
        event (Event): A Tkinter event object representing the key press event.
    """
    Shape.mouse_x = event.x
    Shape.mouse_y = event.y

    if canvas_instance.mouse_pressed != '':
        canvas_instance.dragging = True

    if canvas_instance.mouse_pressed == 'Right':
        canvas_instance.mouse_x, canvas_instance.mouse_y = event.x, event.y