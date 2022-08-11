class Settings():
    """A class to store all Alien Invasion settings."""

    def __init__(self):
        """Initialize the game settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5