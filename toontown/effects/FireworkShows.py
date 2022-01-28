
from .FireworkGlobals import *
from toontown.toonbase import ToontownGlobals
from toontown.parties import PartyGlobals

shows = {
    ToontownGlobals.JULY4_FIREWORKS: [
        # Toontown Central
        (
            # waitTime, style, colorIndex1, colorIndex2, amp, x, y, z
            (2, ROCKET, RED, RED, 5, 80, 88, 30),
            (0.1, ROCKET, BLUE, BLUE, 5, 80, -88, 30),
            (0.1, ROCKET, WHITE, WHITE, 5, 80, -66, 30),
            (0.1, ROCKET, WHITE, WHITE, 5, 80, 66, 30),
            (0.1, ROCKET, BLUE, BLUE, 5, 80, 44, 30),
            (0.1, ROCKET, RED, RED, 5, 80, -44, 30),
            (0.1, ROCKET, RED, RED, 5, 80, 22, 30),
            (0.1, ROCKET, BLUE, BLUE, 5, 80, -22, 30),
            (0.1, ROCKET, WHITE, WHITE, 5, 80, 0, 30),

            (2, CIRCLELARGE, RED, RED, 20, 120, -2, 120),
            (0.1, CIRCLE, RED, RED, 12, 120, -30, 150),
            (0.1, CIRCLE, RED, RED, 12, 120, 26, 150),
            (1.5, ROCKET, WHITE, YELLOW, 3, 80, -40, 0),
            (0.2, ROCKET, WHITE, YELLOW, 3, 80, -20, 0),
            (0.2, ROCKET, WHITE, YELLOW, 3, 80, 0, 0),
            (0.2, ROCKET, WHITE, YELLOW, 3, 80, 20, 0),
            (0.2, ROCKET, WHITE, YELLOW, 3, 80, 40, 0),

            (2, CIRCLE, BLUE, BLUE, 6, 80, -40, 70),
            (0.2, CIRCLE, RED, RED, 7, 80, -20, 70),
            (0.2, CIRCLELARGE, WHITE, WHITE, 8, 80, 0, 70),
            (0.2, CIRCLE, RED, RED, 7, 80, 20, 70),
            (0.2, CIRCLE, BLUE, BLUE, 6, 80, 40, 70),

            (1, CIRCLE, WHITE, WHITE, 14, 80, 0, 80),
            (0.1, CIRCLE, WHITE, WHITE, 7, 80, -10, 90),
            (0.1, CIRCLE, WHITE, WHITE, 7, 80, 10, 90),

            (1, ROCKET, WHITE, YELLOW, 3, -40, 0, 0),
            (0.2, ROCKET, WHITE, YELLOW, 3, -20, 0, 0),
            (0.2, ROCKET, WHITE, YELLOW, 3, 0, 0, 0),
            (0.2, ROCKET, WHITE, YELLOW, 3, 20, 0, 0),
            (0.2, ROCKET, WHITE, YELLOW, 3, 40, 0, 0),

            (2, CIRCLE, BLUE, BLUE, 6, -40, 0, 60),
            (0.2, CIRCLE, RED, RED, 7, -20, 0, 60),
            (0.2, CIRCLE, WHITE, WHITE, 8, 0, 0, 60),
            (0.2, CIRCLE, RED, RED, 7, 20, 0, 60),
            (0.2, CIRCLE, BLUE, BLUE, 6, 40, 0, 60),
            (1.5, CIRCLE, WHITE, WHITE, 10, 0, 0, 80),
            (0.1, CIRCLE, WHITE, WHITE, 5, -10, 0, 90),
            (0.1, CIRCLE, WHITE, WHITE, 5, 10, 0, 90),

            (2, ROCKET, WHITE, YELLOW, 3, -40, 0, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, -20, 0, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, 0, 0, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, 20, 0, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, 40, 0, 0),

            (1.5, CIRCLE, BLUE, RED, 10, -30, -30, 80),
            (0.1, RING, WHITE, WHITE, 10, -30, -30, 80),
            (0.5, CIRCLE, BLUE, RED, 10, 30, -30, 80),
            (0.1, RING, WHITE, WHITE, 10, 30, -30, 80),
            (0.5, CIRCLE, BLUE, RED, 10, -30, 30, 80),
            (0.1, RING, WHITE, WHITE, 10, -30, 30, 80),
            (0.5, CIRCLE, BLUE, RED, 10, 30, 30, 80),
            (0.1, RING, WHITE, WHITE, 10, 30, 30, 80),

            (2, CIRCLELARGE, RED, WHITE, 16, 0, 0, 100),
            (2, CIRCLELARGE, BLUE, WHITE, 16, 0, 0, 100),

            (2, CIRCLE, RED, RED, 8, -10, 0, 90),
            (0.3, CIRCLE, BLUE, BLUE, 10, 0, 20, 60),
            (0.3, CIRCLE, RED, RED, 5, 10, 10, 80),
            (0.5, CIRCLE, RED, BLUE, 8, -10, 0, 90),
            (0.4, CIRCLE, RED, BLUE, 10, 0, 10, 60),
            (0.4, CIRCLE, RED, WHITE, 8, -10, 0, 90),
            (0.5, CIRCLE, BLUE, WHITE, 10, 0, -20, 80),
            (0.4, CIRCLE, WHITE, WHITE, 5, 10, 0, 90),

            (1, CIRCLE, WHITE, WHITE, 15, 0, 0, 100),

            (1.5, ROCKET, WHITE, YELLOW, 5, 0, 0, 0),

            (2, RING, RED, RED, 8, 0, 0, 100),
            (0.1, RING, BLUE, BLUE, 8, 0, 0, 100),
            (1.5, ROCKET, RED, RED, 5, 82, -47, 20),
            (0.1, ROCKET, RED, RED, 5, 93, 45, 26),
            (0.1, ROCKET, RED, RED, 5, 37, -47, 20),
            (0.1, ROCKET, RED, RED, 5, 60, 45, 26),
            (1.5, ROCKET, BLUE, BLUE, 5, 82, -47, 20),
            (0.1, ROCKET, BLUE, BLUE, 5, 93, 45, 26),
            (0.1, ROCKET, BLUE, BLUE, 5, 37, -47, 20),
            (0.1, ROCKET, BLUE, BLUE, 5, 60, 45, 26),

            (2, ROCKET, WHITE, YELLOW, 3, -20, 0, 0),
            (0.1, ROCKET, WHITE, YELLOW, 3, 0, 0, 0),
            (0.1, ROCKET, WHITE, YELLOW, 3, 20, 0, 0),
            (0.1, ROCKET, WHITE, YELLOW, 3, 40, 0, 0),

            (2, CIRCLE, BLUE, BLUE, 6, -40, 0, 60),
            (0.1, CIRCLE, BLUE, BLUE, 6, 40, 0, 60),
            (0.1, CIRCLE, RED, RED, 7, -20, 0, 60),
            (0.1, CIRCLE, RED, RED, 7, 20, 0, 60),
            (0.1, CIRCLE, WHITE, WHITE, 8, 0, 0, 60),

            (1, CIRCLELARGE, BLUE, WHITE, 16, 0, 0, 100),
            (0.1, ROCKET, WHITE, YELLOW, 3, 120, 21, 30),
            (0.1, ROCKET, WHITE, YELLOW, 3, 120, -21, 30),

            (1, CIRCLELARGE, BLUE, WHITE, 16, 0, 0, 100),
            (0.1, ROCKET, WHITE, YELLOW, 3, 120, 21, 30),
            (0.1, ROCKET, WHITE, YELLOW, 3, 120, -21, 30),

            (1, CIRCLE, WHITE, WHITE, 12, 0, 0, 80),
            (0.1, CIRCLE, WHITE, WHITE, 6, -10, 0, 90),
            (0.1, CIRCLE, WHITE, WHITE, 6, 10, 0, 90),

            (1, RING, RED, WHITE, 10, 0, 0, 80),
            (0.1, RING, BLUE, WHITE, 5, -10, 0, 90),
            (0.1, RING, BLUE, WHITE, 5, 10, 0, 90),

            (1, CIRCLE, BLUE, RED, 10, -20, -20, 80),
            (0.1, RING, WHITE, WHITE, 10, -20, -20, 80),
            (0.5, CIRCLE, BLUE, RED, 10, 20, -20, 80),
            (0.1, RING, WHITE, WHITE, 10, 20, -20, 80),
            (0.5, CIRCLE, BLUE, RED, 10, -20, 20, 80),
            (0.1, RING, WHITE, WHITE, 10, -20, 20, 80),
            (0.5, CIRCLE, BLUE, RED, 10, 20, 20, 80),
            (0.1, RING, WHITE, WHITE, 10, 20, 20, 80),

            (2, CIRCLE, WHITE, RED, 8, -10, 0, 90),
            (0.1, ROCKET, WHITE, YELLOW, 6, 120, 21, 30),
            (0.1, ROCKET, WHITE, YELLOW, 6, 120, -21, 30),
            (0.3, CIRCLE, WHITE, BLUE, 10, 0, 20, 60),
            (0.2, CIRCLE, WHITE, RED, 5, 10, 10, 80),
            (0.2, CIRCLE, WHITE, RED, 10, 0, 10, 60),
            (0.3, CIRCLE, WHITE, WHITE, 5, 10, 0, 90),
            (0.2, CIRCLE, WHITE, RED, 8, -10, 0, 90),
            (0.3, CIRCLE, WHITE, BLUE, 10, 0, -20, 80),
            (0.2, CIRCLE, WHITE, RED, 5, 10, 0, 90),
            (0.1, ROCKET, WHITE, YELLOW, 6, 120, 21, 30),
            (0.1, ROCKET, WHITE, YELLOW, 6, 120, -21, 30),

            (1, CIRCLELARGE, RED, RED, 12, 0, 0, 80),

            (1, CIRCLELARGE, WHITE, WHITE, 14, 0, 0, 90),
            (0.2, CIRCLELARGE, BLUE, BLUE, 16, 0, 0, 100)
        ),

        # Daisy Garden
        (
            (1, ROCKET, WHITE, YELLOW, 3, 1, 92, 0),
            (0.8, ROCKET, WHITE, YELLOW, 3, 1, 92, 0),
            (0.6, ROCKET, WHITE, YELLOW, 3, 1, 92, 0),
            (0.4, ROCKET, WHITE, YELLOW, 3, 1, 92, 0),

            (2, CIRCLE, WHITE, YELLOW, 5, 0, 80, 80),
            (1, CIRCLE, PURPLE, PURPLE, 4, -15, 70, 90),
            (0.5, CIRCLE, GREEN, GREEN, 6, 15, 100, 85),
            (1, CIRCLE, CYAN, CYAN, 8, 20, 90, 90),
            (0.6, CIRCLE, YELLOW, WHITE, 4, 30, 110, 90),
            (1, CIRCLE, PINK, PINK, 5, 10, 80, 80),
            (0.3, CIRCLE, YELLOW, YELLOW, 5, 0, 80, 90),
            (1, CIRCLE, WHITE, WHITE, 8, -20, 120, 85),
            (0.4, CIRCLE, PINK, YELLOW, 8, 30, 85, 90),
            (0.7, CIRCLE, YELLOW, PINK, 8, 10, 90, 100),

            (2, ROCKET, WHITE, YELLOW, 3, 10, 90, 0),
            (2, CIRCLE, YELLOW, YELLOW, 8, 10, 90, 70),
            (0.2, RING, YELLOW, YELLOW, 8, 10, 90, 70),
            (0.8, CIRCLE, YELLOW, YELLOW, 8, 10, 90, 80),
            (0.2, RING, YELLOW, YELLOW, 8, 10, 90, 80),

            (1, ROCKET, WHITE, YELLOW, 3, 10, 90, 0),
            (2, CIRCLE, GREEN, GREEN, 8, 10, 90, 70),
            (0.2, RING, GREEN, GREEN, 8, 10, 90, 70),
            (0.8, CIRCLE, GREEN, GREEN, 8, 10, 90, 80),
            (0.2, RING, GREEN, GREEN, 8, 10, 90, 80),

            (1, ROCKET, WHITE, YELLOW, 3, 10, 90, 0),
            (2, CIRCLE, PINK, PINK, 8, 10, 90, 75),
            (0.2, RING, PINK, PINK, 8, 10, 90, 75),
            (0.8, CIRCLE, PINK, PINK, 8, 10, 90, 85),
            (0.2, RING, PINK, PINK, 8, 10, 90, 85),
            (1, ROCKET, WHITE, YELLOW, 3, 20, 70, 0),
            (2, CIRCLE, WHITE, WHITE, 10, 20, 70, 60),
            (0.1, ROCKET, WHITE, YELLOW, 3, 20, 110, 0),
            (2, CIRCLE, WHITE, WHITE, 10, 20, 110, 60),
            (0.1, ROCKET, WHITE, YELLOW, 3, -20, 70, 0),
            (2, CIRCLE, WHITE, WHITE, 10, -20, 70, 60),
            (0.1, ROCKET, WHITE, YELLOW, 3, -20, 110, 0),
            (2, CIRCLE, WHITE, WHITE, 10, -20, 110, 60),

            (1.5, CIRCLE, PURPLE, PINK, 8, -30, 110, 60),
            (0.5, CIRCLE, PURPLE, PINK, 9, -15, 110, 60),
            (0.5, CIRCLE, PURPLE, PINK, 10, 0, 110, 60),
            (0.5, CIRCLE, PURPLE, PINK, 9, 15, 110, 60),
            (0.5, CIRCLE, PURPLE, PINK, 8, 30, 110, 60),

            (1.5, CIRCLE, GREEN, CYAN, 8, 30, 110, 70),
            (0.5, CIRCLE, GREEN, CYAN, 9, 15, 110, 70),
            (0.5, CIRCLE, GREEN, CYAN, 10, 0, 110, 70),
            (0.5, CIRCLE, GREEN, CYAN, 9, -15, 110, 70),
            (0.5, CIRCLE, GREEN, CYAN, 8, -30, 110, 70),

            (2, CIRCLE, WHITE, YELLOW, 6, 0, 80, 80),
            (0.5, CIRCLE, PURPLE, PURPLE, 8, -15, 70, 90),
            (0.5, CIRCLE, GREEN, GREEN, 6, 15, 100, 85),
            (1, CIRCLE, CYAN, CYAN, 8, 20, 90, 90),
            (0.5, CIRCLE, YELLOW, WHITE, 7, 30, 110, 90),
            (1, CIRCLE, PINK, PINK, 12, 10, 80, 80),
            (0.6, CIRCLELARGE, YELLOW, YELLOW, 5, 0, 80, 90),
            (1, CIRCLE, PINK, YELLOW, 8, 30, 85, 90),
            (0.5, CIRCLE, YELLOW, PINK, 12, 10, 90, 100),
            (0.4, ROCKET, WHITE, YELLOW, 3, 1, 92, 0),
            (0.5, CIRCLELARGE, WHITE, WHITE, 8, 0, 90, 60),
            (0.2, ROCKET, WHITE, YELLOW, 3, 1, 92, 0),
            (0.8, CIRCLELARGE, WHITE, WHITE, 8, 0, 90, 70),
            (0.8, CIRCLELARGE, WHITE, WHITE, 10, 0, 90, 80),
            (0.2, RING, YELLOW, YELLOW, 12, 0, 90, 80),
            (0.8, CIRCLELARGE, WHITE, WHITE, 12, 0, 90, 80),
            (0.2, RING, YELLOW, YELLOW, 12, 0, 90, 80),

            (1.5, RING, YELLOW, YELLOW, 6, 20, 110, 70),
            (0.4, RING, YELLOW, YELLOW, 6, 0, 90, 65),
            (0.4, RING, YELLOW, YELLOW, 8, -10, 100, 80),
            (0.4, RING, YELLOW, YELLOW, 8, 10, 110, 60),
            (0.2, ROCKET, WHITE, YELLOW, 3, 1, 92, 0),
            (0.4, RING, YELLOW, YELLOW, 12, -20, 90, 70),
            (0.2, ROCKET, WHITE, YELLOW, 3, 1, 92, 0),
            (0.4, CIRCLELARGE, WHITE, WHITE, 12, 0, 90, 80),

            (0.7, RING, YELLOW, YELLOW, 6, 0, 90, 65),
            (0.2, RING, YELLOW, YELLOW, 8, -10, 100, 80),
            (0.2, RING, YELLOW, YELLOW, 8, 10, 110, 60),
            (0.2, RING, YELLOW, YELLOW, 12, -20, 90, 70),

            (1, CIRCLESPRITE, WHITE, FLOWER, 24, 1, 92, 80),
        ),

        # Dreamland
        (
            (1, ROCKET, WHITE, YELLOW, 3, 63, 88, 10),
            (0, ROCKET, WHITE, YELLOW, 3, 63, -88, 10),
            (0.5, ROCKET, WHITE, YELLOW, 3, 20, 88, 10),
            (0, ROCKET, WHITE, YELLOW, 3, 20, -88, 10),
            (0.5, ROCKET, WHITE, YELLOW, 3, -22, 88, 10),
            (0, ROCKET, WHITE, YELLOW, 3, -22, -88, 10),
            (0.5, ROCKET, WHITE, YELLOW, 3, -83, 88, 10),
            (0, ROCKET, WHITE, YELLOW, 3, -83, -88, 10),

            (2, ROCKET, WHITE, YELLOW, 5, 30, 0, -20),
            (2, CIRCLE, PURPLE, PINK, 8, 30, 0, 80),
            (0.2, CIRCLE, PURPLE, PINK, 8, 10, 0, 80),
            (0.4, CIRCLE, PURPLE, PINK, 8, .5, 0, 80),
            (0.5, CIRCLE, PURPLE, PINK, 8, 30, 20, 80),
            (0.2, CIRCLE, PURPLE, PINK, 8, 30, -20, 80),
            (1, CIRCLELARGE, WHITE, WHITE, 10, 30, 0, 100),

            (2, ROCKET, WHITE, YELLOW, 5, 0, 0, -20),
            (2, CIRCLE, YELLOW, PINK, 8, 0, 0, 80),
            (0.2, CIRCLE, YELLOW, PINK, 8, -20, 0, 80),
            (0.4, CIRCLE, YELLOW, PINK, 8, 20, 0, 80),
            (0.5, CIRCLE, YELLOW, PINK, 8, 0, 20, 80),
            (0.2, CIRCLE, YELLOW, PINK, 8, 0, -20, 80),
            (1, CIRCLELARGE, WHITE, WHITE, 10, 0, 0, 100),

            (1.5, ROCKET, WHITE, YELLOW, 5, -30, 0, -20),
            (2, CIRCLE, PEACH, PINK, 8, -30, 0, 80),
            (0.2, CIRCLE, PEACH, PINK, 8, .5, 0, 80),
            (0.4, CIRCLE, PEACH, PINK, 8, 10, 0, 80),
            (0.5, CIRCLE, PEACH, PINK, 8, -30, 20, 80),
            (0.2, CIRCLE, PEACH, PINK, 8, -30, -20, 80),
            (1, CIRCLELARGE, WHITE, WHITE, 10, -30, 0, 100),

            (2, CIRCLE, PEACH, PEACH, 3, 0, 0, 80),
            (0.5, RING, YELLOW, WHITE, 3, 0, 0, 80),
            (0.1, RING, YELLOW, WHITE, 3, 0, 0, 80),

            (1, CIRCLE, PEACH, PEACH, 9, 0, 0, 100),
            (0.5, RING, YELLOW, WHITE, 9, 0, 0, 100),
            (0.1, RING, YELLOW, WHITE, 9, 0, 0, 100),

            (1, ROCKET, YELLOW, YELLOW, 5, 80, 88, 30),
            (0.1, ROCKET, YELLOW, YELLOW, 5, 80, -88, 30),
            (0.1, ROCKET, PURPLE, PURPLE, 5, 80, -66, 30),
            (0.1, ROCKET, PURPLE, PURPLE, 5, 80, 66, 30),
            (0.1, ROCKET, PINK, PINK, 5, 80, 44, 30),
            (0.1, ROCKET, PINK, PINK, 5, 80, -44, 30),
            (0.1, ROCKET, PEACH, PEACH, 5, 80, 22, 30),
            (0.1, ROCKET, PEACH, PEACH, 5, 80, -22, 30),
            (0.1, ROCKET, WHITE, WHITE, 5, 80, 0, 30),

            (2, ROCKET, YELLOW, YELLOW, 5, -80, 88, 30),
            (0.1, ROCKET, YELLOW, YELLOW, 5, -80, -88, 30),
            (0.1, ROCKET, PURPLE, PURPLE, 5, -80, -66, 30),
            (0.1, ROCKET, PURPLE, PURPLE, 5, -80, 66, 30),
            (0.1, ROCKET, PINK, PINK, 5, -80, 44, 30),
            (0.1, ROCKET, PINK, PINK, 5, -80, -44, 30),
            (0.1, ROCKET, PEACH, PEACH, 5, -80, 22, 30),
            (0.1, ROCKET, PEACH, PEACH, 5, -80, -22, 30),
            (0.1, ROCKET, WHITE, WHITE, 5, -80, 0, 30),

            (2, CIRCLE, PURPLE, PURPLE, 6, -40, 0, 100),
            (0.5, RING, YELLOW, YELLOW, 8, -40, 0, 100),

            (1, CIRCLE, BLUE, BLUE, 6, 0, 0, 100),
            (0.5, RING, YELLOW, YELLOW, 8, 0, 0, 100),
            (0.2, RING, YELLOW, YELLOW, 10, 0, 0, 100),

            (1, CIRCLE, PURPLE, PURPLE, 8, 40, 0, 100),
            (0.5, RING, YELLOW, YELLOW, 10, 40, 0, 100),
            (0.2, RING, YELLOW, YELLOW, 12, 40, 0, 100),
            (0.2, RING, YELLOW, YELLOW, 14, 40, 0, 100),

            (1, CIRCLELARGE, PURPLE, PURPLE, 8, 0, 0, 100),
            (0.5, RING, YELLOW, YELLOW, 8, 0, 0, 100),
            (0.2, RING, YELLOW, YELLOW, 8, 0, 0, 100),
            (0.2, RING, YELLOW, YELLOW, 10, 0, 0, 100),
            (0.2, RING, YELLOW, YELLOW, 12, 0, 0, 100),

            (0.1, ROCKET, WHITE, YELLOW, 4, 30, 30, -20),
            (0.2, ROCKET, WHITE, YELLOW, 4, 30, -30, -20),
            (0.2, ROCKET, WHITE, YELLOW, 6, -30, 30, -20),
            (0.2, ROCKET, WHITE, YELLOW, 8, -30, -30, -20),

            (2, CIRCLELARGE, WHITE, WHITE, 16, 20, -2, 120),
            (0.2, CIRCLE, WHITE, WHITE, 12, 20, -30, 150),
            (0.2, CIRCLE, WHITE, WHITE, 12, 20, 26, 150),

            (1, CIRCLE, WHITE, WHITE, 6, 0, 0, 100),
            (0.5, RING, YELLOW, YELLOW, 6, 0, 0, 100),
            (0.2, RING, PURPLE, PURPLE, 8, 0, 0, 100),
            (0.2, RING, PEACH, PEACH, 10, 0, 0, 100),
            (0.2, RING, PINK, PINK, 12, 0, 0, 100),

            (0.5, CIRCLELARGE, WHITE, WHITE, 8, 0, 0, 100),
            (1, CIRCLELARGE, WHITE, WHITE, 8, 0, 0, 100),
            (0.2, CIRCLESMALL, WHITE, WHITE, 4, 10, 30, 80),
            (0.3, CIRCLESMALL, WHITE, WHITE, 4, 20, -20, 90),
            (0.5, CIRCLESMALL, WHITE, WHITE, 4, -30, 0, 100),
            (0.4, CIRCLESMALL, WHITE, WHITE, 4, 15, -10, 95),
            (0.3, CIRCLESMALL, WHITE, WHITE, 4, 0, 0, 100),

            (1, ROCKET, WHITE, YELLOW, 5, 0, 0, -20),
            (2, CIRCLELARGE, WHITE, WHITE, 8, 0, 0, 100),
            (0.5, CIRCLELARGE, WHITE, WHITE, 8, 0, 0, 105),

            (0.4, ROCKET, WHITE, YELLOW, 5, 0, 0, -20),
            (0.4, ROCKET, WHITE, YELLOW, 5, 0, 0, -20),
            (2, CIRCLELARGE, WHITE, WHITE, 8, 0, 0, 100),
            (0.1, RING, RED, WHITE, 8, 0, 0, 100),
            (0.2, RING, BLUE, WHITE, 4, 10, 30, 80),
            (0.3, RING, RED, WHITE, 6, 20, -20, 90),
            (0.1, RING, BLUE, WHITE, 8, -30, 0, 100),
            (0.4, RING, RED, WHITE, 6, 15, -10, 95),
            (0.1, RING, BLUE, WHITE, 9, 0, 0, 100),
            (1, CIRCLELARGE, WHITE, WHITE, 20, 0, 0, 100),
            (0.5, CIRCLE, RED, WHITE, 20, 20, 20, 105),
            (0.2, CIRCLE, BLUE, WHITE, 20, -30, 40, 110),

            (0.5, ROCKET, WHITE, YELLOW, 5, 30, 0, -20),
            (2, CIRCLE, PURPLE, PINK, 8, 30, 0, 80),
            (0.2, CIRCLE, YELLOW, PINK, 8, 10, 0, 80),
            (0.4, CIRCLE, PINK, WHITE, 8, .5, 0, 80),
            (0.5, CIRCLE, PURPLE, PURPLE, 8, 30, 20, 80),
            (0.2, CIRCLE, BLUE, PURPLE, 8, 30, -20, 80),
            (0.5, CIRCLELARGE, WHITE, WHITE, 10, 30, 0, 100),

            (0.1, POP, WHITE, WHITE, 20, 0, 0, 90),
            (0.2, POP, WHITE, WHITE, 20, 0, 0, 90),
            (0.1, POP, WHITE, WHITE, 20, 0, 0, 90),
            (0.2, POP, WHITE, WHITE, 20, 0, 0, 90),
        ),

        # Minnies Melodyland
        (
            (3, ROCKET, WHITE, YELLOW, 5, 114, -70, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 118, -39, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 114, -20, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 118, 0, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 114, 29, -10),

            (2, ROCKET, WHITE, YELLOW, 4, 145, -35, 60),
            (0.1, ROCKET, WHITE, YELLOW, 4, 145, -30, 60),
            (0.1, ROCKET, WHITE, YELLOW, 4, 145, -20, 60),
            (0.1, ROCKET, WHITE, YELLOW, 4, 145, -10, 60),
            (0.1, ROCKET, WHITE, YELLOW, 4, 145, -5, 60),

            (1.5, CIRCLE, PINK, PINK, 14, 145, -100, 100),
            (0.5, CIRCLE, YELLOW, YELLOW, 14, 145, -60, 120),
            (0.5, CIRCLE, PINK, PINK, 14, 145, -20, 140),
            (0.5, CIRCLE, YELLOW, YELLOW, 14, 145, 20, 120),
            (0.5, CIRCLE, PINK, PINK, 14, 145, 60, 100),

            (2, ROCKET, WHITE, YELLOW, 5, 114, -70, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 118, -39, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 114, -20, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 118, 0, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 114, 29, -10),

            (2, ROCKET, WHITE, YELLOW, 4, 145, -5, 60),
            (0.1, ROCKET, WHITE, YELLOW, 4, 145, -10, 60),
            (0.1, ROCKET, WHITE, YELLOW, 4, 145, -20, 60),
            (0.1, ROCKET, WHITE, YELLOW, 4, 145, -30, 60),
            (0.1, ROCKET, WHITE, YELLOW, 4, 145, -35, 60),

            (2, CIRCLELARGE, PINK, PINK, 14, 145, -20, 120),
            (0.1, CIRCLE, PINK, PINK, 14, 145, -38, 140),
            (0.1, CIRCLE, PINK, PINK, 14, 145, -2, 140),

            (1, CIRCLE, PURPLE, PINK, 10, 120, -60, 80),
            (0.1, RING, WHITE, WHITE, 10, 120, -60, 80),
            (0.5, CIRCLE, PINK, PURPLE, 10, .5, -60, 80),
            (0.1, RING, WHITE, WHITE, 10, .5, -60, 80),
            (0.5, CIRCLE, PURPLE, YELLOW, 10, 120, 20, 80),
            (0.1, RING, WHITE, WHITE, 10, 120, 20, 80),
            (0.5, CIRCLE, YELLOW, PURPLE, 10, .5, 20, 80),
            (0.1, RING, WHITE, WHITE, 10, .5, 20, 80),

            (0.5, CIRCLE, WHITE, WHITE, 14, 145, -20, 140),
            (0.1, POP, WHITE, WHITE, 20, 0, 0, 90),
            (0.2, POP, WHITE, WHITE, 20, 0, 0, 90),

            (0.5, CIRCLE, PURPLE, PURPLE, 6, 140, -80, 80),
            (0.5, CIRCLE, YELLOW, YELLOW, 6, 140, 40, 80),
            (0.5, CIRCLE, PURPLE, PURPLE, 10, 140, -60, 100),
            (0.5, CIRCLE, YELLOW, YELLOW, 10, 140, 20, 100),
            (0.5, CIRCLE, PURPLE, PURPLE, 14, 140, -40, 120),
            (0.5, CIRCLE, YELLOW, YELLOW, 14, 140, 0, 120),
            (0.5, ROCKET, WHITE, YELLOW, 4, 145, -20, 60),

            (2, CIRCLELARGE, WHITE, WHITE, 20, 140, -20, 140),
            (2, ROCKET, WHITE, YELLOW, 5, 118, 29, -10),
            (0, ROCKET, WHITE, YELLOW, 5, 118, -70, -10),
            (2, CIRCLELARGE, WHITE, WHITE, 20, 140, -20, 140),

            (1.5, RING, PURPLE, PURPLE, 8, 140, -20, 120),
            (0.8, RING, PINK, PINK, 10, 140, -20, 120),
            (0.1, RING, PINK, PINK, 10, 140, -20, 120),
            (0.8, RING, YELLOW, YELLOW, 12, 140, -20, 120),
            (0.1, RING, YELLOW, YELLOW, 12, 140, -20, 120),

            (2, ROCKET, WHITE, YELLOW, 4, 145, -5, 60),
            (0.1, ROCKET, WHITE, YELLOW, 4, 145, -10, 60),
            (0.1, ROCKET, WHITE, YELLOW, 4, 145, -20, 60),
            (0.1, ROCKET, WHITE, YELLOW, 4, 145, -30, 60),
            (0.1, ROCKET, WHITE, YELLOW, 4, 145, -35, 60),

            (2, CIRCLELARGE, PINK, PINK, 14, 145, -20, 120),
            (0.1, CIRCLE, PINK, PINK, 14, 145, -38, 140),
            (0.1, CIRCLE, PINK, PINK, 14, 145, -2, 140),

            (2, ROCKET, WHITE, YELLOW, 5, 114, -70, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 118, -39, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 114, -20, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 118, 0, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 114, 29, -10),

            (0.5, CIRCLE, PURPLE, PURPLE, 6, 140, -80, 80),
            (0, ROCKET, WHITE, YELLOW, 5, 114, -70, -10),
            (0.1, CIRCLE, YELLOW, YELLOW, 6, 140, 40, 80),
            (0.4, ROCKET, WHITE, YELLOW, 5, 118, -39, -10),
            (0.5, CIRCLE, PURPLE, PURPLE, 10, 140, -60, 100),
            (0, ROCKET, WHITE, YELLOW, 5, 114, -20, -10),
            (0.1, CIRCLE, YELLOW, YELLOW, 10, 140, 20, 100),
            (0.4, ROCKET, WHITE, YELLOW, 5, 118, 0, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 114, 29, -10),
            (0, CIRCLE, PURPLE, PURPLE, 14, 140, -40, 120),
            (0.1, CIRCLE, YELLOW, YELLOW, 14, 140, 0, 120),
            (0.5, ROCKET, WHITE, YELLOW, 4, 145, -20, 60),
            (0.5, ROCKET, WHITE, YELLOW, 5, 114, -70, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 118, -39, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 114, -20, -10),
            (0.5, ROCKET, WHITE, YELLOW, 5, 118, 0, -10),
            (0, CIRCLELARGE, WHITE, WHITE, 20, 140, -20, 140),
            (0.5, ROCKET, WHITE, YELLOW, 5, 114, 29, -10),
            (0.4, RING, PURPLE, PURPLE, 8, 140, -20, 120),
            (0.1, ROCKET, WHITE, YELLOW, 5, 114, -70, -10),
            (0.4, RING, PINK, PINK, 10, 140, -20, 120),
            (0.1, ROCKET, WHITE, YELLOW, 5, 118, -39, -10),
            (0.1, RING, PINK, PINK, 10, 140, -20, 120),
            (0.4, ROCKET, WHITE, YELLOW, 5, 114, -20, -10),
            (0.5, RING, YELLOW, YELLOW, 12, 140, -20, 120),
            (0, ROCKET, WHITE, YELLOW, 5, 118, 0, -10),
            (0.1, RING, YELLOW, YELLOW, 12, 140, -20, 120),
            (0.4, ROCKET, WHITE, YELLOW, 5, 114, 29, -10),
            (1, CIRCLELARGE, WHITE, WHITE, 25, 140, -20, 140),

            (0.3, CIRCLE, WHITE, WHITE, 20, 140, -40, 120),
            (0.2, CIRCLE, PINK, WHITE, 22, 130, 40, 140),
            (0.4, CIRCLE, PURPLE, WHITE, 12, .5, -30, 110),
            (0.8, CIRCLE, WHITE, PINK, 20, 140, -60, 100),
            (0.5, CIRCLE, PURPLE, YELLOW, 20, .5, .5, 120),
            (0.2, CIRCLE, PURPLE, PURPLE, 16, 140, -20, 90),
            (0.4, CIRCLE, PURPLE, PEACH, 20, .5, -30, 110),
            (0.8, CIRCLE, WHITE, PINK, 16, 140, -20, 140),
            (0.5, CIRCLE, PINK, YELLOW, 22, .5, 10, 120),
            (0.2, CIRCLE, PEACH, PURPLE, 20, 140, -20, 90),
            (1, CIRCLELARGE, WHITE, WHITE, 20, 140, -20, 140),
            (0.6, CIRCLESPRITE, WHITE, MUSICNOTE, 30, 140, -20, 140),
        ),

        # The Burrrgh
        (
            (1, ROCKET, WHITE, BLUE, 3, -117, -39, 0),
            (0.5, ROCKET, WHITE, BLUE, 4, -117, -39, 0),
            (0.5, ROCKET, WHITE, BLUE, 4, -117, -39, 0),
            (0.5, ROCKET, WHITE, BLUE, 5, -117, -39, 0),

            (2, CIRCLE, WHITE, WHITE, 16, -117, -39, 100),
            (0.3, CIRCLE, WHITE, BLUE, 20, -140, -40, 70),
            (0.2, CIRCLE, BLUE, WHITE, 22, -130, 40, 70),
            (0.8, CIRCLE, WHITE, CYAN, 20, -140, -60, 80),
            (0.5, CIRCLE, CYAN, BLUE, 20, -.5, .5, 90),
            (0.2, CIRCLE, BLUE, CYAN, 16, -140, -20, 80),
            (0.8, CIRCLE, WHITE, WHITE, 16, -140, -20, 80),
            (0.5, CIRCLE, BLUE, WHITE, 22, -.5, 10, 90),
            (0.2, CIRCLE, CYAN, BLUE, 20, -140, -20, 80),

            (0, ROCKET, WHITE, BLUE, 4, -117, -39, 0),
            (0.5, ROCKET, WHITE, BLUE, 4, -117, -39, 0),
            (0.5, ROCKET, WHITE, BLUE, 4, -117, -39, 0),
            (0.5, ROCKET, WHITE, BLUE, 4, -117, -39, 0),

            (1.7, CIRCLE, WHITE, WHITE, 16, -117, -39, 100),

            (1, CIRCLE, WHITE, WHITE, 12, -147, -39, 100),
            (0.8, CIRCLE, WHITE, WHITE, 12, -87, -39, 100),
            (0.2, CIRCLE, WHITE, WHITE, 12, -107, -59, 100),
            (0.4, CIRCLE, WHITE, WHITE, 12, -127, -59, 100),
            (0.3, CIRCLE, WHITE, WHITE, 12, -107, -19, 100),
            (0.5, CIRCLE, WHITE, WHITE, 12, -127, -19, 100),

            (1.80, ROCKET, BLUE, WHITE, 4, -117, -39, 0),
            (2, CIRCLE, BLUE, WHITE, 10, -117, -39, 80),
            (0.8, CIRCLE, BLUE, WHITE, 12, -117, -39, 100),

            (0.5, CIRCLE, BLUE, WHITE, 10, -117, -39, 90),
            (0.1, RING, WHITE, WHITE, 14, -117, -39, 90),
            (0.6, CIRCLE, BLUE, WHITE, 10, -97, -59, 80),
            (0.1, RING, WHITE, WHITE, 14, -97, -59, 80),
            (0.5, CIRCLE, BLUE, WHITE, 10, -147, -9, 100),
            (0.1, RING, WHITE, WHITE, 14, -147, -9, 100),
            (0.7, CIRCLE, BLUE, WHITE, 10, -87, -39, 80),
            (0.1, RING, WHITE, WHITE, 14, -87, -39, 80),

            (2.5, ROCKET, BLUE, WHITE, 3, -137, -39, 0),
            (0.1, ROCKET, BLUE, WHITE, 4, -127, -39, 0),
            (0.1, ROCKET, BLUE, WHITE, 5, -117, -39, 0),
            (0.1, ROCKET, BLUE, WHITE, 4, -107, -39, 0),
            (0.1, ROCKET, BLUE, WHITE, 3, -97, -39, 0),

            (1.5, RING, WHITE, BLUE, 14, -117, -39, 90),
            (0.1, RING, WHITE, WHITE, 14, -117, -39, 90),
            (0.1, RING, BLUE, WHITE, 14, -117, -39, 90),

            (1.5, ROCKET, BLUE, WHITE, 3, -117, -19, 0),
            (0.1, ROCKET, BLUE, WHITE, 4, -117, -29, 0),
            (0.1, ROCKET, BLUE, WHITE, 5, -117, -39, 0),
            (0.1, ROCKET, BLUE, WHITE, 4, -117, -49, 0),
            (0.1, ROCKET, BLUE, WHITE, 3, -117, -59, 0),

            (1.5, RING, WHITE, WHITE, 14, -117, -39, 90),
            (0.1, RING, BLUE, WHITE, 14, -117, -39, 90),
            (0.1, RING, WHITE, BLUE, 14, -117, -39, 90),

            (1.5, CIRCLE, WHITE, WHITE, 20, -100, -40, 80),
            (0.1, CIRCLE, WHITE, WHITE, 20, -140, -40, 80),
            (0.1, CIRCLE, WHITE, BLUE, 10, -110, -40, 100),
            (0.1, CIRCLE, WHITE, BLUE, 10, -130, -40, 100),
            (0.1, CIRCLE, WHITE, WHITE, 8, -120, -40, 120),
            (1.5, CIRCLE, WHITE, WHITE, 20, -120, -40, 120),
            (0.2, CIRCLE, BLUE, WHITE, 22, -130, 0, 140),
            (0.4, CIRCLE, BLUE, WHITE, 12, -110, -30, 110),
            (0.8, CIRCLE, WHITE, BLUE, 20, -120, -60, 100),
            (0.5, CIRCLE, BLUE, BLUE, 20, -100, 10, 120),
            (0.2, CIRCLE, BLUE, CYAN, 16, -140, -20, 90),
            (0.5, CIRCLE, CYAN, BLUE, 22, -130, 10, 120),
            (0.2, CIRCLE, BLUE, WHITE, 20, -110, -20, 90),
            (1, CIRCLELARGE, WHITE, WHITE, 20, -120, -40, 140),

            (1, ROCKET, BLUE, WHITE, 5, -117, -59, 0),
            (0.1, ROCKET, BLUE, WHITE, 5, -117, -19, 0),

            (2, RING, WHITE, BLUE, 14, -117, -59, 80),
            (0.1, RING, WHITE, BLUE, 14, -117, -19, 80),
            (0.1, RING, WHITE, WHITE, 14, -117, -59, 80),
            (0.1, RING, BLUE, WHITE, 14, -117, -19, 80),
            (0.1, RING, WHITE, WHITE, 14, -117, -59, 80),
            (0.1, RING, BLUE, WHITE, 14, -117, -19, 80),

            (2, ROCKET, BLUE, WHITE, 4, -105, -20, 0),
            (0.2, CIRCLE, BLUE, WHITE, 22, -130, 0, 140),
            (0.8, ROCKET, BLUE, WHITE, 4, -135, -20, 0),
            (0.5, CIRCLE, WHITE, BLUE, 20, -120, -60, 100),
            (0.4, CIRCLE, BLUE, BLUE, 20, -110, -30, 110),
            (0.1, ROCKET, BLUE, WHITE, 4, -105, -60, 0),
            (0.5, CIRCLE, BLUE, BLUE, 20, -100, 10, 120),
            (0.5, ROCKET, BLUE, WHITE, 4, -135, -60, 0),
            (1, ROCKET, BLUE, WHITE, 4, -105, -20, 0),
            (0.8, CIRCLE, WHITE, BLUE, 16, -140, -20, 140),
            (0.2, ROCKET, BLUE, WHITE, 4, -135, -20, 0),
            (0.5, CIRCLE, BLUE, BLUE, 20, -100, 10, 120),
            (0.4, CIRCLE, BLUE, BLUE, 20, -100, 10, 120),
            (0.1, ROCKET, BLUE, WHITE, 4, -105, -60, 0),
            (1, ROCKET, BLUE, WHITE, 4, -135, -60, 0),
            (0.8, CIRCLE, WHITE, BLUE, 16, -140, -20, 140),
            (0.2, ROCKET, BLUE, WHITE, 4, -105, -20, 0),
            (0.7, CIRCLE, WHITE, BLUE, 16, -140, -20, 140),
            (0.3, ROCKET, BLUE, WHITE, 4, -135, -20, 0),
            (1, CIRCLELARGE, WHITE, WHITE, 20, -120, -40, 140),
            (0, ROCKET, BLUE, WHITE, 4, -105, -60, 0),
            (0.5, CIRCLE, BLUE, BLUE, 20, -100, 10, 120),
            (1, ROCKET, BLUE, WHITE, 4, -115, -35, 0),
            (0.2, ROCKET, BLUE, WHITE, 4, -120, -35, 0),
            (0.2, ROCKET, BLUE, WHITE, 4, -115, -45, 0),
            (0.2, ROCKET, BLUE, WHITE, 4, -120, -45, 0),
            (1.20, CIRCLELARGE, WHITE, WHITE, 20, -120, -40, 120),
            (1, CIRCLE, WHITE, WHITE, 20, -120, -40, 100),
            (0.8, CIRCLE, WHITE, WHITE, 20, -120, -40, 110),
            (0.8, CIRCLE, WHITE, WHITE, 20, -120, -40, 100),

            (1, CIRCLESPRITE, WHITE, SNOWFLAKE, 30, -117, -39, 110),
        ),

        # Donalds Dock
        (
            (1, ROCKET, WHITE, YELLOW, 3, -23, 3, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, -23, 3, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, -23, 3, 0),

            (1, ROCKET, WHITE, YELLOW, 3, -60, 0, 0),
            (0.2, ROCKET, WHITE, YELLOW, 3, -40, 0, 0),
            (0.2, ROCKET, WHITE, YELLOW, 3, -20, 0, 0),
            (0.2, ROCKET, WHITE, YELLOW, 3, 0, 0, 0),
            (0.2, ROCKET, WHITE, YELLOW, 3, 20, 0, 0),
            (2, CIRCLE, BLUE, GREEN, 6, -60, 0, 60),
            (0.2, CIRCLE, GREEN, BLUE, 7, -40, 0, 60),
            (0.2, CIRCLE, WHITE, WHITE, 8, -20, 0, 60),
            (0.2, CIRCLE, GREEN, GREEN, 7, 0, 0, 60),
            (0.2, CIRCLE, BLUE, BLUE, 6, 20, 0, 60),
            (1.5, CIRCLE, WHITE, WHITE, 10, 0, 0, 80),
            (0.1, CIRCLE, WHITE, WHITE, 5, -10, 0, 90),
            (0.1, CIRCLE, WHITE, WHITE, 5, 10, 0, 90),

            (1, CIRCLE, GREEN, BLUE, 10, -20, -20, 80),
            (0.1, RING, WHITE, WHITE, 10, -20, -20, 80),
            (0.5, CIRCLE, GREEN, BLUE, 10, 20, -20, 80),
            (0.1, RING, WHITE, WHITE, 10, 20, -20, 80),
            (0.5, CIRCLE, GREEN, BLUE, 10, -20, 20, 80),
            (0.1, RING, WHITE, WHITE, 10, -20, 20, 80),
            (0.5, CIRCLE, GREEN, BLUE, 10, 20, 20, 80),
            (0.1, RING, WHITE, WHITE, 10, 20, 20, 80),

            (2, ROCKET, WHITE, YELLOW, 3, -60, 0, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, -40, 0, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, -20, 0, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, 0, 0, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, 20, 0, 0),

            (1, CIRCLELARGE, BLUE, WHITE, 16, 0, 0, 100),
            (0.1, ROCKET, WHITE, YELLOW, 3, 120, 21, 30),
            (0.1, ROCKET, WHITE, YELLOW, 3, 120, -21, 30),
            (1, CIRCLELARGE, BLUE, WHITE, 16, 0, 0, 100),
            (0.1, ROCKET, WHITE, YELLOW, 3, 120, 21, 30),
            (0.1, ROCKET, WHITE, YELLOW, 3, 120, -21, 30),

            (0.1, ROCKET, WHITE, YELLOW, 3, -23, 3, 0),
            (2, CIRCLE, BLUE, BLUE, 10, -23, 3, 80),
            (0.1, ROCKET, WHITE, YELLOW, 4, -23, 3, 0),
            (2, CIRCLE, BLUE, BLUE, 14, -23, 3, 90),
            (0.1, ROCKET, WHITE, YELLOW, 5, -23, 3, 0),
            (2, CIRCLE, BLUE, BLUE, 18, -23, 3, 100),

            (1.5, ROCKET, WHITE, RED, 6, 120, 21, 30),
            (0.1, ROCKET, WHITE, RED, 6, 120, -21, 30),
            (0.3, CIRCLE, WHITE, RED, 10, 0, 20, 60),
            (0.4, CIRCLE, WHITE, RED, 5, 10, 10, 80),
            (0.2, CIRCLE, WHITE, RED, 10, 0, 10, 60),
            (0.3, CIRCLE, WHITE, RED, 5, 10, 0, 90),
            (0.2, CIRCLE, WHITE, RED, 8, -10, 0, 90),
            (0.3, CIRCLE, WHITE, RED, 10, 0, -20, 80),
            (0.2, CIRCLE, WHITE, RED, 5, 10, 0, 90),

            (2, ROCKET, WHITE, YELLOW, 6, 120, 21, 30),
            (0.1, ROCKET, WHITE, YELLOW, 6, 120, -21, 30),
            (0.2, CIRCLE, WHITE, YELLOW, 5, 10, 10, 80),
            (0.4, CIRCLE, WHITE, YELLOW, 8, -10, 0, 90),
            (0.2, CIRCLE, WHITE, YELLOW, 10, 0, 10, 60),
            (0.3, CIRCLE, WHITE, YELLOW, 5, 10, 0, 90),
            (0.4, CIRCLE, WHITE, YELLOW, 10, 0, -20, 80),
            (0.3, CIRCLE, WHITE, YELLOW, 10, 0, 20, 60),
            (0.2, CIRCLE, WHITE, YELLOW, 5, 10, 0, 110),

            (2, ROCKET, WHITE, BLUE, 6, 120, 21, 30),
            (0.1, ROCKET, WHITE, BLUE, 6, 120, -21, 30),
            (0.3, CIRCLE, WHITE, BLUE, 10, 0, 20, 60),
            (0.2, CIRCLE, WHITE, BLUE, 5, 10, 10, 80),
            (0.4, CIRCLE, WHITE, BLUE, 10, 0, 10, 60),
            (0.3, CIRCLE, WHITE, BLUE, 5, 10, 0, 90),
            (0.2, CIRCLE, WHITE, BLUE, 8, -10, 0, 90),
            (0.4, CIRCLE, WHITE, BLUE, 10, 0, -20, 80),
            (0.2, CIRCLE, WHITE, BLUE, 5, 10, 0, 90),

            (2.5, ROCKET, WHITE, YELLOW, 3, -28, 8, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, -18, 8, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, -28, -2, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, -18, -2, 0),

            (2, CIRCLE, BLUE, GREEN, 8, -60, 20, 60),
            (0.2, CIRCLE, BLUE, BLUE, 8, 20, -20, 60),
            (0.6, CIRCLE, GREEN, BLUE, 9, -40, 20, 60),
            (0.2, CIRCLE, GREEN, GREEN, 9, 0, -20, 60),
            (0.6, CIRCLE, WHITE, WHITE, 11, -20, 20, 60),
            (0.2, CIRCLE, WHITE, WHITE, 11, -20, -20, 60),
            (0.6, CIRCLE, GREEN, GREEN, 9, 0, 20, 60),
            (0.2, CIRCLE, GREEN, BLUE, 9, -40, -20, 60),
            (0.6, CIRCLE, BLUE, BLUE, 8, 20, 20, 60),
            (0.2, CIRCLE, BLUE, GREEN, 8, -60, -20, 60),

            (2, ROCKET, WHITE, YELLOW, 3, -28, 8, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, -18, 8, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, -28, -2, 0),
            (0.5, ROCKET, WHITE, YELLOW, 3, -18, -2, 0),

            (2, RING, BLUE, GREEN, 8, -60, 20, 60),
            (0.1, RING, BLUE, BLUE, 8, 20, -20, 60),
            (0.5, RING, GREEN, BLUE, 9, -40, 20, 60),
            (0.1, RING, GREEN, GREEN, 9, 0, -20, 60),
            (0.5, RING, WHITE, WHITE, 11, -20, 20, 60),
            (0.1, RING, WHITE, WHITE, 11, -20, -20, 60),
            (0.5, RING, GREEN, GREEN, 9, 0, 20, 60),
            (0.1, RING, GREEN, BLUE, 9, -40, -20, 60),
            (0.5, RING, BLUE, BLUE, 8, 20, 20, 60),
            (0.1, RING, BLUE, GREEN, 8, -60, -20, 60),

            (2, ROCKET, WHITE, YELLOW, 3, -28, 8, 0),
            (1, ROCKET, WHITE, YELLOW, 3, -18, 8, 0),
            (0.4, CIRCLE, RED, RED, 15, -30, -10, 80),
            (0.6, ROCKET, WHITE, YELLOW, 3, -28, -2, 0),
            (0.2, CIRCLE, RED, RED, 12, -10, -30, 85),
            (0.2, CIRCLE, BLUE, BLUE, 10, 20, -30, 90),
            (0.6, ROCKET, WHITE, YELLOW, 3, -18, -2, 0),
            (0.2, CIRCLE, BLUE, BLUE, 8, -20, 10, 100),
            (0.3, ROCKET, WHITE, YELLOW, 3, -28, 8, 0),
            (0.5, RING, WHITE, WHITE, 11, -20, 20, 60),
            (0, ROCKET, WHITE, YELLOW, 3, -18, 8, 0),
            (0.1, RING, WHITE, WHITE, 11, -20, -20, 60),
            (0.2, CIRCLE, BLUE, BLUE, 12, -20, 10, 90),
            (0.2, ROCKET, WHITE, YELLOW, 3, -28, -2, 0),
            (0.2, CIRCLE, BLUE, BLUE, 14, -23, 3, 80),
            (0.3, ROCKET, WHITE, YELLOW, 3, -18, -2, 0),
            (0.3, CIRCLE, RED, RED, 14, -23, 3, 90),
            (0.3, CIRCLELARGE, WHITE, WHITE, 16, -23, 3, 100),
        )
    ],

    ToontownGlobals.NEWYEARS_FIREWORKS: [
        # Toontown Central
        (
            (0.50, ROCKET, WHITE, WHITE, 5.00, 113.22, 1.05, 73.24),
            (0.25, ROCKET, RED, RED, 5.00, 115.54, 13.80, 59.11),
            (0.03, ROCKET, RED, RED, 5.00, 118.36, -13.83, 57.71),
            (0.22, ROCKET, BLUE, BLUE, 5.00, 110.05, 25.37, 57.01),
            (0.03, ROCKET, BLUE, BLUE, 5.00, 110.05, -25.37, 57.01),
            (3.22, CIRCLELARGE, WHITE, WHITE, 10.00, 121.75, 1.07, 106.69),
            (1.94, CIRCLELARGE, RED, RED, 10.00, 121.75, 1.07, 106.69),
            (1.31, ROCKET, BLUE, BLUE, 4.00, 121.75, 28.63, 38.55),
            (0.06, ROCKET, RED, RED, 4.00, 121.75, 1.30, 38.76),
            (0.06, ROCKET, WHITE, WHITE, 4.00, 121.81, -25.60, 37.54),
            (0.88, ROCKET, BLUE, BLUE, 4.00, 121.81, -25.60, 37.54),
            (0.06, ROCKET, RED, RED, 4.00, 121.74, 1.30, 37.75),
            (0.06, ROCKET, WHITE, WHITE, 4.00, 121.81, 27.34, 37.12),
            (0.82, ROCKET, BLUE, BLUE, 4.00, 55.00, 40.00, 40.00),
            (0.09, ROCKET, RED, RED, 4.00, 70.00, 40.00, 40.00),
            (0.09, ROCKET, WHITE, WHITE, 4.00, 85.00, 40.00, 40.00),
            (0.72, ROCKET, BLUE, BLUE, 4.00, 55.00, -40.00, 40.00),
            (0.09, ROCKET, RED, RED, 4.00, 70.00, -40.00, 40.00),
            (0.09, ROCKET, WHITE, WHITE, 4.00, 85.00, -40.00, 40.00),
            (0.84, CIRCLE, BLUE, BLUE, 10.00, 121.81, 29.29, 78.62),
            (0.06, RING, WHITE, WHITE, 5.00, 121.81, 29.29, 78.62),
            (0.75, CIRCLE, RED, RED, 10.00, 120.00, -30.00, 100.00),
            (0.06, RING, WHITE, WHITE, 5.00, 120.00, -30.00, 100.00),
            (0.70, CIRCLE, WHITE, WHITE, 10.00, 121.81, 29.29, 92.00),
            (0.19, RING, BLUE, BLUE, 5.00, 121.81, 29.29, 92.00),
            (0.80, CIRCLE, WHITE, WHITE, 10.00, 121.81, 0.00, 100.00),
            (0.08, RING, RED, RED, 5.00, 121.81, 0.00, 100.00),
            (1.00, ROCKET, WHITE, PEACH, 4.00, 11.43, 22.69, 4.00),
            (0.25, ROCKET, WHITE, PEACH, 4.00, 11.24, 17.57, 4.00),
            (0.25, ROCKET, WHITE, PEACH, 4.00, 10.82, 12.13, 4.00),
            (0.22, ROCKET, WHITE, PEACH, 4.00, 11.17, 6.76, 4.00),
            (0.31, ROCKET, WHITE, PEACH, 4.00, 11.10, 1.91, 4.00),
            (0.25, ROCKET, WHITE, PEACH, 4.00, 11.71, -3.56, 4.00),
            (0.19, ROCKET, WHITE, PEACH, 4.00, 11.26, -8.51, 4.00),
            (0.28, ROCKET, WHITE, PEACH, 4.00, 11.25, -14.18, 4.00),
            (0.25, ROCKET, WHITE, PEACH, 4.00, 11.20, -19.42, 4.00),
            (0.25, ROCKET, WHITE, PEACH, 4.00, 11.53, -24.46, 4.00),
            (1.24, CIRCLESMALL, RED, WHITE, 15.00, 68.68, -29.58, 57.72),
            (1.63, CIRCLE, BLUE, WHITE, 15.00, 70.33, 29.76, 56.30),
            (0.87, CIRCLELARGE, WHITE, WHITE, 15.00, 121.64, 1.20, 92.64),
            (1.26, RING, WHITE, WHITE, 15.00, 83.12, 12.21, 92.04),
            (0.44, RING, RED, RED, 15.00, 84.41, -23.72, 78.01),
            (0.44, RING, WHITE, WHITE, 15.00, 83.50, 1.77, 68.65),
            (0.38, RING, BLUE, BLUE, 15.00, 82.60, 26.64, 68.65),
            (0.37, CIRCLESMALL, WHITE, WHITE, 11.00, 74.50, 15.00, 71.80),
            (0.12, CIRCLELARGE, RED, RED, 11.00, 74.50, 15.00, 71.80),
            (0.75, CIRCLESMALL, WHITE, WHITE, 11.00, 94.03, -15.23, 62.12),
            (0.13, CIRCLELARGE, BLUE, BLUE, 11.00, 94.03, -15.23, 62.12),
            (0.56, CIRCLESMALL, RED, RED, 11.00, 54.56, 7.87, 53.74),
            (0.19, CIRCLELARGE, WHITE, WHITE, 11.00, 54.56, 7.87, 53.74),
            (0.63, CIRCLESMALL, BLUE, BLUE, 11.00, 82.51, 0.23, 82.99),
            (0.12, CIRCLELARGE, WHITE, WHITE, 11.00, 82.51, 0.23, 82.99),
            (0.37, RING, RED, RED, 5.00, 82.51, 0.23, 82.99),
            (0.47, RING, WHITE, WHITE, 6.00, 82.51, 0.23, 82.99),
            (0.47, RING, BLUE, BLUE, 7.00, 82.51, 0.23, 82.99),
            (0.47, RING, WHITE, WHITE, 8.00, 82.51, 0.23, 82.99),
            (0.47, RING, RED, RED, 10.00, 82.51, 0.23, 82.99),
            (0.37, ROCKET, WHITE, WHITE, 8.00, 53.85, 14.92, 4.00),
            (0.06, ROCKET, WHITE, WHITE, 8.00, 54.66, -16.71, 4.00),
            (0.44, ROCKET, WHITE, WHITE, 8.00, 73.27, 15.16, 4.00),
            (0.06, ROCKET, WHITE, WHITE, 8.00, 73.38, -15.98, 4.00),
            (0.44, ROCKET, WHITE, WHITE, 8.00, 93.33, 15.17, 4.00),
            (0.06, ROCKET, WHITE, WHITE, 8.00, 93.71, -15.73, 4.00),
            (0.89, CIRCLELARGE, WHITE, WHITE, 8.00, 151.88, 1.92, 144.56),
            (0.93, CIRCLESMALL, WHITE, WHITE, 8.00, 82.25, 16.72, 82.50),
            (0.12, CIRCLELARGE, WHITE, WHITE, 8.00, 79.31, 1.00, 63.69),
            (0.13, CIRCLESMALL, WHITE, WHITE, 8.00, 82.02, -13.25, 79.16),
            (0.88, ROCKET, WHITE, RED, 4.00, 6.47, -15.00, 8.60),
            (0.06, ROCKET, WHITE, RED, 4.00, 18.41, 15.00, 4.00),
            (0.31, ROCKET, WHITE, BLUE, 4.00, 53.79, 15.00, 4.00),
            (0.06, ROCKET, WHITE, BLUE, 4.00, 54.85, -15.00, 4.00),
            (0.50, ROCKET, RED, RED, 4.00, 90.45, -15.00, 4.00),
            (0.19, ROCKET, RED, RED, 4.00, 90.21, 15.00, 4.00),
            (0.19, ROCKET, BLUE, BLUE, 4.00, 90.21, 0.00, 4.00),
            (0.44, CIRCLE, WHITE, WHITE, 4.00, 18.41, 15.00, 90.00),
            (0.06, RING, RED, RED, 1.00, 18.41, 15.00, 90.00),
            (0.75, CIRCLE, WHITE, WHITE, 4.00, 93.56, -16.02, 72.89),
            (0.06, RING, RED, RED, 1.00, 93.56, -16.02, 72.89),
            (0.69, CIRCLE, WHITE, WHITE, 4.00, 53.19, -10.03, 98.97),
            (0.06, RING, BLUE, BLUE, 1.00, 53.19, -10.03, 98.97),
            (0.69, CIRCLE, WHITE, WHITE, 4.00, 71.46, 13.03, 56.82),
            (0.06, RING, BLUE, BLUE, 1.00, 71.46, 13.03, 56.82),
            (0.25, CIRCLE, RED, RED, 4.00, 89.38, -3.18, 95.18),
            (0.06, RING, WHITE, WHITE, 1.00, 89.38, -3.18, 95.18),
            (0.31, CIRCLELARGE, WHITE, WHITE, 19.00, 94.74, 0.89, 65.55),
            (0.44, ROCKET, WHITE, PEACH, 3.00, 96.50, 2.50, 4.00),
            (0.06, ROCKET, WHITE, PEACH, 3.00, 95.93, -2.61, 4.00),
            (0.38, ROCKET, WHITE, PEACH, 3.00, 76.08, 7.72, 4.00),
            (0.06, ROCKET, WHITE, PEACH, 3.00, 76.54, -8.28, 4.00),
            (0.37, ROCKET, WHITE, PEACH, 3.00, 56.41, 12.05, 4.00),
            (0.06, ROCKET, WHITE, PEACH, 3.00, 56.76, -13.51, 4.00),
            (0.31, ROCKET, WHITE, PEACH, 3.00, 36.29, 16.92, 4.00),
            (0.10, ROCKET, WHITE, PEACH, 3.00, 37.03, -19.08, 4.00),
            (0.96, CIRCLESMALL, WHITE, WHITE, 3.00, 100.31, 2.50, 66.59),
            (0.06, CIRCLESMALL, WHITE, WHITE, 3.00, 100.31, -2.50, 66.59),
            (0.44, CIRCLESMALL, WHITE, RED, 6.00, 76.25, 8.00, 66.59),
            (0.06, CIRCLESMALL, WHITE, RED, 6.00, 76.25, -8.00, 66.59),
            (0.44, CIRCLE, WHITE, BLUE, 3.00, 34.77, 12.00, 66.59),
            (0.06, CIRCLE, WHITE, BLUE, 3.00, 34.77, -12.00, 66.59),
            (0.44, CIRCLELARGE, WHITE, WHITE, 3.00, 10.00, 16.00, 66.59),
            (0.06, CIRCLELARGE, WHITE, WHITE, 3.00, 10.00, -16.00, 66.59),
            (0.94, CIRCLESPRITE, WHITE, ICECREAM, 6.00, 10.00, 0.00, 66.59),
            (2.25, ROCKET, WHITE, WHITE, 5.00, 50.00, 23.91, 19.44),
            (0.13, ROCKET, RED, RED, 5.00, 90.00, 23.91, 19.44),
            (0.44, ROCKET, WHITE, WHITE, 5.00, 50.00, -23.91, 19.44),
            (0.06, ROCKET, RED, RED, 5.00, 90.00, -23.91, 19.44),
            (0.38, ROCKET, WHITE, WHITE, 5.00, 50.00, 23.91, 19.44),
            (0.13, ROCKET, BLUE, BLUE, 5.00, 90.00, 23.91, 19.44),
            (0.25, ROCKET, WHITE, WHITE, 5.00, 50.00, -23.91, 19.44),
            (0.25, ROCKET, BLUE, BLUE, 5.00, 90.00, -23.91, 19.44),
            (0.63, ROCKET, RED, RED, 5.00, 50.00, 23.91, 19.44),
            (0.13, ROCKET, BLUE, BLUE, 5.00, 50.00, -23.91, 19.44),
            (0.25, ROCKET, BLUE, BLUE, 5.00, 90.00, 23.91, 19.44),
            (0.19, ROCKET, RED, RED, 5.00, 90.00, -23.91, 19.44),
            (0.94, ROCKET, WHITE, WHITE, 5.00, 74.23, -0.06, 4.00),
            (0.28, ROCKET, BLUE, BLUE, 5.00, 53.66, 0.14, 13.48),
            (0.28, ROCKET, RED, RED, 5.00, 53.96, -0.38, 4.00),
            (0.28, ROCKET, WHITE, WHITE, 5.00, 63.67, 10.54, 4.00),
            (0.34, ROCKET, WHITE, WHITE, 4.00, 63.88, -10.98, 4.00),
            (0.16, ROCKET, RED, RED, 5.00, 64.24, -4.44, 4.00),
            (0.16, ROCKET, RED, RED, 5.00, 64.16, 2.92, 4.00),
            (0.25, ROCKET, WHITE, WHITE, 5.00, 50.00, 23.91, 19.44),
            (0.12, ROCKET, RED, RED, 5.00, 90.00, 23.91, 19.44),
            (0.34, ROCKET, WHITE, WHITE, 5.00, 50.00, -23.91, 19.44),
            (0.03, ROCKET, RED, RED, 5.00, 90.00, -23.91, 19.44),
            (0.50, ROCKET, WHITE, WHITE, 5.00, 50.00, 23.91, 19.44),
            (0.06, ROCKET, BLUE, BLUE, 5.00, 90.00, 23.91, 19.44),
            (0.38, ROCKET, WHITE, WHITE, 5.00, 50.00, -23.91, 19.44),
            (0.06, ROCKET, BLUE, BLUE, 5.00, 90.00, -23.91, 19.44),
            (0.34, ROCKET, BLUE, BLUE, 5.00, 107.79, 19.80, 24.32),
            (0.25, ROCKET, RED, RED, 5.00, 107.58, 11.29, 45.00),
            (0.22, ROCKET, WHITE, WHITE, 5.00, 108.22, 3.33, 60.00),
            (0.37, ROCKET, WHITE, WHITE, 5.00, 108.34, -0.98, 60.00),
            (0.22, ROCKET, RED, RED, 5.00, 108.45, -9.33, 45.00),
            (0.19, ROCKET, BLUE, BLUE, 5.00, 108.69, -17.77, 24.40),
            (0.53, ROCKET, BLUE, BLUE, 5.00, 107.79, 19.80, 24.32),
            (0.25, ROCKET, RED, RED, 5.00, 107.58, 11.29, 45.00),
            (0.25, ROCKET, WHITE, WHITE, 5.00, 108.22, 3.33, 60.00),
            (0.50, ROCKET, WHITE, WHITE, 5.00, 108.34, -0.98, 60.00),
            (0.19, ROCKET, RED, RED, 5.00, 108.45, -9.33, 45.00),
            (0.19, ROCKET, BLUE, BLUE, 5.00, 108.69, -17.77, 24.40),
            (0.50, ROCKET, BLUE, BLUE, 5.00, 107.79, 19.80, 24.32),
            (0.06, ROCKET, BLUE, BLUE, 5.00, 108.69, -17.77, 24.40),
            (0.19, ROCKET, WHITE, WHITE, 5.00, 108.22, 3.33, 60.00),
            (0.06, ROCKET, WHITE, WHITE, 5.00, 108.34, -0.98, 60.00),
            (0.19, ROCKET, BLUE, BLUE, 5.00, 107.79, 19.80, 24.32),
            (0.06, ROCKET, BLUE, BLUE, 5.00, 108.69, -17.77, 24.40),
            (0.94, CIRCLELARGE, BLUE, BLUE, 5.00, 43.82, -2.09, 49.31),
            (0.25, POP, BLUE, BLUE, 5.00, 43.82, -2.09, 49.31),
            (0.25, CIRCLESMALL, BLUE, BLUE, 5.00, 43.82, -2.09, 49.31),
            (0.13, CIRCLELARGE, RED, RED, 5.00, 40.83, 10.33, 65.41),
            (0.25, CIRCLE, WHITE, WHITE, 5.00, 103.30, 12.66, 83.93),
            (0.25, RING, RED, RED, 5.00, 95.27, -9.92, 72.55),
            (0.37, POP, BLUE, BLUE, 5.00, 43.82, -2.09, 49.31),
            (0.13, CIRCLELARGE, BLUE, RED, 5.00, 107.72, -11.81, 50.51),
            (0.50, CIRCLESMALL, BLUE, WHITE, 5.00, 102.29, -8.59, 80.37),
            (0.31, RING, BLUE, BLUE, 5.00, 49.85, 12.65, 59.45),
            (0.44, RING, WHITE, WHITE, 5.00, 22.91, -0.70, 68.75),
            (0.13, CIRCLELARGE, WHITE, RED, 5.00, 91.87, 0.99, 72.32),
            (0.25, POP, BLUE, BLUE, 5.00, 43.82, -2.09, 49.31),
            (0.25, CIRCLE, RED, RED, 5.00, 2.49, 6.37, 43.93),
            (0.37, RING, BLUE, BLUE, 5.00, 84.93, 8.50, 77.25),
            (0.44, RING, WHITE, WHITE, 5.00, 85.37, -5.29, 75.30),
            (0.44, CIRCLELARGE, RED, RED, 5.00, 86.11, -11.82, 71.43),
            (0.31, CIRCLELARGE, WHITE, WHITE, 5.00, 79.35, 8.71, 77.00),
            (0.19, CIRCLELARGE, BLUE, BLUE, 5.00, 66.08, 0.98, 68.80),
        ),

        # Daisy Garden
        (
            (3, ROCKET, RED, WHITE, 1, 1.44, 92.5, -5),
            (1, ROCKET, WHITE, WHITE, 2, 1.44, 92.5, -5),
            (1, ROCKET, BLUE, WHITE, 3, 1.44, 92.5, -5),
            (2.5, CIRCLE, YELLOW, WHITE, 17, 1.44, 92.5, 70),
            (3.5, ROCKET, BLUE, WHITE, 2, 1.44, 92.5, -5),
            (1, ROCKET, WHITE, WHITE, 3, 1.44, 92.5, -5),
            (1, ROCKET, RED, WHITE, 4, 1.44, 92.5, -5),
            (2.25, CIRCLE, YELLOW, WHITE, 20, 1.44, 92.5, 75),
            (2.75, ROCKET, WHITE, WHITE, 5, 1.44, 92.5, -5),
            (2.97, RING, RED, RED, 5, 1.44, 92.5, 80),
            (0.03, RING, RED, RED, 5, 1.44, 92.5, 80),
            (0.03, RING, RED, RED, 5, 1.44, 92.5, 80),
            (0.44, RING, BLUE, BLUE, 7.5, 1.44, 92.5, 85),
            (0.03, RING, BLUE, BLUE, 7.5, 1.44, 92.5, 85),
            (0.05, RING, BLUE, BLUE, 7.5, 1.44, 92.5, 85),
            (0.39, RING, WHITE, WHITE, 5, 1.44, 92.5, 90),
            (0.03, RING, WHITE, WHITE, 5, 1.44, 92.5, 90),
            (0.03, RING, WHITE, WHITE, 5, 1.44, 92.5, 90),
            (4, POP, BLUE, BLUE, 15, 1.44, 92.5, 90),
            (1.5, CIRCLESPRITE, WHITE, FLOWER, 5, 1.44, 92.5, 30),
            (0.5, CIRCLESPRITE, RED, FLOWER, 7.5, 1.44, 92.5, .5),
            (0.63, CIRCLESPRITE, BLUE, FLOWER, 10, 1.44, 92.5, 70),
            (3.38, POP, BLUE, BLUE, 15, 1.44, 92.5, 90),
            (1, CIRCLESPRITE, YELLOW, FLOWER, 20, 1.44, 92.5, 40),
            (0.5, CIRCLESPRITE, GREEN, FLOWER, 25, 1.44, 92.5, 60),
            (0.5, CIRCLESPRITE, PINK, FLOWER, 30, 1.44, 92.5, 80),
            (3.5, CIRCLELARGE, BLUE, WHITE, 20, -4.44, 88.5, 80),
            (0.5, CIRCLELARGE, WHITE, WHITE, 20, 6.44, 92.5, 80),
            (0.5, CIRCLELARGE, RED, WHITE, 20, 6.44, 88.5, 80),
            (1.5, CIRCLESMALL, WHITE, WHITE, 30, 1.44, 92.5, 80),
            (0.5, CIRCLE, RED, RED, 40, 1.44, 92.5, 90),
            (0.5, CIRCLELARGE, BLUE, BLUE, .5, 1.44, 92.5, 100),
            (1, POP, BLUE, BLUE, 15, 1.44, 92.5, 90),
            (0.22, POP, BLUE, WHITE, 25, 1.44, 92.5, 70),
            (0.91, POP, BLUE, WHITE, 25, 1.44, 92.5, 70),
            (0.12, POP, BLUE, BLUE, 15, 1.44, 92.5, 90),
            (0.13, POP, BLUE, WHITE, 25, 1.44, 92.5, 70),
            (1.62, CIRCLESMALL, BLUE, BLUE, 20, -4.44, 88.5, 90),
            (0.5, CIRCLESMALL, RED, RED, 20, 6.44, 92.5, 90),
            (0.5, CIRCLESMALL, WHITE, WHITE, 20, 6.44, 88.5, 90),
            (2, CIRCLE, WHITE, WHITE, 40, -4.44, 88.5, 100),
            (0.5, CIRCLE, BLUE, BLUE, 40, 6.44, 92.5, 100),
            (0.38, CIRCLE, RED, RED, 40, 6.44, 88.5, 100),
            (3.88, POP, WHITE, WHITE, 20, 1.44, 92.5, 40),
            (0.25, POP, WHITE, WHITE, 30, 1.44, 92.5, 40),
            (0.25, POP, WHITE, WHITE, 40, 1.44, 92.5, 40),
            (1.69, ROCKET, BLUE, BLUE, 2, 6.44, 92.5, -1),
            (0.07, ROCKET, RED, RED, 2, 6.44, 88.5, -1),
            (0.05, ROCKET, WHITE, WHITE, 2, -4.44, 88.5, -1),
            (0.87, ROCKET, RED, RED, 4, 6.44, 88.5, -1),
            (0.07, ROCKET, WHITE, WHITE, 4, -4.44, 88.5, -1),
            (0.05, ROCKET, BLUE, BLUE, 4, 6.44, 92.5, -1),
            (0.87, ROCKET, BLUE, BLUE, 8, 6.44, 92.5, -1),
            (0.07, ROCKET, WHITE, WHITE, 8, -4.44, 88.5, -1),
            (0.05, ROCKET, RED, RED, 8, 6.44, 88.5, -1),
            (0.87, POP, RED, RED, 2, 6.44, 88.5, -1),
            (0.07, POP, RED, RED, 2, 6.44, 88.5, -1),
            (0.05, POP, RED, RED, 2, 6.44, 88.5, -1),
            (0.87, POP, RED, RED, 2, 6.44, 88.5, -1),
            (0.07, POP, RED, RED, 2, 6.44, 88.5, -1),
            (0.05, POP, RED, RED, 2, 6.44, 88.5, -1),
            (0.87, CIRCLELARGE, BLUE, BLUE, 2, 6.44, 88.5, 80),
            (0.06, CIRCLELARGE, RED, RED, 2, -4.44, 88.5, 80),
            (0.06, CIRCLELARGE, WHITE, WHITE, 2, 6.44, 92.5, 80),
            (0.44, POP, RED, WHITE, 30, 6.44, 92.5, 100),
            (0.06, POP, RED, WHITE, 30, 6.44, 92.5, 100),
            (0.06, POP, RED, WHITE, 30, 6.44, 92.5, 100),
            (0.49, CIRCLE, BLUE, WHITE, 40, 6.44, 88.5, 100),
            (0.06, CIRCLE, WHITE, WHITE, 40, -4.44, 88.5, 100),
            (0.06, CIRCLE, RED, WHITE, 40, 6.01, 91.87, 96.32),
            (0.55, POP, RED, WHITE, 30, 6.44, 92.5, 100),
            (0.04, POP, RED, WHITE, 30, 6.44, 92.5, 100),
            (0.05, POP, RED, WHITE, 30, 6.44, 92.5, 100),
            (0.41, CIRCLELARGE, BLUE, WHITE, 30, -4.44, 88.5, 120),
            (0.06, CIRCLELARGE, RED, WHITE, 30, 6.44, 92.5, 120),
            (0.06, CIRCLELARGE, WHITE, WHITE, 30, 6.44, 88.5, 120),
        ),

        # Dreamland
        (
            (1.00, ROCKET, PURPLE, PURPLE, 4.00, -120.00, -71.66, 52.06),
            (0.06, ROCKET, PURPLE, PURPLE, 4.00, -120.00, 71.17, 52.45),
            (0.81, RING, RED, RED, 4.00, -76.73, -12.67, 38.84),
            (0.75, RING, BLUE, BLUE, 4.00, -76.18, 13.97, 53.23),
            (0.50, RING, PURPLE, PURPLE, 4.00, -66.77, -1.55, 46.73),
            (0.13, RING, PINK, PINK, 4.00, -66.77, -1.55, 46.73),
            (0.12, RING, BLUE, BLUE, 4.00, -66.77, -1.55, 46.73),
            (1.13, ROCKET, RED, RED, 4.00, -62.87, -56.53, -5.17),
            (0.06, ROCKET, RED, RED, 4.00, -62.67, 56.28, -5.13),
            (0.06, ROCKET, RED, RED, 4.00, -116.10, -53.82, -1.46),
            (0.06, ROCKET, RED, RED, 4.00, -116.34, 52.84, -1.33),
            (1.44, CIRCLELARGE, PURPLE, PURPLE, 12.00, -92.38, -0.33, 55.76),
            (0.62, RING, PINK, PINK, 12.00, -92.38, -0.33, 55.76),
            (0.13, RING, RED, RED, 12.00, -92.38, -0.33, 55.76),
            (0.13, RING, BLUE, BLUE, 12.00, -92.38, -0.33, 55.76),
            (0.87, ROCKET, RED, RED, 12.00, -63.50, -56.18, -4.62),
            (0.03, ROCKET, RED, RED, 12.00, -63.50, 55.42, -3.42),
            (0.09, ROCKET, PURPLE, PURPLE, 12.00, -91.51, -56.50, -3.09),
            (0.03, ROCKET, PURPLE, PURPLE, 12.00, -91.51, 54.87, -1.89),
            (0.09, ROCKET, BLUE, BLUE, 12.00, -118.26, -55.07, -1.63),
            (0.03, ROCKET, BLUE, BLUE, 12.00, -118.26, 54.95, -0.44),
            (0.59, ROCKET, RED, RED, 12.00, -117.97, -56.18, -4.62),
            (0.03, ROCKET, RED, RED, 12.00, -115.83, 56.32, -3.41),
            (0.09, ROCKET, PURPLE, PURPLE, 12.00, -91.51, -55.17, -3.08),
            (0.03, ROCKET, PURPLE, PURPLE, 12.00, -91.51, 55.55, -1.88),
            (0.09, ROCKET, BLUE, BLUE, 12.00, -64.80, -55.07, -1.63),
            (0.03, ROCKET, BLUE, BLUE, 12.00, -64.80, 54.24, -0.45),
            (0.84, CIRCLELARGE, PURPLE, PURPLE, 12.00, -92.38, -0.33, 55.76),
            (0.13, RING, RED, RED, 5.00, -92.38, -0.33, 55.76),
            (1.50, CIRCLESMALL, RED, RED, 4.00, -134.53, -50.54, 75.30),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -35.34, 75.34),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -50.38, 70.28),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -35.49, 70.17),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -50.85, 65.71),
            (0.25, CIRCLESMALL, RED, RED, 2.00, -134.53, -45.37, 65.13),
            (0.25, CIRCLESMALL, RED, RED, 2.00, -134.53, -40.51, 65.14),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -35.65, 65.14),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -50.38, 60.39),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -35.49, 60.42),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -50.07, 55.81),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -35.34, 54.95),
            (0.50, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -20.11, 75.23),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -22.78, 70.35),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -17.60, 70.36),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -24.20, 65.02),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -16.50, 65.04),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -26.71, 60.43),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 2.00, -134.53, -22.94, 60.14),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 2.00, -134.53, -18.54, 60.15),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -13.04, 60.60),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -30.32, 55.10),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -10.37, 55.13),
            (0.50, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, -5.65, 74.82),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, -0.46, 75.43),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 4.26, 75.74),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, -5.18, 70.39),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 7.41, 70.12),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, -5.49, 65.35),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, -0.46, 65.36),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 4.42, 65.23),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.50, -5.42, 58.90),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.50, -5.13, 53.96),
            (0.50, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, 14.50, 74.87),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, 19.71, 75.33),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, 24.28, 75.34),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, 14.66, 70.58),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, 27.12, 70.46),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, 14.66, 65.25),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, 19.39, 65.25),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, 24.28, 64.82),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, 14.66, 60.21),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, 14.66, 55.47),
            (0.50, CIRCLESMALL, RED, RED, 4.00, -134.53, 29.33, 75.21),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 44.65, 74.80),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 33.28, 70.03),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 40.54, 70.19),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 37.54, 65.14),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 37.54, 59.95),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 37.22, 55.35),
            (0.50, CIRCLESMALL, RED, RED, 4.00, -134.53, -30.27, 74.94),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -15.34, 74.83),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -30.27, 70.35),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -25.71, 70.07),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -15.49, 70.09),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -30.27, 65.03),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -23.20, 65.04),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -15.65, 65.20),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -30.43, 60.44),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -17.85, 60.02),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -15.49, 60.03),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -30.27, 55.27),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -15.65, 55.58),
            (0.53, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -10.30, 75.13),
            (0.22, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -5.58, 75.00),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -0.38, 75.01),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, 4.66, 74.88),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -10.30, 70.40),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -10.14, 65.22),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -5.89, 65.22),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -0.38, 65.09),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.50, -10.26, 59.42),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.50, -10.26, 54.56),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -5.89, 55.01),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -0.54, 55.02),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, 4.35, 55.17),
            (0.50, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 9.71, 75.04),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 29.59, 75.38),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 11.44, 70.15),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 28.01, 70.19),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 12.23, 65.26),
            (0.25, CIRCLESMALL, BLUE, BLUE, 2.00, -134.53, 19.96, 65.13),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 27.07, 65.29),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 12.86, 60.22),
            (0.25, CIRCLESMALL, BLUE, BLUE, 2.00, -134.53, 16.78, 60.16),
            (0.25, CIRCLESMALL, BLUE, BLUE, 2.00, -134.53, 21.54, 60.39),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 26.12, 60.25),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 14.75, 55.63),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 24.38, 55.35),
            (0.53, CIRCLESMALL, RED, RED, 4.00, -134.53, -40.16, 75.06),
            (0.22, CIRCLESMALL, RED, RED, 4.00, -134.53, -25.40, 75.39),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.50, -35.69, 68.32),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -29.33, 70.21),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -32.63, 65.17),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -32.78, 60.44),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -32.78, 55.41),
            (0.50, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -20.37, 74.96),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -15.49, 74.83),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -10.30, 74.99),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -5.74, 74.85),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -20.53, 70.08),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -20.21, 65.20),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -15.65, 64.91),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -10.14, 65.07),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -20.05, 60.02),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -20.21, 55.43),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -15.02, 55.14),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -10.62, 55.15),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -5.74, 55.30),
            (0.50, CIRCLESMALL, BLUE, BLUE, 4.00, -134.50, 8.72, 73.77),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 6.24, 70.14),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 13.02, 70.30),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 4.35, 65.39),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 14.28, 65.12),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.50, 1.92, 60.18),
            (0.25, CIRCLESMALL, BLUE, BLUE, 2.00, -134.53, 7.90, 60.22),
            (0.25, CIRCLESMALL, BLUE, BLUE, 2.00, -134.53, 11.91, 60.22),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 16.17, 60.23),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.50, -0.85, 54.23),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 19.49, 55.34),
            (0.50, CIRCLESMALL, RED, RED, 4.00, -134.53, 24.70, 75.22),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 29.28, 75.23),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 34.97, 74.65),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 24.86, 69.88),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 37.34, 70.06),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 24.70, 65.29),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 29.75, 64.85),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 34.49, 65.16),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 24.54, 59.80),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 37.66, 60.12),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 24.54, 55.20),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 40.82, 54.63),
            (0.50, CIRCLESMALL, RED, RED, 4.00, -134.53, -40.47, 75.06),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -35.45, 75.07),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -45.49, 70.47),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -30.58, 70.50),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -34.67, 65.17),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -40.47, 62.05),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -45.65, 59.53),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -45.65, 55.39),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -40.47, 55.55),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -35.92, 55.26),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, -30.58, 55.27),
            (0.50, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -15.49, 75.12),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -10.62, 74.99),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -20.68, 70.37),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -4.95, 70.26),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -20.37, 65.20),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -5.74, 65.08),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -20.21, 60.02),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -5.42, 60.19),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -15.49, 55.14),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 4.00, -134.53, -10.46, 55.15),
            (0.50, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 9.39, 75.18),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 14.60, 75.20),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 4.66, 69.99),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 18.70, 70.31),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 4.35, 65.24),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 19.64, 65.28),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 5.45, 60.21),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 18.54, 60.08),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 9.39, 55.03),
            (0.25, CIRCLESMALL, BLUE, BLUE, 4.00, -134.53, 14.60, 55.04),
            (0.53, CIRCLESMALL, RED, RED, 4.00, -134.53, 29.75, 75.23),
            (0.22, CIRCLESMALL, RED, RED, 4.00, -134.53, 42.56, 74.97),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 29.44, 70.04),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 42.40, 70.22),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 29.59, 65.15),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 33.07, 65.15),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 38.29, 65.02),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 42.08, 65.17),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 42.24, 60.57),
            (0.25, CIRCLESMALL, RED, RED, 4.00, -134.53, 42.08, 55.23),
            (0.28, ROCKET, RED, RED, 1.00, -134.53, 51.93, 55.34),
            (0.75, CIRCLELARGE, RED, RED, 5.00, -90.69, -19.74, 38.96),
            (0.22, CIRCLESMALL, PURPLE, PURPLE, 5.00, -89.41, 12.93, 57.47),
            (0.25, RING, BLUE, BLUE, 5.00, -89.41, -14.28, 51.82),
            (0.25, CIRCLESMALL, PINK, PINK, 5.00, -89.41, 17.67, 27.95),
            (0.25, CIRCLESMALL, WHITE, WHITE, 5.00, -89.41, -15.05, 31.01),
            (0.25, CIRCLELARGE, BLUE, RED, 5.00, -89.41, -16.86, 59.20),
            (0.25, RING, RED, PURPLE, 5.00, -89.41, 9.76, 46.80),
            (0.25, CIRCLESMALL, PURPLE, PURPLE, 5.00, -89.41, 12.64, 30.14),
            (0.25, CIRCLELARGE, BLUE, BLUE, 5.00, -89.41, -16.20, 36.45),
            (0.38, CIRCLESMALL, PURPLE, PURPLE, 5.00, -89.41, -3.85, 61.98),
            (0.37, RING, RED, RED, 5.00, -89.41, 12.96, 34.61),
            (0.37, CIRCLELARGE, PURPLE, PURPLE, 5.00, -89.41, 13.46, 66.24),
            (0.25, CIRCLESMALL, BLUE, RED, 5.00, -89.41, -5.28, 37.68),
            (0.25, RING, RED, RED, 5.00, -89.41, -0.94, 44.71),
            (0.06, RING, PURPLE, PURPLE, 5.00, -89.41, -0.94, 44.71),
            (0.06, RING, BLUE, BLUE, 5.00, -89.41, -0.94, 44.71),
        ),

        # Minnies Melodyland
        (
            (0.56, CIRCLELARGE, WHITE, PEACH, 10.00, 137.92, -20.14, 107.40),
            (0.94, CIRCLE, PEACH, PEACH, 10.00, 137.92, 63.27, 50.69),
            (0.06, CIRCLE, PEACH, PEACH, 10.00, 137.92, -101.42, 50.69),
            (0.69, CIRCLE, YELLOW, YELLOW, 10.00, 137.92, 30.99, 73.30),
            (0.06, CIRCLE, YELLOW, YELLOW, 10.00, 137.92, -72.63, 73.30),
            (0.69, ROCKET, PINK, PINK, 3.00, 137.92, 5.88, 75.31),
            (0.12, ROCKET, PINK, PINK, 3.00, 137.92, -45.83, 75.31),
            (0.13, ROCKET, PURPLE, PURPLE, 5.00, 137.92, -19.45, 75.31),
            (1.75, CIRCLELARGE, WHITE, PURPLE, 15.00, 137.92, -19.45, 170.91),
            (1.00, CIRCLE, PINK, PINK, 15.00, 137.92, 27.97, 118.05),
            (0.12, RING, WHITE, WHITE, 15.00, 137.92, 27.97, 118.05),
            (0.62, CIRCLE, PURPLE, PURPLE, 15.00, 137.92, -72.79, 118.05),
            (0.13, RING, WHITE, WHITE, 15.00, 137.92, -72.79, 118.05),
            (0.75, ROCKET, YELLOW, YELLOW, 5.00, 132.97, 36.51, -10.35),
            (0.09, ROCKET, YELLOW, YELLOW, 5.00, 132.97, 20.55, -3.80),
            (0.09, ROCKET, YELLOW, YELLOW, 5.00, 132.97, 5.97, 1.14),
            (0.09, ROCKET, YELLOW, YELLOW, 5.00, 132.97, -9.70, 5.16),
            (0.59, ROCKET, PEACH, PEACH, 5.00, 132.97, -77.37, -10.50),
            (0.13, ROCKET, PEACH, PEACH, 5.00, 132.97, -60.43, -3.31),
            (0.13, ROCKET, PEACH, PEACH, 5.00, 132.97, -47.12, 1.14),
            (0.12, ROCKET, PEACH, PEACH, 5.00, 132.97, -30.65, 5.16),
            (0.62, ROCKET, PINK, PINK, 5.00, 132.97, 36.51, -10.35),
            (0.13, ROCKET, PINK, PINK, 5.00, 132.97, 20.55, -3.80),
            (0.13, ROCKET, PINK, PINK, 5.00, 132.97, 5.97, 1.14),
            (0.12, ROCKET, PINK, PINK, 5.00, 132.97, -9.70, 5.16),
            (0.50, ROCKET, PURPLE, PURPLE, 5.00, 132.97, -77.37, -10.50),
            (0.13, ROCKET, PURPLE, PURPLE, 5.00, 132.97, -60.43, -3.31),
            (0.12, ROCKET, PURPLE, PURPLE, 5.00, 132.97, -47.12, 1.14),
            (0.13, ROCKET, PURPLE, PURPLE, 5.00, 132.97, -30.65, 5.16),
            (0.75, CIRCLELARGE, YELLOW, YELLOW, 15.00, 110.03, 29.40, 21.16),
            (0.75, CIRCLELARGE, PEACH, PEACH, 15.00, 110.03, -68.21, 21.16),
            (0.75, CIRCLELARGE, PINK, PINK, 15.00, 110.03, 0.88, 47.21),
            (0.75, CIRCLELARGE, PURPLE, PURPLE, 15.00, 110.03, -58.67, 68.78),
            (0.75, CIRCLESMALL, WHITE, YELLOW, 15.00, 110.03, -50.66, 48.46),
            (0.31, CIRCLESMALL, WHITE, PINK, 15.00, 110.03, 13.95, 48.97),
            (0.25, CIRCLELARGE, PURPLE, PURPLE, 15.00, 110.03, -17.82, 72.34),
            (0.06, RING, WHITE, WHITE, 15.00, 110.03, -17.82, 72.34),
            (0.31, CIRCLELARGE, PEACH, PEACH, 15.00, 110.03, -17.82, 72.34),
            (0.06, RING, WHITE, WHITE, 15.00, 110.03, -17.82, 72.34),
            (0.38, POP, WHITE, WHITE, 15.00, 110.03, -17.82, 72.34),
            (2.62, ROCKET, PEACH, WHITE, 3.00, 112.26, 15.89, -4.52),
            (0.03, ROCKET, PEACH, WHITE, 3.00, 112.26, -54.60, -4.52),
            (0.28, ROCKET, PEACH, WHITE, 3.00, 101.59, 20.65, -4.71),
            (0.03, ROCKET, PEACH, WHITE, 3.00, 103.60, -57.91, -4.52),
            (0.31, ROCKET, PEACH, WHITE, 3.00, 99.07, 31.56, -4.52),
            (0.03, ROCKET, PEACH, WHITE, 3.00, 98.42, -68.05, -4.52),
            (0.31, ROCKET, PEACH, WHITE, 3.00, 102.69, -78.04, -4.52),
            (0.03, ROCKET, PEACH, WHITE, 3.00, 103.51, 42.25, -4.52),
            (0.34, ROCKET, PEACH, WHITE, 3.00, 114.48, 45.43, -4.52),
            (0.03, ROCKET, PEACH, WHITE, 3.00, 112.58, -82.93, -4.52),
            (0.28, ROCKET, PEACH, WHITE, 3.00, 123.92, 40.62, -4.52),
            (0.03, ROCKET, PEACH, WHITE, 3.00, 122.92, -79.72, -4.52),
            (0.28, ROCKET, PEACH, WHITE, 3.00, 128.00, 30.05, -4.52),
            (0.03, ROCKET, PEACH, WHITE, 3.00, 128.24, -69.29, -4.52),
            (0.34, ROCKET, PEACH, WHITE, 3.00, 128.00, 14.58, -0.18),
            (0.03, ROCKET, PEACH, WHITE, 3.00, 128.00, -55.60, -0.18),
            (0.28, ROCKET, PEACH, WHITE, 3.00, 128.00, 1.12, 4.79),
            (0.03, ROCKET, PEACH, WHITE, 3.00, 128.00, -41.73, 4.79),
            (0.28, ROCKET, PEACH, WHITE, 3.00, 128.00, -10.37, 7.53),
            (0.06, ROCKET, PEACH, WHITE, 3.00, 128.00, -29.31, 7.53),
            (0.19, ROCKET, PEACH, WHITE, 3.00, 128.00, -20.23, 7.53),
            (2.12, RING, PINK, PINK, 5.00, 128.00, -19.26, 65.26),
            (0.13, CIRCLELARGE, PURPLE, PURPLE, 5.00, 128.00, -19.26, 65.26),
            (2.00, ROCKET, WHITE, WHITE, 3.00, 128.74, -76.99, -10.35),
            (0.25, ROCKET, YELLOW, YELLOW, 3.00, 128.74, -48.58, -0.30),
            (0.25, ROCKET, PEACH, PEACH, 3.00, 128.74, -19.91, 5.62),
            (0.25, ROCKET, PINK, PINK, 3.00, 128.74, 7.82, 0.08),
            (0.25, ROCKET, PURPLE, PURPLE, 3.00, 128.74, 36.06, -9.94),
            (0.25, ROCKET, PINK, PINK, 3.00, 128.74, 7.97, 0.13),
            (0.25, ROCKET, PEACH, PEACH, 3.00, 128.74, -20.22, 5.66),
            (0.25, ROCKET, YELLOW, YELLOW, 3.00, 128.74, -49.59, -0.26),
            (0.25, ROCKET, WHITE, WHITE, 3.00, 128.74, -77.29, -10.44),
            (0.75, CIRCLE, WHITE, PINK, 8.00, 128.74, 49.33, 27.06),
            (0.25, CIRCLE, WHITE, YELLOW, 10.00, 128.74, 24.30, 59.18),
            (0.25, CIRCLE, WHITE, PEACH, 12.00, 128.74, -20.59, 86.54),
            (0.25, CIRCLE, WHITE, PURPLE, 10.00, 128.74, -63.30, 62.82),
            (0.25, CIRCLE, WHITE, RED, 8.00, 128.74, -85.90, 28.25),
            (1.19, RING, PINK, PINK, 4.00, 78.66, -50.27, 65.42),
            (0.50, CIRCLESMALL, PURPLE, PURPLE, 12.00, 119.63, -34.17, 43.49),
            (0.25, CIRCLESMALL, YELLOW, YELLOW, 12.00, 78.80, 0.32, 44.50),
            (0.31, CIRCLELARGE, WHITE, WHITE, 12.00, 81.00, -13.05, 72.06),
            (0.06, RING, PEACH, PEACH, 12.00, 81.00, -13.05, 72.06),
            (2.44, ROCKET, WHITE, WHITE, 4.00, 139.06, 4.93, 66.62),
            (0.06, ROCKET, WHITE, WHITE, 4.00, 139.06, -45.46, 66.08),
            (0.44, ROCKET, YELLOW, YELLOW, 4.00, 139.06, -78.11, 35.09),
            (0.06, ROCKET, YELLOW, YELLOW, 4.00, 139.06, -97.43, 22.07),
            (0.44, ROCKET, PEACH, PEACH, 4.00, 139.06, 57.01, 22.06),
            (0.06, ROCKET, PEACH, PEACH, 4.00, 139.06, 37.16, 34.56),
            (0.44, ROCKET, PINK, PINK, 4.00, 139.06, -83.11, 43.43),
            (0.06, ROCKET, PINK, PINK, 4.00, 139.06, -46.63, 55.47),
            (0.44, ROCKET, PURPLE, PURPLE, 4.00, 139.06, 41.59, 44.45),
            (0.06, ROCKET, PURPLE, PURPLE, 4.00, 139.06, 5.84, 55.90),
            (1.44, RING, PINK, PINK, 2.00, 139.06, 58.76, 48.85),
            (0.06, RING, PINK, PINK, 2.00, 139.06, -100.96, 47.13),
            (0.38, RING, PURPLE, PURPLE, 2.00, 139.06, 30.48, 72.08),
            (0.06, RING, PURPLE, PURPLE, 2.00, 139.06, -68.17, 72.65),
            (0.44, CIRCLELARGE, RED, WHITE, 2.00, 136.43, -9.32, 91.88),
            (0.37, CIRCLELARGE, WHITE, WHITE, 2.00, 139.06, -24.09, 110.54),
            (0.06, RING, PURPLE, PURPLE, 2.00, 139.06, -24.09, 110.54),
            (0.50, ROCKET, WHITE, PINK, 3.00, 140.86, -3.39, 66.10),
            (0.06, ROCKET, WHITE, PINK, 3.00, 140.86, -34.91, 65.76),
            (0.31, ROCKET, WHITE, PEACH, 3.00, 140.86, 8.90, 54.37),
            (0.06, ROCKET, WHITE, PEACH, 3.00, 140.86, -49.88, 53.74),
            (0.31, ROCKET, WHITE, PURPLE, 3.00, 140.86, 31.63, 47.78),
            (0.06, ROCKET, WHITE, PURPLE, 3.00, 140.86, -74.65, 46.63),
            (0.41, ROCKET, WHITE, RED, 3.00, 140.86, 57.27, 21.24),
            (0.09, ROCKET, WHITE, RED, 3.00, 140.86, -98.14, 19.57),
            (0.91, ROCKET, PINK, PINK, 3.00, 140.86, 41.17, 44.63),
            (0.03, ROCKET, PINK, PINK, 3.00, 140.86, -80.26, 43.33),
            (0.22, ROCKET, PURPLE, PURPLE, 3.00, 140.86, 12.12, 62.48),
            (0.03, ROCKET, PURPLE, PURPLE, 3.00, 140.86, -54.27, 61.76),
            (0.16, ROCKET, RED, RED, 3.00, 140.86, -13.79, 75.93),
            (0.03, ROCKET, RED, RED, 3.00, 140.86, -23.17, 75.83),
            (0.56, RING, YELLOW, YELLOW, 3.00, 120.63, -19.19, 77.13),
            (0.50, RING, PEACH, PEACH, 3.00, 120.63, -19.19, 77.13),
            (0.38, CIRCLESMALL, PURPLE, PURPLE, 8.00, 85.06, -0.67, 38.82),
            (0.12, CIRCLESMALL, PINK, PINK, 9.00, 85.06, -23.72, 49.29),
            (0.13, CIRCLESMALL, PEACH, PEACH, 10.00, 85.06, 8.51, 62.30),
            (0.25, CIRCLELARGE, WHITE, PINK, 15.00, 86.04, -16.85, 58.76),
            (0.06, RING, PURPLE, WHITE, 5.00, 86.04, -16.85, 58.76),
            (0.69, CIRCLELARGE, WHITE, WHITE, 5.00, 82.52, -32.63, 42.45),
            (0.25, CIRCLELARGE, PURPLE, PURPLE, 10.00, 98.02, -4.11, 58.76),
            (0.50, CIRCLELARGE, PINK, PINK, 8.00, 107.66, -45.36, 67.65),
            (0.50, CIRCLELARGE, PEACH, PEACH, 12.00, 101.02, -11.32, 35.33),
            (0.38, CIRCLELARGE, YELLOW, YELLOW, 14.00, 84.21, -9.10, 68.81),
            (0.31, CIRCLELARGE, RED, RED, 8.00, 86.04, -37.69, 42.21),
            (0.50, RING, PURPLE, PINK, 4.00, 97.11, -17.22, 58.76),
            (0.02, RING, PINK, PEACH, 4.00, 97.11, -17.22, 58.76),
            (0.02, RING, PEACH, YELLOW, 4.00, 97.11, -17.22, 58.76),
            (1.03, ROCKET, YELLOW, YELLOW, 4.00, 139.70, 53.94, 24.67),
            (0.06, ROCKET, YELLOW, YELLOW, 4.00, 139.70, -94.94, 23.07),
            (0.19, ROCKET, PEACH, PEACH, 4.00, 139.70, 27.59, 49.73),
            (0.06, ROCKET, PEACH, PEACH, 4.00, 139.70, -70.33, 48.68),
            (0.19, ROCKET, PINK, PINK, 4.00, 139.70, 4.74, 66.45),
            (0.09, ROCKET, PINK, PINK, 4.00, 139.70, -45.20, 65.92),
            (0.59, ROCKET, YELLOW, YELLOW, 4.00, 139.70, 53.94, 24.67),
            (0.03, ROCKET, YELLOW, YELLOW, 4.00, 139.70, -94.94, 23.07),
            (0.09, ROCKET, PEACH, PEACH, 4.00, 139.70, 27.59, 49.73),
            (0.03, ROCKET, PEACH, PEACH, 4.00, 139.70, -70.33, 48.68),
            (0.09, ROCKET, PINK, PINK, 4.00, 139.70, 4.74, 66.45),
            (0.03, ROCKET, PINK, PINK, 4.00, 139.70, -45.20, 65.92),
            (0.47, CIRCLELARGE, PURPLE, PINK, 5.00, 82.52, -32.63, 42.45),
            (0.31, CIRCLELARGE, PINK, PEACH, 10.00, 98.02, -4.11, 58.76),
            (0.31, CIRCLELARGE, PEACH, YELLOW, 8.00, 107.66, -45.36, 67.65),
            (0.44, CIRCLELARGE, YELLOW, WHITE, 12.00, 101.02, -11.32, 35.33),
            (0.69, ROCKET, YELLOW, YELLOW, 4.00, 106.90, 41.71, -4.52),
            (0.25, ROCKET, YELLOW, YELLOW, 4.00, 127.41, 29.95, -4.52),
            (0.25, ROCKET, YELLOW, YELLOW, 4.00, 112.57, 16.35, -4.52),
            (0.31, ROCKET, PEACH, PEACH, 4.00, 112.01, -82.53, -4.52),
            (0.31, ROCKET, PEACH, PEACH, 4.00, 127.64, -69.67, -4.52),
            (0.25, ROCKET, PEACH, PEACH, 4.00, 113.58, -54.24, -4.52),
            (0.37, ROCKET, PINK, PINK, 4.00, 113.77, 44.25, -4.52),
            (0.25, ROCKET, PINK, PINK, 4.00, 127.64, 30.10, -4.52),
            (0.25, ROCKET, PINK, PINK, 4.00, 112.21, 16.69, -4.52),
            (0.31, ROCKET, WHITE, WHITE, 4.00, 112.99, -81.98, -4.52),
            (0.25, ROCKET, WHITE, WHITE, 4.00, 127.44, -69.67, -4.52),
            (0.25, ROCKET, WHITE, WHITE, 4.00, 113.97, -54.42, -4.52),
            (0.25, ROCKET, YELLOW, YELLOW, 4.00, 113.97, 44.25, -4.52),
            (0.06, ROCKET, YELLOW, YELLOW, 4.00, 112.40, 16.14, -4.52),
            (0.19, ROCKET, PEACH, PEACH, 4.00, 113.77, -54.24, -4.52),
            (0.06, ROCKET, PEACH, PEACH, 4.00, 112.40, -81.98, -4.52),
            (0.19, ROCKET, PINK, PINK, 4.00, 115.09, -10.10, 0.79),
            (0.06, ROCKET, PINK, PINK, 4.00, 115.66, -29.69, 0.79),
            (0.69, CIRCLELARGE, PURPLE, PURPLE, 10.00, 112.99, -21.41, 73.40),
            (0.25, CIRCLESMALL, PINK, PINK, 10.00, 82.59, -7.83, 49.23),
            (0.12, CIRCLESMALL, PINK, PINK, 10.00, 106.28, -39.22, 60.32),
            (0.13, CIRCLESMALL, WHITE, WHITE, 10.00, 106.28, -18.80, 69.23),
            (0.25, CIRCLELARGE, RED, RED, 10.00, 106.28, -5.25, 43.69),
            (0.25, CIRCLESMALL, PINK, PINK, 10.00, 107.33, -21.69, 78.98),
            (0.12, CIRCLESMALL, PINK, PINK, 10.00, 111.92, -52.95, 64.92),
            (0.13, CIRCLESMALL, WHITE, WHITE, 10.00, 109.82, 14.35, 79.55),
            (0.25, CIRCLELARGE, YELLOW, YELLOW, 10.00, 75.62, -42.59, 39.25),
            (0.25, CIRCLESMALL, PEACH, PEACH, 10.00, 92.41, -1.70, 30.90),
            (0.12, CIRCLESMALL, PINK, PINK, 10.00, 71.90, -0.06, 50.32),
            (0.13, CIRCLESMALL, RED, RED, 10.00, 100.33, -38.07, 49.92),
            (0.25, CIRCLELARGE, RED, WHITE, 10.00, 125.29, -21.70, 85.61),
            (0.25, RING, YELLOW, YELLOW, 4.00, 125.29, -21.70, 85.61),
            (0.13, RING, PEACH, PEACH, 4.00, 125.29, -21.70, 85.61),
            (0.12, RING, PINK, PINK, 4.00, 125.29, -21.70, 85.61),
            (0.25, CIRCLELARGE, PEACH, PEACH, 4.00, 86.78, -32.61, 78.74),
            (0.25, CIRCLESMALL, PINK, PINK, 4.00, 85.81, 6.87, 65.98),
            (0.13, RING, YELLOW, YELLOW, 4.00, 97.06, -16.05, 94.59),
            (0.12, CIRCLESMALL, RED, RED, 4.00, 76.01, -46.69, 61.22),
            (0.31, CIRCLELARGE, WHITE, PINK, 4.00, 56.79, 4.47, 27.11),
            (0.31, RING, RED, RED, 4.00, 113.67, -19.24, 78.88),
            (0.06, CIRCLESMALL, PINK, PINK, 4.00, 86.78, -11.48, 84.63),
            (0.06, RING, PURPLE, PURPLE, 4.00, 76.66, -54.89, 50.20),
            (0.50, CIRCLELARGE, PURPLE, WHITE, 4.00, 94.84, -38.08, 63.24),
            (0.25, CIRCLESMALL, PEACH, WHITE, 4.00, 109.52, -1.16, 63.64),
            (0.13, CIRCLESMALL, PINK, WHITE, 4.00, 76.28, -37.94, 50.25),
            (0.12, CIRCLESMALL, YELLOW, WHITE, 4.00, 71.61, 1.57, 41.52),
            (0.69, RING, YELLOW, YELLOW, 4.00, 141.96, -20.09, 92.36),
            (0.03, RING, PEACH, PEACH, 4.00, 141.96, -20.09, 92.36),
            (0.03, RING, RED, RED, 4.00, 141.96, -20.09, 92.36),
        ),

        # The Burrrgh
        (
            (4, POP, PURPLE, WHITE, 20, -107.67, -39.76, 9),
            (1.5, CIRCLESPRITE, PURPLE, SNOWFLAKE, 20, -107.67, -39.76, 30),
            (2.25, POP, PURPLE, WHITE, 20, -107.67, -39.76, 9),
            (1.5, CIRCLESPRITE, CYAN, SNOWFLAKE, 20, -107.67, -39.76, 60),
            (2.75, POP, CYAN, WHITE, 20, -107.67, -39.76, 60),
            (1.5, CIRCLESPRITE, BLUE, SNOWFLAKE, 20, -107.67, -39.76, 60),
            (2.5, POP, BLUE, WHITE, 20, -107.67, -39.76, 60),
            (1.5, CIRCLESPRITE, WHITE, SNOWFLAKE, 20, -107.67, -39.76, 80),
            (4.75, POP, WHITE, WHITE, 20, -107.67, -39.76, 80),
            (0.5, POP, WHITE, WHITE, 20, -107.67, -39.76, 80),
            (0.5, POP, WHITE, WHITE, 20, -107.67, -39.76, 80),
            (1.25, CIRCLESPRITE, WHITE, SNOWFLAKE, 30, -107.67, -39.76, 90),
            (0.5, CIRCLESPRITE, PURPLE, SNOWFLAKE, 35, -107.67, -39.76, 90),
            (0.5, CIRCLESPRITE, CYAN, SNOWFLAKE, 40, -107.67, -39.76, 90),
            (3.75, POP, CYAN, WHITE, 60, -107.67, -39.76, 90),
            (0.25, POP, CYAN, WHITE, 60, -107.67, -39.76, 90),
            (0.25, POP, CYAN, WHITE, 60, -107.67, -39.76, 90),
            (0.25, POP, CYAN, WHITE, 60, -107.67, -39.76, 90),
            (1.25, CIRCLESPRITE, WHITE, SNOWFLAKE, .5, -107.67, -59.76, 90),
            (0.25, CIRCLESPRITE, BLUE, SNOWFLAKE, .5, -87.67, -39.76, 90),
            (0.25, CIRCLESPRITE, PURPLE, SNOWFLAKE, .5, -107.67, -19.76, 90),
            (0.25, CIRCLESPRITE, CYAN, SNOWFLAKE, .5, -127.67, -39.76, 90),
            (6, POP, CYAN, WHITE, 40, -107.67, -39.76, 90),
            (1, ROCKET, CYAN, WHITE, 5, -107.67, -39.76, 10),
            (0.5, CIRCLE, PURPLE, WHITE, 20, -107.67, -39.76, 10),
            (0.5, CIRCLESPRITE, WHITE, SNOWFLAKE, 49, -107.67, -39.76, 110),
            (3, POP, WHITE, WHITE, 49, -107.67, -39.76, 110),
            (0.25, POP, WHITE, WHITE, 49, -107.67, -39.76, 110),
            (1, ROCKET, CYAN, WHITE, 5, -107.67, -39.76, 10),
            (0.25, ROCKET, PURPLE, WHITE, 5, -107.67, -39.76, 10),
            (0.25, CIRCLE, PURPLE, WHITE, 20, -107.67, -39.76, 10),
            (0.25, CIRCLE, CYAN, WHITE, 20, -107.67, -39.76, 10),
            (0.25, CIRCLESPRITE, WHITE, SNOWFLAKE, 49, -107.67, -39.76, 110),
            (0.25, CIRCLESPRITE, BLUE, SNOWFLAKE, 49, -107.67, -39.76, 110),
            (2.5, POP, CYAN, WHITE, 5, -107.67, -39.76, 10),
            (0.25, POP, CYAN, WHITE, 5, -107.67, -39.76, 10),
            (0.25, POP, CYAN, WHITE, 5, -107.67, -39.76, 10),
            (0.5, ROCKET, BLUE, WHITE, 5, -107.67, -39.76, 10),
            (0.25, ROCKET, PURPLE, WHITE, 5, -107.67, -39.76, 10),
            (0.25, ROCKET, CYAN, WHITE, 5, -107.67, -39.76, 10),
            (0.5, CIRCLESPRITE, BLUE, SNOWFLAKE, 49, -107.67, -39.76, 110),
            (0.25, CIRCLESPRITE, PURPLE, SNOWFLAKE, 49, -107.67, -39.76, 110),
            (0.25, CIRCLESPRITE, CYAN, SNOWFLAKE, 49, -107.67, -39.76, 110),
            (6.5, POP, CYAN, WHITE, 5, -107.67, -39.76, 10),
            (0.25, POP, CYAN, WHITE, 5, -107.67, -39.76, 10),
            (0.25, POP, CYAN, WHITE, 5, -107.67, -39.76, 10),
            (0.25, POP, CYAN, WHITE, 5, -107.67, -39.76, 10),
            (0.5, POP, CYAN, WHITE, 40, -107.67, -59.76, 90),
            (0.05, POP, CYAN, WHITE, 40, -107.67, -59.76, 90),
            (0.05, POP, CYAN, WHITE, 40, -87.67, -39.76, 90),
            (0.05, POP, CYAN, WHITE, 40, -87.67, -39.76, 90),
            (0.05, POP, CYAN, WHITE, 40, -107.67, -19.76, 90),
            (0.05, POP, CYAN, WHITE, 40, -107.67, -19.76, 90),
            (0.05, POP, CYAN, WHITE, 40, -127.67, -39.76, 90),
            (0, ROCKET, CYAN, WHITE, 5, -107.67, -59.76, 10),
            (0.05, POP, CYAN, WHITE, 40, -127.67, -39.76, 90),
            (0, ROCKET, BLUE, WHITE, 5, -107.67, -59.76, 10),
            (0.05, ROCKET, CYAN, WHITE, 5, -87.67, -39.76, 10),
            (0.05, ROCKET, BLUE, WHITE, 5, -87.67, -39.76, 10),
            (0.05, ROCKET, CYAN, WHITE, 5, -107.67, -19.76, 10),
            (0.05, ROCKET, BLUE, WHITE, 5, -107.67, -19.76, 10),
            (0.05, ROCKET, CYAN, WHITE, 5, -127.67, -39.76, 10),
            (0, CIRCLE, PURPLE, WHITE, 20, -107.67, -59.76, 10),
            (0.05, ROCKET, BLUE, WHITE, 5, -127.67, -39.76, 10),
            (0, CIRCLE, CYAN, WHITE, 20, -107.67, -59.76, 10),
            (0.05, CIRCLE, PURPLE, WHITE, 20, -87.67, -39.76, 10),
            (0.05, CIRCLE, CYAN, WHITE, 20, -87.67, -39.76, 10),
            (0.05, CIRCLE, PURPLE, WHITE, 20, -107.67, -19.76, 10),
            (0.05, CIRCLE, CYAN, WHITE, 20, -107.67, -19.76, 10),
            (0.05, CIRCLE, PURPLE, WHITE, 20, -127.67, -39.76, 10),
            (0.05, CIRCLE, CYAN, WHITE, 20, -127.67, -39.76, 10),
            (0.35, CIRCLESPRITE, WHITE, SNOWFLAKE, 49, -107.67, -59.76, 110),
            (0.06, CIRCLESPRITE, PURPLE, SNOWFLAKE, 49, -107.67, -59.76, 110),
            (0.05, CIRCLESPRITE, WHITE, SNOWFLAKE, 49, -87.67, -39.76, 110),
            (0.05, CIRCLESPRITE, PURPLE, WHITE, 49, -87.67, -39.76, 110),
            (0.05, CIRCLESPRITE, WHITE, SNOWFLAKE, 49, -107.67, -19.76, 110),
            (0.05, CIRCLESPRITE, PURPLE, SNOWFLAKE, 49, -107.67, -19.76, 110),
            (0.05, CIRCLESPRITE, WHITE, SNOWFLAKE, 49, -127.67, -39.76, 110),
            (0.06, CIRCLESPRITE, PURPLE, SNOWFLAKE, 49, -127.67, -39.76, 110),
            (0.09, POP, PURPLE, WHITE, 49, -127.67, -39.76, 110),
            (0.09, POP, PURPLE, WHITE, 49, -127.67, -39.76, 110),
            (0.09, POP, PURPLE, WHITE, 49, -127.67, -39.76, 110),
            (0.06, POP, PURPLE, WHITE, 49, -127.67, -39.76, 110),
            (0.25, CIRCLESPRITE, PINK, SNOWFLAKE, 65, -107.67, -59.76, 110),
            (0.16, CIRCLESPRITE, PINK, SNOWFLAKE, 65, -87.67, -39.76, 110),
            (0.22, CIRCLESPRITE, PINK, SNOWFLAKE, 65, -107.67, -19.76, 110),
            (0.12, CIRCLESPRITE, PINK, SNOWFLAKE, 65, -127.67, -39.76, 110),
            (0.22, POP, PURPLE, WHITE, 49, -127.67, -39.76, 110),
            (0.09, POP, PURPLE, WHITE, 49, -127.67, -39.76, 110),
            (0.09, POP, PURPLE, WHITE, 49, -127.67, -39.76, 110),
            (0.12, POP, PURPLE, WHITE, 49, -127.67, -39.76, 110),
            (0.28, CIRCLESPRITE, WHITE, SNOWFLAKE, 55, -107.67, -59.76, 110),
            (0.12, CIRCLESPRITE, WHITE, SNOWFLAKE, 55, -87.67, -39.76, 110),
            (0.12, CIRCLESPRITE, WHITE, SNOWFLAKE, 55, -107.67, -19.76, 110),
            (0.09, CIRCLESPRITE, WHITE, SNOWFLAKE, 55, -127.67, -39.76, 110),
        ),
        # Donalds Dock
        (
            (4.5, ROCKET, YELLOW, WHITE, 5, 0, 190, 0),
            (0.5, ROCKET, YELLOW, WHITE, 5, 14.69, 179.71, 0),
            (0.5, ROCKET, YELLOW, WHITE, 5, 20, 170, 0),
            (0.5, ROCKET, YELLOW, WHITE, 5, 25.65, 158.38, 0),
            (0.5, ROCKET, YELLOW, WHITE, 5, 35, .5, 0),
            (0.5, ROCKET, YELLOW, WHITE, 5, 37.27, 139.59, 0),
            (0.5, ROCKET, YELLOW, WHITE, 5, 40, 130, 0),
            (0.5, ROCKET, YELLOW, WHITE, 5, 54.79, 127.03, 0),
            (3.5, ROCKET, WHITE, YELLOW, 5, 54.79, 127.03, 0),
            (0.5, ROCKET, WHITE, YELLOW, 5, 40, 130, 0),
            (0.5, ROCKET, WHITE, YELLOW, 5, 37.27, 139.59, 0),
            (0.5, ROCKET, WHITE, YELLOW, 5, 35, .5, 0),
            (0.5, ROCKET, WHITE, YELLOW, 5, 25.65, 158.38, 0),
            (0.5, ROCKET, WHITE, YELLOW, 5, 20, 170, 0),
            (0.5, ROCKET, WHITE, YELLOW, 5, 14.69, 179.71, 0),
            (0.5, ROCKET, WHITE, YELLOW, 5, 0, 190, 0),
            (4, ROCKET, YELLOW, WHITE, 5, 35, .5, 0),
            (0, ROCKET, YELLOW, WHITE, 5, 0, 190, 0),
            (0, ROCKET, YELLOW, WHITE, 5, 40, 130, 0),
            (0, ROCKET, YELLOW, WHITE, 5, 20, 170, 0),
            (1, ROCKET, WHITE, YELLOW, 5, 25.65, 158.38, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 14.69, 179.71, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 37.27, 139.59, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 54.79, 127.03, 0),
            (2, ROCKET, WHITE, YELLOW, 5, 54.79, 127.03, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 0, 190, 0),
            (0.31, ROCKET, WHITE, YELLOW, 5, 40, 130, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 14.69, 179.71, 0),
            (0.31, ROCKET, WHITE, YELLOW, 5, 20, 170, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 37.27, 139.59, 0),
            (0.38, ROCKET, WHITE, YELLOW, 5, 25.65, 158.38, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 35, .5, 0),
            (4, ROCKET, WHITE, YELLOW, 5, 35, .5, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 25.65, 158.38, 0),
            (0.38, ROCKET, WHITE, YELLOW, 5, 20, 170, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 37.27, 139.59, 0),
            (0.37, ROCKET, WHITE, YELLOW, 5, 40, 130, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 14.69, 179.71, 0),
            (0.25, ROCKET, WHITE, YELLOW, 5, 0, 190, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 54.79, 127.03, 0),
            (4, ROCKET, WHITE, YELLOW, 5, 0, 190, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 54.79, 127.03, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 35, .5, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 25.65, 158.38, 0),
            (0.5, ROCKET, WHITE, YELLOW, 5, 40, 130, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 37.27, 139.59, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 14.69, 179.71, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 20, 170, 0),
            (0.5, ROCKET, WHITE, YELLOW, 5, 25.65, 158.38, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 54.79, 127.03, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 35, .5, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 0, 190, 0),
            (0, ROCKET, WHITE, YELLOW, 5, 25.65, 158.38, 0),
            (2, ROCKET, WHITE, YELLOW, 5, 0, 190, 0),
            (0.25, ROCKET, WHITE, YELLOW, 5, 14.69, 179.71, 0),
            (0.25, ROCKET, WHITE, YELLOW, 5, 20, 170, 0),
            (0.25, ROCKET, WHITE, YELLOW, 5, 25.65, 158.38, 0),
            (0.5, ROCKET, WHITE, YELLOW, 5, 54.79, 127.03, 0),
            (0.25, ROCKET, WHITE, YELLOW, 5, 40, 130, 0),
            (0.25, ROCKET, WHITE, YELLOW, 5, 37.27, 139.59, 0),
            (0.25, ROCKET, WHITE, YELLOW, 5, 35, .5, 0),
            (3.13, ROCKET, YELLOW, WHITE, 5, 54.79, 127.03, 0),
            (0, ROCKET, YELLOW, WHITE, 5, 0, 190, 0),
            (0.25, ROCKET, PINK, WHITE, 5, 0, 190, 0),
            (0, ROCKET, PINK, WHITE, 5, 54.79, 127.03, 0),
            (0.25, ROCKET, PURPLE, WHITE, 5, 54.79, 127.03, 0),
            (0, ROCKET, PURPLE, WHITE, 5, 54.79, 127.03, 0),
            (0.25, ROCKET, YELLOW, WHITE, 5, 14.69, 179.71, 0),
            (0, ROCKET, YELLOW, WHITE, 5, 40, 130, 0),
            (0.25, ROCKET, PINK, WHITE, 5, 40, 130, 0),
            (0, ROCKET, PINK, WHITE, 5, 14.69, 179.71, 0),
            (0.25, ROCKET, PURPLE, WHITE, 5, 14.69, 179.71, 0),
            (0, ROCKET, PURPLE, WHITE, 5, 40, 130, 0),
            (0.25, ROCKET, YELLOW, WHITE, 5, 37.27, 139.59, 0),
            (0, ROCKET, YELLOW, WHITE, 5, 20, 170, 0),
            (0.25, ROCKET, PINK, WHITE, 5, 37.27, 139.59, 0),
            (0, ROCKET, PINK, WHITE, 5, 20, 170, 0),
            (0.25, ROCKET, PURPLE, WHITE, 5, 37.27, 139.59, 0),
            (0, ROCKET, PURPLE, WHITE, 5, 20, 170, 0),
            (2.88, ROCKET, YELLOW, WHITE, 5, 0, 190, 0),
            (0.25, ROCKET, PINK, WHITE, 5, 0, 190, 0),
            (0.25, ROCKET, PURPLE, WHITE, 5, 0, 190, 0),
            (0, ROCKET, YELLOW, WHITE, 5, 14.69, 179.71, 0),
            (0.25, ROCKET, PINK, WHITE, 5, 14.69, 179.71, 0),
            (0.25, ROCKET, YELLOW, WHITE, 5, 20, 170, 0),
            (0, ROCKET, PURPLE, WHITE, 5, 20, 170, 0),
            (0.25, ROCKET, PINK, WHITE, 5, 20, 170, 0),
            (0.25, ROCKET, PURPLE, WHITE, 5, 25.65, 158.38, 0),
            (0, ROCKET, YELLOW, WHITE, 5, 25.65, 158.38, 0),
            (0.25, ROCKET, PINK, WHITE, 5, 25.65, 158.38, 0),
            (0.25, ROCKET, YELLOW, WHITE, 5, 35, .5, 0),
            (0.25, ROCKET, PINK, WHITE, 5, 35, .5, 0),
            (0.25, ROCKET, PURPLE, WHITE, 5, 35, .5, 0),
            (0, ROCKET, YELLOW, WHITE, 5, 37.27, 139.59, 0),
            (0.25, ROCKET, PINK, WHITE, 5, 37.27, 139.59, 0),
            (0.25, ROCKET, PURPLE, WHITE, 5, 37.27, 139.59, 0),
            (0, ROCKET, YELLOW, WHITE, 5, 40, 130, 0),
            (0.25, ROCKET, PINK, WHITE, 5, 40, 130, 0),
            (0.25, ROCKET, PURPLE, WHITE, 5, 40, 130, 0),
            (0, ROCKET, YELLOW, WHITE, 5, 54.79, 127.03, 0),
            (0.25, ROCKET, PINK, WHITE, 5, 54.79, 127.03, 0),
            (0.25, ROCKET, PURPLE, WHITE, 5, 54.79, 127.03, 0),
            (3.99, POP, PINK, WHITE, 5, 40, 130, 0),
            (0.12, POP, PINK, WHITE, 5, 40, 130, 0),
            (0.14, POP, PINK, WHITE, 5, 40, 130, 0),
            (0.75, POP, PINK, WHITE, 5, 40, 130, 0),
            (0.12, POP, PINK, WHITE, 5, 40, 130, 0),
            (0.13, POP, PINK, WHITE, 5, 40, 130, 0),
            (0.75, POP, PINK, WHITE, 5, 40, 130, 0),
            (0.13, POP, PINK, WHITE, 5, 40, 130, 0),
            (0.12, POP, PINK, WHITE, 5, 40, 130, 0),
            (0.71, CIRCLE, YELLOW, WHITE, 10, 0, 190, 5),
            (0.03, ROCKET, YELLOW, WHITE, 5, 0, 190, 0),
            (0.09, CIRCLE, YELLOW, WHITE, 10, 14.69, 179.71, 0),
            (0.03, ROCKET, YELLOW, WHITE, 5, 14.69, 179.71, 0),
            (0.09, CIRCLE, YELLOW, WHITE, 10, 20, 170, 0),
            (0.04, ROCKET, YELLOW, WHITE, 5, 20, 170, 0),
            (0.08, CIRCLE, YELLOW, WHITE, 10, 35, .5, 0),
            (0.04, ROCKET, YELLOW, WHITE, 5, 35, .5, 0),
            (0.08, CIRCLE, YELLOW, WHITE, 10, 35, .5, 0),
            (0.05, ROCKET, YELLOW, WHITE, 5, 35, .5, 0),
            (0.07, CIRCLE, YELLOW, WHITE, 10, 37.27, 139.59, 0),
            (0.05, ROCKET, YELLOW, WHITE, 5, 37.27, 139.59, 0),
            (0.07, CIRCLE, YELLOW, WHITE, 10, 40, 130, 0),
            (0.06, ROCKET, YELLOW, WHITE, 5, 40, 130, 0),
            (0.06, CIRCLE, YELLOW, WHITE, 10, 54.79, 127.03, 0),
            (0.06, ROCKET, YELLOW, WHITE, 5, 54.79, 127.03, 0),
            (0.56, CIRCLE, PINK, WHITE, 12, 0, 190, 5),
            (0.04, ROCKET, PINK, WHITE, 7, 0, 190, 0),
            (0.08, CIRCLE, PINK, WHITE, 12, 14.69, 179.71, 5),
            (0.04, ROCKET, PINK, WHITE, 7, 14.69, 179.71, 0),
            (0.08, CIRCLE, PINK, WHITE, 7, 20, 170, 5),
            (0.05, ROCKET, PINK, WHITE, 7, 20, 170, 0),
            (0.06, CIRCLE, PINK, WHITE, 12, 35, .5, 5),
            (0.03, ROCKET, PINK, WHITE, 7, 35, .5, 0),
            (0.10, CIRCLE, PINK, WHITE, 12, 35, .5, 5),
            (0.03, ROCKET, PINK, WHITE, 7, 35, .5, 0),
            (0.09, CIRCLE, PINK, WHITE, 12, 37.27, 139.59, 5),
            (0.03, ROCKET, PINK, WHITE, 7, 37.27, 139.59, 0),
            (0.09, CIRCLE, PINK, WHITE, 12, 40, 130, 5),
            (0.04, ROCKET, PINK, WHITE, 7, 40, 130, 0),
            (0.08, CIRCLE, PINK, WHITE, 12, 54.79, 127.03, 5),
            (0.04, ROCKET, PINK, WHITE, 7, 54.79, 127.03, 0),
            (0.58, CIRCLE, PURPLE, WHITE, 14, 0, 190, 5),
            (0.05, ROCKET, PURPLE, WHITE, 9, 0, 190, 0),
            (0.12, CIRCLE, PURPLE, WHITE, 14, 14.69, 179.71, 5),
            (0.03, ROCKET, PURPLE, WHITE, 9, 14.69, 179.71, 0),
            (0.09, CIRCLE, PURPLE, WHITE, 14, 20, 170, 5),
            (0.06, ROCKET, PURPLE, WHITE, 9, 20, 170, 0),
            (0.09, CIRCLE, PURPLE, WHITE, 14, 35, .5, 5),
            (0.06, ROCKET, PURPLE, WHITE, 9, 35, .5, 0),
            (0.09, CIRCLE, PURPLE, WHITE, 14, 35, .5, 5),
            (0.03, ROCKET, PURPLE, WHITE, 9, 35, .5, 0),
            (0.12, CIRCLE, PURPLE, WHITE, 14, 37.27, 139.59, 5),
            (0.03, ROCKET, PURPLE, WHITE, 9, 37.27, 139.59, 0),
            (0.12, CIRCLE, PURPLE, WHITE, 14, 40, 130, 0),
            (0.03, ROCKET, PURPLE, WHITE, 9, 40, 130, 0),
            (0.09, CIRCLE, PURPLE, WHITE, 14, 54.79, 127.03, 5),
            (0.06, ROCKET, PURPLE, WHITE, 9, 54.79, 127.03, 0),
            (0.5, CIRCLELARGE, YELLOW, WHITE, 10, 0, 190, 80),
            (0.06, CIRCLELARGE, YELLOW, WHITE, 10, 14.69, 179.71, 80),
            (0.06, CIRCLELARGE, YELLOW, WHITE, 10, 20, 170, 80),
            (0.06, CIRCLELARGE, YELLOW, WHITE, 10, 35, .5, 80),
            (0.06, CIRCLELARGE, YELLOW, WHITE, 10, 35, .5, 80),
            (0.06, CIRCLELARGE, YELLOW, WHITE, 10, 37.27, 139.59, 80),
            (0.06, CIRCLELARGE, YELLOW, WHITE, 10, 40, 130, 80),
            (0.06, CIRCLELARGE, YELLOW, WHITE, 10, 54.79, 127.03, 80),
            (0.56, CIRCLELARGE, PINK, WHITE, 15, 0, 190, 90),
            (0.06, CIRCLELARGE, PINK, WHITE, 15, 14.69, 179.71, 90),
            (0.06, CIRCLELARGE, PINK, WHITE, 15, 20, 170, 90),
            (0.06, CIRCLELARGE, PINK, WHITE, 15, 35, .5, 90),
            (0.06, CIRCLELARGE, PINK, WHITE, 15, 35, .5, 90),
            (0.06, CIRCLELARGE, PINK, WHITE, 15, 37.27, 139.59, 0),
            (0.06, CIRCLELARGE, PINK, WHITE, 15, 40, 130, 90),
            (0.06, CIRCLELARGE, PINK, WHITE, 7, 54.79, 127.03, 90),
            (0.56, CIRCLELARGE, PURPLE, WHITE, 20, 0, 190, 100),
            (0.06, CIRCLELARGE, PURPLE, WHITE, 20, 14.69, 179.71, 100),
            (0.06, CIRCLELARGE, PURPLE, WHITE, 20, 20, 170, 100),
            (0.06, CIRCLELARGE, PURPLE, WHITE, 20, 35, .5, 100),
            (0.06, CIRCLELARGE, PURPLE, WHITE, 20, 35, .5, 100),
            (0.06, CIRCLELARGE, PURPLE, WHITE, 20, 37.27, 139.59, 100),
            (0.06, CIRCLELARGE, PURPLE, WHITE, 9, 40, 130, 0),
            (0.06, CIRCLELARGE, PURPLE, WHITE, 20, 54.79, 127.03, 100),
        ),
    ],

    PartyGlobals.FireworkShows.Summer: [
        # copy of Toontown Central New Years
        (
            (0.50, ROCKET, WHITE, WHITE, 5.00, 113.22 +
             PartyGlobals.FireworksGlobalXOffset, 1.05 +
             PartyGlobals.FireworksGlobalYOffset, 73.24),
            (0.25, ROCKET, RED, RED, 5.00, 115.54 +
             PartyGlobals.FireworksGlobalXOffset, 13.80 +
             PartyGlobals.FireworksGlobalYOffset, 59.11),
            (0.03, ROCKET, RED, RED, 5.00, 118.36 +
             PartyGlobals.FireworksGlobalXOffset, -
             13.83 +
             PartyGlobals.FireworksGlobalYOffset, 57.71),
            (0.22, ROCKET, BLUE, BLUE, 5.00, 110.05 +
             PartyGlobals.FireworksGlobalXOffset, 25.37 +
             PartyGlobals.FireworksGlobalYOffset, 57.01),
            (0.03, ROCKET, BLUE, BLUE, 5.00, 110.05 +
             PartyGlobals.FireworksGlobalXOffset, -
             25.37 +
             PartyGlobals.FireworksGlobalYOffset, 57.01),
            (3.22, CIRCLELARGE, WHITE, WHITE, 10.00, 121.75 +
             PartyGlobals.FireworksGlobalXOffset, 1.07 +
             PartyGlobals.FireworksGlobalYOffset, 106.69),
            (1.94, CIRCLELARGE, RED, RED, 10.00, 121.75 +
             PartyGlobals.FireworksGlobalXOffset, 1.07 +
             PartyGlobals.FireworksGlobalYOffset, 106.69),
            (1.31, ROCKET, BLUE, BLUE, 4.00, 121.75 +
             PartyGlobals.FireworksGlobalXOffset, 28.63 +
             PartyGlobals.FireworksGlobalYOffset, 38.55),
            (0.06, ROCKET, RED, RED, 4.00, 121.75 +
             PartyGlobals.FireworksGlobalXOffset, 1.30 +
             PartyGlobals.FireworksGlobalYOffset, 38.76),
            (0.06, ROCKET, WHITE, WHITE, 4.00, 121.81 +
             PartyGlobals.FireworksGlobalXOffset, -
             25.60 +
             PartyGlobals.FireworksGlobalYOffset, 37.54),
            (0.88, ROCKET, BLUE, BLUE, 4.00, 121.81 +
             PartyGlobals.FireworksGlobalXOffset, -
             25.60 +
             PartyGlobals.FireworksGlobalYOffset, 37.54),
            (0.06, ROCKET, RED, RED, 4.00, 121.74 +
             PartyGlobals.FireworksGlobalXOffset, 1.30 +
             PartyGlobals.FireworksGlobalYOffset, 37.75),
            (0.06, ROCKET, WHITE, WHITE, 4.00, 121.81 +
             PartyGlobals.FireworksGlobalXOffset, 27.34 +
             PartyGlobals.FireworksGlobalYOffset, 37.12),
            (0.82, ROCKET, BLUE, BLUE, 4.00, 55.00 +
             PartyGlobals.FireworksGlobalXOffset, 40.00 +
             PartyGlobals.FireworksGlobalYOffset, 40.00),
            (0.09, ROCKET, RED, RED, 4.00, 70.00 +
             PartyGlobals.FireworksGlobalXOffset, 40.00 +
             PartyGlobals.FireworksGlobalYOffset, 40.00),
            (0.09, ROCKET, WHITE, WHITE, 4.00, 85.00 +
             PartyGlobals.FireworksGlobalXOffset, 40.00 +
             PartyGlobals.FireworksGlobalYOffset, 40.00),
            (0.72, ROCKET, BLUE, BLUE, 4.00, 55.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             40.00 +
             PartyGlobals.FireworksGlobalYOffset, 40.00),
            (0.09, ROCKET, RED, RED, 4.00, 70.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             40.00 +
             PartyGlobals.FireworksGlobalYOffset, 40.00),
            (0.09, ROCKET, WHITE, WHITE, 4.00, 85.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             40.00 +
             PartyGlobals.FireworksGlobalYOffset, 40.00),
            (0.84, CIRCLE, BLUE, BLUE, 10.00, 121.81 +
             PartyGlobals.FireworksGlobalXOffset, 29.29 +
             PartyGlobals.FireworksGlobalYOffset, 78.62),
            (0.06, RING, WHITE, WHITE, 5.00, 121.81 +
             PartyGlobals.FireworksGlobalXOffset, 29.29 +
             PartyGlobals.FireworksGlobalYOffset, 78.62),
            (0.75, CIRCLE, RED, RED, 10.00, 120.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             30.00 +
             PartyGlobals.FireworksGlobalYOffset, 100.00),
            (0.06, RING, WHITE, WHITE, 5.00, 120.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             30.00 +
             PartyGlobals.FireworksGlobalYOffset, 100.00),
            (0.70, CIRCLE, WHITE, WHITE, 10.00, 121.81 +
             PartyGlobals.FireworksGlobalXOffset, 29.29 +
             PartyGlobals.FireworksGlobalYOffset, 92.00),
            (0.19, RING, BLUE, BLUE, 5.00, 121.81 +
             PartyGlobals.FireworksGlobalXOffset, 29.29 +
             PartyGlobals.FireworksGlobalYOffset, 92.00),
            (0.80, CIRCLE, WHITE, WHITE, 10.00, 121.81 +
             PartyGlobals.FireworksGlobalXOffset, 0.00 +
             PartyGlobals.FireworksGlobalYOffset, 100.00),
            (0.08, RING, RED, RED, 5.00, 121.81 +
             PartyGlobals.FireworksGlobalXOffset, 0.00 +
             PartyGlobals.FireworksGlobalYOffset, 100.00),
            (1.00, ROCKET, WHITE, PEACH, 4.00, 11.43 +
             PartyGlobals.FireworksGlobalXOffset, 22.69 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.25, ROCKET, WHITE, PEACH, 4.00, 11.24 +
             PartyGlobals.FireworksGlobalXOffset, 17.57 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.25, ROCKET, WHITE, PEACH, 4.00, 10.82 +
             PartyGlobals.FireworksGlobalXOffset, 12.13 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.22, ROCKET, WHITE, PEACH, 4.00, 11.17 +
             PartyGlobals.FireworksGlobalXOffset, 6.76 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.31, ROCKET, WHITE, PEACH, 4.00, 11.10 +
             PartyGlobals.FireworksGlobalXOffset, 1.91 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.25, ROCKET, WHITE, PEACH, 4.00, 11.71 +
             PartyGlobals.FireworksGlobalXOffset, -
             3.56 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.19, ROCKET, WHITE, PEACH, 4.00, 11.26 +
             PartyGlobals.FireworksGlobalXOffset, -
             8.51 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.28, ROCKET, WHITE, PEACH, 4.00, 11.25 +
             PartyGlobals.FireworksGlobalXOffset, -
             14.18 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.25, ROCKET, WHITE, PEACH, 4.00, 11.20 +
             PartyGlobals.FireworksGlobalXOffset, -
             19.42 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.25, ROCKET, WHITE, PEACH, 4.00, 11.53 +
             PartyGlobals.FireworksGlobalXOffset, -
             24.46 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (1.24, CIRCLESMALL, RED, WHITE, 15.00, 68.68 +
             PartyGlobals.FireworksGlobalXOffset, -
             29.58 +
             PartyGlobals.FireworksGlobalYOffset, 57.72),
            (1.63, CIRCLE, BLUE, WHITE, 15.00, 70.33 +
             PartyGlobals.FireworksGlobalXOffset, 29.76 +
             PartyGlobals.FireworksGlobalYOffset, 56.30),
            (0.87, CIRCLELARGE, WHITE, WHITE, 15.00, 121.64 +
             PartyGlobals.FireworksGlobalXOffset, 1.20 +
             PartyGlobals.FireworksGlobalYOffset, 92.64),
            (1.26, RING, WHITE, WHITE, 15.00, 83.12 +
             PartyGlobals.FireworksGlobalXOffset, 12.21 +
             PartyGlobals.FireworksGlobalYOffset, 92.04),
            (0.44, RING, RED, RED, 15.00, 84.41 +
             PartyGlobals.FireworksGlobalXOffset, -
             23.72 +
             PartyGlobals.FireworksGlobalYOffset, 78.01),
            (0.44, RING, WHITE, WHITE, 15.00, 83.50 +
             PartyGlobals.FireworksGlobalXOffset, 1.77 +
             PartyGlobals.FireworksGlobalYOffset, 68.65),
            (0.38, RING, BLUE, BLUE, 15.00, 82.60 +
             PartyGlobals.FireworksGlobalXOffset, 26.64 +
             PartyGlobals.FireworksGlobalYOffset, 68.65),
            (0.37, CIRCLESMALL, WHITE, WHITE, 11.00, 74.50 +
             PartyGlobals.FireworksGlobalXOffset, 15.00 +
             PartyGlobals.FireworksGlobalYOffset, 71.80),
            (0.12, CIRCLELARGE, RED, RED, 11.00, 74.50 +
             PartyGlobals.FireworksGlobalXOffset, 15.00 +
             PartyGlobals.FireworksGlobalYOffset, 71.80),
            (0.75, CIRCLESMALL, WHITE, WHITE, 11.00, 94.03 +
             PartyGlobals.FireworksGlobalXOffset, -
             15.23 +
             PartyGlobals.FireworksGlobalYOffset, 62.12),
            (0.13, CIRCLELARGE, BLUE, BLUE, 11.00, 94.03 +
             PartyGlobals.FireworksGlobalXOffset, -
             15.23 +
             PartyGlobals.FireworksGlobalYOffset, 62.12),
            (0.56, CIRCLESMALL, RED, RED, 11.00, 54.56 +
             PartyGlobals.FireworksGlobalXOffset, 7.87 +
             PartyGlobals.FireworksGlobalYOffset, 53.74),
            (0.19, CIRCLELARGE, WHITE, WHITE, 11.00, 54.56 +
             PartyGlobals.FireworksGlobalXOffset, 7.87 +
             PartyGlobals.FireworksGlobalYOffset, 53.74),
            (0.63, CIRCLESMALL, BLUE, BLUE, 11.00, 82.51 +
             PartyGlobals.FireworksGlobalXOffset, 0.23 +
             PartyGlobals.FireworksGlobalYOffset, 82.99),
            (0.12, CIRCLELARGE, WHITE, WHITE, 11.00, 82.51 +
             PartyGlobals.FireworksGlobalXOffset, 0.23 +
             PartyGlobals.FireworksGlobalYOffset, 82.99),
            (0.37, RING, RED, RED, 5.00, 82.51 +
             PartyGlobals.FireworksGlobalXOffset, 0.23 +
             PartyGlobals.FireworksGlobalYOffset, 82.99),
            (0.47, RING, WHITE, WHITE, 6.00, 82.51 +
             PartyGlobals.FireworksGlobalXOffset, 0.23 +
             PartyGlobals.FireworksGlobalYOffset, 82.99),
            (0.47, RING, BLUE, BLUE, 7.00, 82.51 +
             PartyGlobals.FireworksGlobalXOffset, 0.23 +
             PartyGlobals.FireworksGlobalYOffset, 82.99),
            (0.47, RING, WHITE, WHITE, 8.00, 82.51 +
             PartyGlobals.FireworksGlobalXOffset, 0.23 +
             PartyGlobals.FireworksGlobalYOffset, 82.99),
            (0.47, RING, RED, RED, 10.00, 82.51 +
             PartyGlobals.FireworksGlobalXOffset, 0.23 +
             PartyGlobals.FireworksGlobalYOffset, 82.99),
            (0.37, ROCKET, WHITE, WHITE, 8.00, 53.85 +
             PartyGlobals.FireworksGlobalXOffset, 14.92 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.06, ROCKET, WHITE, WHITE, 8.00, 54.66 +
             PartyGlobals.FireworksGlobalXOffset, -
             16.71 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.44, ROCKET, WHITE, WHITE, 8.00, 73.27 +
             PartyGlobals.FireworksGlobalXOffset, 15.16 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.06, ROCKET, WHITE, WHITE, 8.00, 73.38 +
             PartyGlobals.FireworksGlobalXOffset, -
             15.98 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.44, ROCKET, WHITE, WHITE, 8.00, 93.33 +
             PartyGlobals.FireworksGlobalXOffset, 15.17 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.06, ROCKET, WHITE, WHITE, 8.00, 93.71 +
             PartyGlobals.FireworksGlobalXOffset, -
             15.73 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.89, CIRCLELARGE, WHITE, WHITE, 8.00, 151.88 +
             PartyGlobals.FireworksGlobalXOffset, 1.92 +
             PartyGlobals.FireworksGlobalYOffset, 144.56),
            (0.93, CIRCLESMALL, WHITE, WHITE, 8.00, 82.25 +
             PartyGlobals.FireworksGlobalXOffset, 16.72 +
             PartyGlobals.FireworksGlobalYOffset, 82.50),
            (0.12, CIRCLELARGE, WHITE, WHITE, 8.00, 79.31 +
             PartyGlobals.FireworksGlobalXOffset, 1.00 +
             PartyGlobals.FireworksGlobalYOffset, 63.69),
            (0.13, CIRCLESMALL, WHITE, WHITE, 8.00, 82.02 +
             PartyGlobals.FireworksGlobalXOffset, -
             13.25 +
             PartyGlobals.FireworksGlobalYOffset, 79.16),
            (0.88, ROCKET, WHITE, RED, 4.00, 6.47 +
             PartyGlobals.FireworksGlobalXOffset, -
             15.00 +
             PartyGlobals.FireworksGlobalYOffset, 8.60),
            (0.06, ROCKET, WHITE, RED, 4.00, 18.41 +
             PartyGlobals.FireworksGlobalXOffset, 15.00 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.31, ROCKET, WHITE, BLUE, 4.00, 53.79 +
             PartyGlobals.FireworksGlobalXOffset, 15.00 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.06, ROCKET, WHITE, BLUE, 4.00, 54.85 +
             PartyGlobals.FireworksGlobalXOffset, -
             15.00 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.50, ROCKET, RED, RED, 4.00, 90.45 +
             PartyGlobals.FireworksGlobalXOffset, -
             15.00 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.19, ROCKET, RED, RED, 4.00, 90.21 +
             PartyGlobals.FireworksGlobalXOffset, 15.00 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.19, ROCKET, BLUE, BLUE, 4.00, 90.21 +
             PartyGlobals.FireworksGlobalXOffset, 0.00 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.44, CIRCLE, WHITE, WHITE, 4.00, 18.41 +
             PartyGlobals.FireworksGlobalXOffset, 15.00 +
             PartyGlobals.FireworksGlobalYOffset, 90.00),
            (0.06, RING, RED, RED, 1.00, 18.41 +
             PartyGlobals.FireworksGlobalXOffset, 15.00 +
             PartyGlobals.FireworksGlobalYOffset, 90.00),
            (0.75, CIRCLE, WHITE, WHITE, 4.00, 93.56 +
             PartyGlobals.FireworksGlobalXOffset, -
             16.02 +
             PartyGlobals.FireworksGlobalYOffset, 72.89),
            (0.06, RING, RED, RED, 1.00, 93.56 +
             PartyGlobals.FireworksGlobalXOffset, -
             16.02 +
             PartyGlobals.FireworksGlobalYOffset, 72.89),
            (0.69, CIRCLE, WHITE, WHITE, 4.00 +
             PartyGlobals.FireworksGlobalXOffset, 53.19 +
             PartyGlobals.FireworksGlobalYOffset, -
             10.03, 98.97),
            (0.06, RING, BLUE, BLUE, 1.00, 53.19 +
             PartyGlobals.FireworksGlobalXOffset, -
             10.03 +
             PartyGlobals.FireworksGlobalYOffset, 98.97),
            (0.69, CIRCLE, WHITE, WHITE, 4.00, 71.46 +
             PartyGlobals.FireworksGlobalXOffset, 13.03 +
             PartyGlobals.FireworksGlobalYOffset, 56.82),
            (0.06, RING, BLUE, BLUE, 1.00, 71.46 +
             PartyGlobals.FireworksGlobalXOffset, 13.03 +
             PartyGlobals.FireworksGlobalYOffset, 56.82),
            (0.25, CIRCLE, RED, RED, 4.00, 89.38 +
             PartyGlobals.FireworksGlobalXOffset, -
             3.18 +
             PartyGlobals.FireworksGlobalYOffset, 95.18),
            (0.06, RING, WHITE, WHITE, 1.00, 89.38 +
             PartyGlobals.FireworksGlobalXOffset, -
             3.18 +
             PartyGlobals.FireworksGlobalYOffset, 95.18),
            (0.31, CIRCLELARGE, WHITE, WHITE, 19.00, 94.74 +
             PartyGlobals.FireworksGlobalXOffset, 0.89 +
             PartyGlobals.FireworksGlobalYOffset, 65.55),
            (0.44, ROCKET, WHITE, PEACH, 3.00, 96.50 +
             PartyGlobals.FireworksGlobalXOffset, 2.50 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.06, ROCKET, WHITE, PEACH, 3.00, 95.93 +
             PartyGlobals.FireworksGlobalXOffset, -
             2.61 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.38, ROCKET, WHITE, PEACH, 3.00, 76.08 +
             PartyGlobals.FireworksGlobalXOffset, 7.72 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.06, ROCKET, WHITE, PEACH, 3.00, 76.54 +
             PartyGlobals.FireworksGlobalXOffset, -
             8.28 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.37, ROCKET, WHITE, PEACH, 3.00, 56.41 +
             PartyGlobals.FireworksGlobalXOffset, 12.05 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.06, ROCKET, WHITE, PEACH, 3.00, 56.76 +
             PartyGlobals.FireworksGlobalXOffset, -
             13.51 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.31, ROCKET, WHITE, PEACH, 3.00, 36.29 +
             PartyGlobals.FireworksGlobalXOffset, 16.92 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.10, ROCKET, WHITE, PEACH, 3.00, 37.03 +
             PartyGlobals.FireworksGlobalXOffset, -
             19.08 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.96, CIRCLESMALL, WHITE, WHITE, 3.00, 100.31 +
             PartyGlobals.FireworksGlobalXOffset, 2.50 +
             PartyGlobals.FireworksGlobalYOffset, 66.59),
            (0.06, CIRCLESMALL, WHITE, WHITE, 3.00, 100.31 +
             PartyGlobals.FireworksGlobalXOffset, -
             2.50 +
             PartyGlobals.FireworksGlobalYOffset, 66.59),
            (0.44, CIRCLESMALL, WHITE, RED, 6.00, 76.25 +
             PartyGlobals.FireworksGlobalXOffset, 8.00 +
             PartyGlobals.FireworksGlobalYOffset, 66.59),
            (0.06, CIRCLESMALL, WHITE, RED, 6.00, 76.25 +
             PartyGlobals.FireworksGlobalXOffset, -
             8.00 +
             PartyGlobals.FireworksGlobalYOffset, 66.59),
            (0.44, CIRCLE, WHITE, BLUE, 3.00, 34.77 +
             PartyGlobals.FireworksGlobalXOffset, 12.00 +
             PartyGlobals.FireworksGlobalYOffset, 66.59),
            (0.06, CIRCLE, WHITE, BLUE, 3.00, 34.77 +
             PartyGlobals.FireworksGlobalXOffset, -
             12.00 +
             PartyGlobals.FireworksGlobalYOffset, 66.59),
            (0.44, CIRCLELARGE, WHITE, WHITE, 3.00, 10.00 +
             PartyGlobals.FireworksGlobalXOffset, 16.00 +
             PartyGlobals.FireworksGlobalYOffset, 66.59),
            (0.06, CIRCLELARGE, WHITE, WHITE, 3.00, 10.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             16.00 +
             PartyGlobals.FireworksGlobalYOffset, 66.59),
            (0.94, CIRCLESPRITE, WHITE, ICECREAM, 6.00, 10.00 +
             PartyGlobals.FireworksGlobalXOffset, 0.00 +
             PartyGlobals.FireworksGlobalYOffset, 66.59),
            (2.25, ROCKET, WHITE, WHITE, 5.00, 50.00 +
             PartyGlobals.FireworksGlobalXOffset, 23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.13, ROCKET, RED, RED, 5.00, 90.00 +
             PartyGlobals.FireworksGlobalXOffset, 23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.44, ROCKET, WHITE, WHITE, 5.00, 50.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.06, ROCKET, RED, RED, 5.00, 90.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.38, ROCKET, WHITE, WHITE, 5.00, 50.00 +
             PartyGlobals.FireworksGlobalXOffset, 23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.13, ROCKET, BLUE, BLUE, 5.00, 90.00 +
             PartyGlobals.FireworksGlobalXOffset, 23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.25, ROCKET, WHITE, WHITE, 5.00, 50.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.25, ROCKET, BLUE, BLUE, 5.00, 90.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.63, ROCKET, RED, RED, 5.00, 50.00 +
             PartyGlobals.FireworksGlobalXOffset, 23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.13, ROCKET, BLUE, BLUE, 5.00, 50.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.25, ROCKET, BLUE, BLUE, 5.00, 90.00 +
             PartyGlobals.FireworksGlobalXOffset, 23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.19, ROCKET, RED, RED, 5.00, 90.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.94, ROCKET, WHITE, WHITE, 5.00, 74.23 +
             PartyGlobals.FireworksGlobalXOffset, -
             0.06 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.28, ROCKET, BLUE, BLUE, 5.00, 53.66 +
             PartyGlobals.FireworksGlobalXOffset, 0.14 +
             PartyGlobals.FireworksGlobalYOffset, 13.48),
            (0.28, ROCKET, RED, RED, 5.00, 53.96 +
             PartyGlobals.FireworksGlobalXOffset, -
             0.38 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.28, ROCKET, WHITE, WHITE, 5.00, 63.67 +
             PartyGlobals.FireworksGlobalXOffset, 10.54 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.34, ROCKET, WHITE, WHITE, 4.00, 63.88 +
             PartyGlobals.FireworksGlobalXOffset, -
             10.98 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.16, ROCKET, RED, RED, 5.00, 64.24 +
             PartyGlobals.FireworksGlobalXOffset, -
             4.44 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.16, ROCKET, RED, RED, 5.00, 64.16 +
             PartyGlobals.FireworksGlobalXOffset, 2.92 +
             PartyGlobals.FireworksGlobalYOffset, 4.00),
            (0.25, ROCKET, WHITE, WHITE, 5.00, 50.00 +
             PartyGlobals.FireworksGlobalXOffset, 23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.12, ROCKET, RED, RED, 5.00, 90.00 +
             PartyGlobals.FireworksGlobalXOffset, 23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.34, ROCKET, WHITE, WHITE, 5.00, 50.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.03, ROCKET, RED, RED, 5.00, 90.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.50, ROCKET, WHITE, WHITE, 5.00, 50.00 +
             PartyGlobals.FireworksGlobalXOffset, 23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.06, ROCKET, BLUE, BLUE, 5.00, 90.00 +
             PartyGlobals.FireworksGlobalXOffset, 23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.38, ROCKET, WHITE, WHITE, 5.00, 50.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.06, ROCKET, BLUE, BLUE, 5.00, 90.00 +
             PartyGlobals.FireworksGlobalXOffset, -
             23.91 +
             PartyGlobals.FireworksGlobalYOffset, 19.44),
            (0.34, ROCKET, BLUE, BLUE, 5.00, 107.79 +
             PartyGlobals.FireworksGlobalXOffset, 19.80 +
             PartyGlobals.FireworksGlobalYOffset, 24.32),
            (0.25, ROCKET, RED, RED, 5.00, 107.58 +
             PartyGlobals.FireworksGlobalXOffset, 11.29 +
             PartyGlobals.FireworksGlobalYOffset, 45.00),
            (0.22, ROCKET, WHITE, WHITE, 5.00, 108.22 +
             PartyGlobals.FireworksGlobalXOffset, 3.33 +
             PartyGlobals.FireworksGlobalYOffset, 60.00),
            (0.37, ROCKET, WHITE, WHITE, 5.00, 108.34 +
             PartyGlobals.FireworksGlobalXOffset, -
             0.98 +
             PartyGlobals.FireworksGlobalYOffset, 60.00),
            (0.22, ROCKET, RED, RED, 5.00, 108.45 +
             PartyGlobals.FireworksGlobalXOffset, -
             9.33 +
             PartyGlobals.FireworksGlobalYOffset, 45.00),
            (0.19, ROCKET, BLUE, BLUE, 5.00, 108.69 +
             PartyGlobals.FireworksGlobalXOffset, -
             17.77 +
             PartyGlobals.FireworksGlobalYOffset, 24.40),
            (0.53, ROCKET, BLUE, BLUE, 5.00, 107.79 +
             PartyGlobals.FireworksGlobalXOffset, 19.80 +
             PartyGlobals.FireworksGlobalYOffset, 24.32),
            (0.25, ROCKET, RED, RED, 5.00, 107.58 +
             PartyGlobals.FireworksGlobalXOffset, 11.29 +
             PartyGlobals.FireworksGlobalYOffset, 45.00),
            (0.25, ROCKET, WHITE, WHITE, 5.00, 108.22 +
             PartyGlobals.FireworksGlobalXOffset, 3.33 +
             PartyGlobals.FireworksGlobalYOffset, 60.00),
            (0.50, ROCKET, WHITE, WHITE, 5.00, 108.34 +
             PartyGlobals.FireworksGlobalXOffset, -
             0.98 +
             PartyGlobals.FireworksGlobalYOffset, 60.00),
            (0.19, ROCKET, RED, RED, 5.00, 108.45 +
             PartyGlobals.FireworksGlobalXOffset, -
             9.33 +
             PartyGlobals.FireworksGlobalYOffset, 45.00),
            (0.19, ROCKET, BLUE, BLUE, 5.00, 108.69 +
             PartyGlobals.FireworksGlobalXOffset, -
             17.77 +
             PartyGlobals.FireworksGlobalYOffset, 24.40),
            (0.50, ROCKET, BLUE, BLUE, 5.00, 107.79 +
             PartyGlobals.FireworksGlobalXOffset, 19.80 +
             PartyGlobals.FireworksGlobalYOffset, 24.32),
            (0.06, ROCKET, BLUE, BLUE, 5.00, 108.69 +
             PartyGlobals.FireworksGlobalXOffset, -
             17.77 +
             PartyGlobals.FireworksGlobalYOffset, 24.40),
            (0.19, ROCKET, WHITE, WHITE, 5.00, 108.22 +
             PartyGlobals.FireworksGlobalXOffset, 3.33 +
             PartyGlobals.FireworksGlobalYOffset, 60.00),
            (0.06, ROCKET, WHITE, WHITE, 5.00, 108.34 +
             PartyGlobals.FireworksGlobalXOffset, -
             0.98 +
             PartyGlobals.FireworksGlobalYOffset, 60.00),
            (0.19, ROCKET, BLUE, BLUE, 5.00, 107.79 +
             PartyGlobals.FireworksGlobalXOffset, 19.80 +
             PartyGlobals.FireworksGlobalYOffset, 24.32),
            (0.06, ROCKET, BLUE, BLUE, 5.00, 108.69 +
             PartyGlobals.FireworksGlobalXOffset, -
             17.77 +
             PartyGlobals.FireworksGlobalYOffset, 24.40),
            (0.94, CIRCLELARGE, BLUE, BLUE, 5.00, 43.82 +
             PartyGlobals.FireworksGlobalXOffset, -
             2.09 +
             PartyGlobals.FireworksGlobalYOffset, 49.31),
            (0.25, POP, BLUE, BLUE, 5.00, 43.82 +
             PartyGlobals.FireworksGlobalXOffset, -
             2.09 +
             PartyGlobals.FireworksGlobalYOffset, 49.31),
            (0.25, CIRCLESMALL, BLUE, BLUE, 5.00, 43.82 +
             PartyGlobals.FireworksGlobalXOffset, -
             2.09 +
             PartyGlobals.FireworksGlobalYOffset, 49.31),
            (0.13, CIRCLELARGE, RED, RED, 5.00, 40.83 +
             PartyGlobals.FireworksGlobalXOffset, 10.33 +
             PartyGlobals.FireworksGlobalYOffset, 65.41),
            (0.25, CIRCLE, WHITE, WHITE, 5.00, 103.30 +
             PartyGlobals.FireworksGlobalXOffset, 12.66 +
             PartyGlobals.FireworksGlobalYOffset, 83.93),
            (0.25, RING, RED, RED, 5.00, 95.27 +
             PartyGlobals.FireworksGlobalXOffset, -
             9.92 +
             PartyGlobals.FireworksGlobalYOffset, 72.55),
            (0.37, POP, BLUE, BLUE, 5.00, 43.82 +
             PartyGlobals.FireworksGlobalXOffset, -
             2.09 +
             PartyGlobals.FireworksGlobalYOffset, 49.31),
            (0.13, CIRCLELARGE, BLUE, RED, 5.00, 107.72 +
             PartyGlobals.FireworksGlobalXOffset, -
             11.81 +
             PartyGlobals.FireworksGlobalYOffset, 50.51),
            (0.50, CIRCLESMALL, BLUE, WHITE, 5.00, 102.29 +
             PartyGlobals.FireworksGlobalXOffset, -
             8.59 +
             PartyGlobals.FireworksGlobalYOffset, 80.37),
            (0.31, RING, BLUE, BLUE, 5.00, 49.85 +
             PartyGlobals.FireworksGlobalXOffset, 12.65 +
             PartyGlobals.FireworksGlobalYOffset, 59.45),
            (0.44, RING, WHITE, WHITE, 5.00, 22.91 +
             PartyGlobals.FireworksGlobalXOffset, -
             0.70 +
             PartyGlobals.FireworksGlobalYOffset, 68.75),
            (0.13, CIRCLELARGE, WHITE, RED, 5.00, 91.87 +
             PartyGlobals.FireworksGlobalXOffset, 0.99 +
             PartyGlobals.FireworksGlobalYOffset, 72.32),
            (0.25, POP, BLUE, BLUE, 5.00, 43.82 +
             PartyGlobals.FireworksGlobalXOffset, -
             2.09 +
             PartyGlobals.FireworksGlobalYOffset, 49.31),
            (0.25, CIRCLE, RED, RED, 5.00, 2.49 +
             PartyGlobals.FireworksGlobalXOffset, 6.37 +
             PartyGlobals.FireworksGlobalYOffset, 43.93),
            (0.37, RING, BLUE, BLUE, 5.00, 84.93 +
             PartyGlobals.FireworksGlobalXOffset, 8.50 +
             PartyGlobals.FireworksGlobalYOffset, 77.25),
            (0.44, RING, WHITE, WHITE, 5.00, 85.37 +
             PartyGlobals.FireworksGlobalXOffset, -
             5.29 +
             PartyGlobals.FireworksGlobalYOffset, 75.30),
            (0.44, CIRCLELARGE, RED, RED, 5.00, 86.11 +
             PartyGlobals.FireworksGlobalXOffset, -
             11.82 +
             PartyGlobals.FireworksGlobalYOffset, 71.43),
            (0.31, CIRCLELARGE, WHITE, WHITE, 5.00, 79.35 +
             PartyGlobals.FireworksGlobalXOffset, 8.71 +
             PartyGlobals.FireworksGlobalYOffset, 77.00),
            (0.19, CIRCLELARGE, BLUE, BLUE, 5.00, 66.08 +
             PartyGlobals.FireworksGlobalXOffset, 0.98 +
             PartyGlobals.FireworksGlobalYOffset, 68.80),
        ),
    ],
}


def getShow(holidayId, index):
    showList = shows.get(holidayId, [])
    if index < len(showList):
        return showList[index]
    else:
        return None


def getShowDuration(eventId, index):
    show = getShow(eventId, index)
    duration = 0.0
    # Add in preshow duration
    duration += skyTransitionDuration
    duration += preShowPauseDuration
    for effect in show:
        waitTime, style, colorIndex1, colorIndex2, amp, x, y, z = effect
        duration += waitTime
    # Add in post show duration
    duration += postShowPauseDuration
    duration += preNormalMusicPauseDuration
    return duration
