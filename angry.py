import time
from smiley import Smiley


class Angry(Smiley):
    """
    Provides a Smiley with an angry expression
    """
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        """
        Draws an angry mouth by blanking specific pixels
        """
        mouth = [42, 43, 44, 45, 50, 53]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws angry eyes on the smiley
        :param wide_open: Render eyes wide open or shut
        """
        eyes = [10, 13, 18, 21]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.complexion()
            self.pixels[pixel] = eyes
