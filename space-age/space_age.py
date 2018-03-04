class SpaceAge(object):
    planets = {
        'mercury': 7600543.81992,
        'venus': 19414149.052176,
        'earth': 31557600,
        'mars': 59354032.69008,
        'jupiter': 374355659.124,
        'saturn': 929292362.8848,
        'uranus': 2651370019.3296,
        'neptune': 5200418560.032
    }

    def __init__(self, age):
        self.age = age
        for key in self.planets:
            setattr(self, 'on_' + key, self.calculate(key))

    @property
    def seconds(self):
        return self.age

    def calculate(self, key):
        return lambda: round(self.age / self.planets[key], 2)
