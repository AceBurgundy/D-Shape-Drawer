from Geometry.Shapes import Shape
from typing import override
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

from custom_types import *
from constants import *

class Cylinder(Shape):

    def __init__(self, radius: NUMBER = 1.0, height: NUMBER = 2.0, slices: NUMBER = 3) -> None:
        """
        Initializes the sphere

        Args:
            radius (NUMBER): the radius of the sphere. Defaults to 1.0
            height (NUMBER): the height of the sphere. Defaults to 2.0
            slices (NUMBER): the slices of the sphere. Defaults to 3
        """
        self.radius: NUMBER = radius
        self.height: NUMBER = height
        self.slices: NUMBER = slices

    @override
    def __change_shape(self, increment: bool = True) -> None:
        """
        Increases or decreases the size of the cube by Shape.resize_value units.

        Args:
            increment (bool): If True, increase the size, else decrease. Defaults to True.
        """
        if increment:
            self.radius += Shape.resize_value
            self.height += Shape.resize_value
            self.slices += Shape.resize_value
        else:
            if self.width > Shape.resize_value and self.height > Shape.resize_value and self.depth > Shape.resize_value:
                self.radius -= Shape.resize_value
                self.height -= Shape.resize_value
                self.slices -= Shape.resize_value

    @override
    def draw(self, offscreen) -> None:
        """
        Draws the cylinder
        """
        assigned_buffer_color: RGB = Shape.buffer_colors[self.__class__.__name__]
        glColor3f(*self.background_color if not offscreen else assigned_buffer_color)

        quadric = gluNewQuadric()
        cylinder_arguments: Tuple[any, NUMBER, NUMBER, NUMBER] = (
            quadric,
            self.radius, self.radius,
            self.height,
            self.slices, self.slices
        )

        gluQuadricDrawStyle(quadric, GLU_FILL)
        gluCylinder(*cylinder_arguments)

        if self.show_grid:
            glColor3f(*self.grid_color)
            quadric = gluNewQuadric()
            gluQuadricDrawStyle(quadric, GLU_LINE)
            gluCylinder(*cylinder_arguments)

        for slice_ in range(self.slices + 1):
            theta: NUMBER = 2 * pi * slice_ / self.slices
            for index in range(2):  # Two vertices for each circle (top and bottom)
                x: NUMBER = self.radius * cos(theta)
                y: NUMBER = self.radius * sin(theta)
                z: NUMBER = index * self.height
                self.vertices.append((x, y, z))
