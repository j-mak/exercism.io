NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot(object):
    commands = {'L': 'turn_left',
                'R': 'turn_right',
                'A': 'advance'
                }

    move = {
        NORTH: (0, 1),
        EAST: (1, 0),
        SOUTH: (0, -1),
        WEST: (-1, 0)
    }

    def __init__(self, direction=0, x_position=0, y_position=0):
        self.direction = direction
        self.x = x_position
        self.y = y_position

    @property
    def coordinates(self):
        """Returns robot coordinates."""
        return self.x, self.y

    @coordinates.setter
    def coordinates(self, pos):
        self.x += pos[0]
        self.y += pos[1]

    @property
    def bearing(self):
        """Returns robot direction."""
        return self.direction

    def advance(self):
        """Go one step ahead according robot direction."""
        self.coordinates = self.move[self.direction]

    def turn_left(self):
        """Rotate robot to left."""
        self.direction = (self.direction - 1) % 4

    def turn_right(self):
        """Rotate robot to right."""
        self.direction = (self.direction + 1) % 4

    def simulate(self, simulation_path):
        """Simulate robot path."""
        for step in simulation_path:
            getattr(self, self.commands[step])()
