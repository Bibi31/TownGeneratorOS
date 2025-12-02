"""Color palettes for map rendering."""


class Palette:
    """Color palette for rendering."""
    
    def __init__(self, paper: int, light: int, medium: int, dark: int):
        """Initialize a palette with four colors."""
        self.paper = paper
        self.light = light
        self.medium = medium
        self.dark = dark
    
    # Predefined palettes
    DEFAULT = None
    BLUEPRINT = None
    BW = None
    INK = None
    NIGHT = None
    ANCIENT = None
    COLOUR = None
    SIMPLE = None


# Initialize predefined palettes
Palette.DEFAULT = Palette(0xccc5b8, 0x99948a, 0x67635c, 0x1a1917)
Palette.BLUEPRINT = Palette(0x455b8d, 0x7383aa, 0xa1abc6, 0xfcfbff)
Palette.BW = Palette(0xffffff, 0xcccccc, 0x888888, 0x000000)
Palette.INK = Palette(0xcccac2, 0x9a979b, 0x6c6974, 0x130f26)
Palette.NIGHT = Palette(0x000000, 0x402306, 0x674b14, 0x99913d)
Palette.ANCIENT = Palette(0xccc5a3, 0xa69974, 0x806f4d, 0x342414)
Palette.COLOUR = Palette(0xfff2c8, 0xd6a36e, 0x869a81, 0x4c5950)
Palette.SIMPLE = Palette(0xffffff, 0x000000, 0x000000, 0x000000)
