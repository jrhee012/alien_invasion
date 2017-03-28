class Settings():
# A class to store all settings for Alien Invasion.

    def __init__(self):
        # Initialize the game's settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        self.ship_speed_factor = 20

        self.bullet_speed_factor = 30
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 127, 255, 0
        self.bullets_allowed = 10

        self.alien_speed_factor = 5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
